# Note: initially copied from https://github.com/florimondmanca/httpx-sse/blob/master/src/httpx_sse/_decoders.py
from __future__ import annotations

import json
from typing import Any, Dict, Iterator, AsyncIterator, Optional
from .models import (
    MessageChunk,
    Message,
    ChatCompletion,
    ChatCompletionChunk
)

from .models.entity._base import TaskingaiBaseModel

from .exceptions import ApiException


def _cast(item: Dict):
    if item.get("object") == "ChatCompletion":
        return ChatCompletion(**item)
    elif item.get("object") == "ChatCompletionChunk":
        return ChatCompletionChunk(**item)
    elif item.get("object") == "Message":
        return Message(**item)
    elif item.get("object") == "MessageChunk":
        return MessageChunk(**item)
    else:
        # cannot cast, keep the original dict
        return item

class Stream(object):
    """Provides the core interface to iterate over a synchronous stream response."""

    def __init__(self, stream_generator):
        self._stream_generator = stream_generator
        self._decoder = SSEDecoder()
        self._iterator = self.__stream__()

    def __next__(self) -> Dict:
        return self._iterator.__next__()

    def __iter__(self) -> Iterator[Dict]:
        for item in self._iterator:
            yield item

    def _iter_events(self) -> Iterator[ServerSentEvent]:
        yield from self._decoder.iter(self._stream_generator)

    def __stream__(self) -> Iterator[Dict]:
        iterator = self._iter_events()

        for sse in iterator:
            if sse.data.startswith("[DONE]"):
                break

            if sse.event is None:
                data = sse.json()
                if isinstance(data, Dict) and data.get("error"):
                    raise ApiException(
                        status=400,  # or appropriate status code
                        reason="An error occurred during streaming",
                    )

                yield _cast(data)

        # Ensure the entire stream is consumed
        for sse in iterator:
            ...

class AsyncStream(object):
    """Provides the core interface to iterate over an asynchronous stream response."""

    def __init__(self, async_stream_generator):
        self._async_stream_generator = async_stream_generator
        self._decoder = SSEDecoder()  # Assuming SSEDecoder is compatible with async
        self._iterator = self.__stream__()

    async def __anext__(self) -> Dict:
        return await self._iterator.__anext__()

    async def __aiter__(self) -> AsyncIterator[Dict]:
        async for item in self._iterator:
            yield item

    async def _iter_events(self) -> AsyncIterator[ServerSentEvent]:
        async for sse in self._decoder.aiter(self._async_stream_generator):
            yield sse

    async def __stream__(self) -> AsyncIterator[Dict]:
        async for sse in self._iter_events():
            if sse.data.startswith("[DONE]"):
                break

            if sse.event is None:
                data = sse.json()
                if isinstance(data, Dict) and data.get("error"):
                    raise ApiException(
                        status=400,  # or appropriate status code
                        reason="An error occurred during streaming",
                    )

                yield _cast(data)

        # Ensure the entire stream is consumed
        async for sse in self._iter_events():
            ...

class ServerSentEvent:
    def __init__(
        self,
        *,
        event: Optional[str] = None,
        data: Optional[str] = None,
        id: Optional[str] = None,
        retry: Optional[int] = None,
    ) -> None:
        if data is None:
            data = ""

        self._id = id
        self._data = data
        self._event = event or None
        self._retry = retry

    @property
    def event(self) -> Optional[str]:
        return self._event

    @property
    def id(self) -> Optional[str]:
        return self._id

    @property
    def retry(self) -> Optional[int]:
        return self._retry

    @property
    def data(self) -> str:
        return self._data

    def json(self) -> Any:
        return json.loads(self.data)

    def __repr__(self) -> str:
        return f"ServerSentEvent(event={self.event}, data={self.data}, id={self.id}, retry={self.retry})"

class SSEDecoder:
    _data: list[str]
    _event: Optional[str]
    _retry: Optional[int]
    _last_event_id: Optional[str]

    def __init__(self) -> None:
        self._event = None
        self._data = []
        self._last_event_id = None
        self._retry = None

    def iter(self, iterator: Iterator[str]) -> Iterator[ServerSentEvent]:
        """Given an iterator that yields lines, iterate over it & yield every event encountered"""
        for line in iterator:
            line = line.rstrip("\n")
            sse = self.decode(line)
            if sse is not None:
                yield sse

    async def aiter(self, iterator: AsyncIterator[str]) -> AsyncIterator[ServerSentEvent]:
        """Given an async iterator that yields lines, iterate over it & yield every event encountered"""
        async for line in iterator:
            line = line.rstrip("\n")
            sse = self.decode(line)
            if sse is not None:
                yield sse

    def decode(self, line: str) -> Optional[ServerSentEvent]:
        # See: https://html.spec.whatwg.org/multipage/server-sent-events.html#event-stream-interpretation  # noqa: E501

        if not line:
            if not self._event and not self._data and not self._last_event_id and self._retry is None:
                return None

            sse = ServerSentEvent(
                event=self._event,
                data="\n".join(self._data),
                id=self._last_event_id,
                retry=self._retry,
            )

            # NOTE: as per the SSE spec, do not reset last_event_id.
            self._event = None
            self._data = []
            self._retry = None

            return sse

        if line.startswith(":"):
            return None

        fieldname, _, value = line.partition(":")

        if value.startswith(" "):
            value = value[1:]

        if fieldname == "event":
            self._event = value
        elif fieldname == "data":
            self._data.append(value)
        elif fieldname == "id":
            if "\0" in value:
                pass
            else:
                self._last_event_id = value
        elif fieldname == "retry":
            try:
                self._retry = int(value)
            except (TypeError, ValueError):
                pass
        else:
            pass  # Field is ignored.

        return None
