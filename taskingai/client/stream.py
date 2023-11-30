# Note: initially copied from https://github.com/florimondmanca/httpx-sse/blob/master/src/httpx_sse/_decoders.py
from __future__ import annotations

import json
from typing import TYPE_CHECKING, Any, Dict, Iterator, AsyncIterator, Type

import httpx

from .models.entity._base import TaskingaiBaseModel
from .exceptions import ApiException

from .rest import RESTSyncClientObject, RESTAsyncClientObject


class Stream(object):
    """Provides the core interface to iterate over a synchronous stream response."""

    response: httpx.Response

    def __init__(
        self,
        *,
        cast_map: Dict[str, Type[TaskingaiBaseModel]],
        response: httpx.Response,
        client: RESTSyncClientObject,
    ) -> None:
        if not isinstance(response, httpx.Response):
            raise TypeError("response must be an httpx.Response object")

        self.response = response
        self._cast_map = cast_map
        self._client = client
        self._decoder = SSEDecoder()
        self._iterator = self.__stream__()

    def __next__(self) -> TaskingaiBaseModel:
        return self._iterator.__next__()

    def __iter__(self) -> Iterator[TaskingaiBaseModel]:
        for item in self._iterator:
            yield item

    def _iter_events(self) -> Iterator[ServerSentEvent]:
        yield from self._decoder.iter(self.response.iter_lines())

    def _cast(self, obj_dict, class_type) -> TaskingaiBaseModel:
        cast_map = self._cast_map
        if class_type in cast_map:
            return cast_map[class_type](**obj_dict)
        else:
            raise ValueError(f"No class found for type '{class_type}'")

    def __stream__(self) -> Iterator[TaskingaiBaseModel]:
        print("streaming...")
        response = self.response
        iterator = self._iter_events()

        for sse in iterator:
            if sse.data.startswith("[DONE]"):
                break

            if sse.event is None:
                data = sse.json()
                if isinstance(data, Dict) and data.get("error"):
                    raise ApiException(
                        status=response.status_code,
                        reason="An error ocurred during streaming",
                        http_resp=response,
                    )

                object_type = data.get("object")
                # todo: raise valid format error
                yield self._cast(data, object_type)

        # Ensure the entire stream is consumed
        for sse in iterator:
            ...


class ServerSentEvent:
    def __init__(
        self,
        *,
        event: str | None = None,
        data: str | None = None,
        id: str | None = None,
        retry: int | None = None,
    ) -> None:
        if data is None:
            data = ""

        self._id = id
        self._data = data
        self._event = event or None
        self._retry = retry

    @property
    def event(self) -> str | None:
        return self._event

    @property
    def id(self) -> str | None:
        return self._id

    @property
    def retry(self) -> int | None:
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
    _event: str | None
    _retry: int | None
    _last_event_id: str | None

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

    def decode(self, line: str) -> ServerSentEvent | None:
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
