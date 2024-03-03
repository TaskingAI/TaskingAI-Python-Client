from typing import Optional, List, Dict, Union

from taskingai.client.models import *
from taskingai.client.apis import *
from taskingai.client.stream_apis import *
from taskingai.client.stream import Stream, AsyncStream

__all__ = [
    "Message",
    "MessageChunk",
    "get_message",
    "list_messages",
    "create_message",
    "update_message",
    "generate_message",
    "a_get_message",
    "a_list_messages",
    "a_create_message",
    "a_update_message",
    "a_generate_message",
]


def list_messages(
    assistant_id: str,
    chat_id: str,
    order: str = "desc",
    limit: int = 20,
    after: Optional[str] = None,
    before: Optional[str] = None,
) -> List[Message]:
    """
    List messages.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    :param order: The order of the messages. It can be "asc" or "desc".
    :param limit: The maximum number of messages to return.
    :param after: The cursor to get the next page of messages.
    :param before: The cursor to get the previous page of messages.
    :return: The list of messages.
    """
    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    # only add non-None parameters
    payload = MessageListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: MessageListResponse = api_list_messages(
        assistant_id=assistant_id,
        chat_id=chat_id,
        payload=payload,
    )
    return response.data


async def a_list_messages(
    assistant_id: str,
    chat_id: str,
    order: str = "desc",
    limit: int = 20,
    after: Optional[str] = None,
    before: Optional[str] = None,
) -> List[Message]:
    """
    List messages in async mode.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    :param order: The order of the messages. It can be "asc" or "desc".
    :param limit: The maximum number of messages to return.
    :param after: The cursor to get the next page of messages.
    :param before: The cursor to get the previous page of messages.
    :return: The list of messages.
    """
    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    # only add non-None parameters
    payload = MessageListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: MessageListResponse = await async_api_list_messages(
        assistant_id=assistant_id,
        chat_id=chat_id,
        payload=payload,
    )
    return response.data


def get_message(assistant_id: str, chat_id: str, message_id: str) -> Message:
    """
    Get a message.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    :param message_id: The ID of the message.
    """

    response: MessageGetResponse = api_get_message(
        assistant_id=assistant_id,
        chat_id=chat_id,
        message_id=message_id,
    )
    return response.data


async def a_get_message(assistant_id: str, chat_id: str, message_id: str) -> Message:
    """
    Get a message in async mode.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    :param message_id: The ID of the message.
    """

    response: MessageGetResponse = await async_api_get_message(
        assistant_id=assistant_id,
        chat_id=chat_id,
        message_id=message_id,
    )
    return response.data


def create_message(
    assistant_id: str,
    chat_id: str,
    text: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Message:
    """
    Create a message.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    :param text: The text content of the message.
    :param metadata: The message metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created message object.
    """

    body = MessageCreateRequest(
        role=MessageRole.USER,
        content=MessageContent(text=text),
        metadata=metadata or {},
    )
    response: MessageCreateResponse = api_create_message(assistant_id=assistant_id, chat_id=chat_id, payload=body)
    return response.data


async def a_create_message(
    assistant_id: str,
    chat_id: str,
    text: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Message:
    """
    Create a message in async mode.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    :param text: The text content of the message.
    :param metadata: The message metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created message object.
    """

    body = MessageCreateRequest(
        role=MessageRole.USER,
        content=MessageContent(text=text),
        metadata=metadata or {},
    )
    response: MessageCreateResponse = await async_api_create_message(
        assistant_id=assistant_id, chat_id=chat_id, payload=body
    )
    return response.data


def update_message(
    assistant_id: str,
    chat_id: str,
    message_id: str,
    metadata: Dict[str, str],
) -> Message:
    """
    Update a message.

    :param assistant_id: The ID of the assistant.
    :param message_id: The ID of the message.
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The updated message object.
    """

    body = MessageUpdateRequest(
        metadata=metadata or {},
    )
    response: MessageUpdateResponse = api_update_message(
        assistant_id=assistant_id, chat_id=chat_id, message_id=message_id, payload=body
    )
    return response.data


async def a_update_message(
    assistant_id: str,
    chat_id: str,
    message_id: str,
    metadata: Dict[str, str],
) -> Message:
    """
    Update a message in async mode.

    :param assistant_id: The ID of the assistant.
    :param message_id: The ID of the message.
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The updated message object.
    """

    body = MessageUpdateRequest(
        metadata=metadata or {},
    )
    response: MessageUpdateResponse = await async_api_update_message(
        assistant_id=assistant_id, chat_id=chat_id, message_id=message_id, payload=body
    )
    return response.data


def generate_message(
    assistant_id: str,
    chat_id: str,
    system_prompt_variables: Optional[Dict] = None,
    stream: bool = False,
) -> Union[Message, Stream]:
    """
    Generate a message.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    :param system_prompt_variables: The system prompt variables.
    :param stream: Whether to return a stream.
    :return: The generated message object.
    """

    body = MessageGenerateRequest(
        system_prompt_variables=system_prompt_variables,
        stream=stream,
    )

    if not stream:
        response: MessageGenerateResponse = api_generate_message(
            assistant_id=assistant_id,
            chat_id=chat_id,
            payload=body,
        )
        return response.data
    else:
        response: Stream = stream_api_generate_message(
            assistant_id=assistant_id, chat_id=chat_id, payload=body, _preload_content=False
        )
        return response


async def a_generate_message(
    assistant_id: str,
    chat_id: str,
    system_prompt_variables: Optional[Dict] = None,
    stream: bool = False,
) -> Union[Message, AsyncStream]:
    """
    Generate a message in async mode.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    :param system_prompt_variables: The system prompt variables.
    :param stream: Whether to return a stream.
    :return: The generated message object.
    """

    body = MessageGenerateRequest(
        system_prompt_variables=system_prompt_variables,
        stream=stream,
    )

    if not stream:
        response: MessageGenerateResponse = await async_api_generate_message(
            assistant_id=assistant_id,
            chat_id=chat_id,
            payload=body,
        )
        return response.data
    else:
        response: AsyncStream = await async_stream_api_generate_message(
            assistant_id=assistant_id, chat_id=chat_id, payload=body, stream=True, _preload_content=False
        )
        return response
