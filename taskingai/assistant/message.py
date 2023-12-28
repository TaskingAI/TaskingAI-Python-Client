from typing import Optional, List, Dict, Union

from taskingai.client.utils import get_api_instance, ModuleType
from taskingai.client.models import (
    Message,
    MessageRole,
    MessageContent,
    MessageChunk,
)
from taskingai.client.models import (
    MessageCreateRequest,
    MessageCreateResponse,
    MessageUpdateRequest,
    MessageUpdateResponse,
    MessageGetResponse,
    MessageListResponse,
    MessageGenerateRequest
)
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

    api_instance = get_api_instance(ModuleType.assistant)
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: MessageListResponse = api_instance.list_messages(
        assistant_id=assistant_id,
        chat_id=chat_id,
        **params
    )
    messages: List[Message] = [Message(**item) for item in response.data]
    return messages


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

    api_instance = get_api_instance(ModuleType.assistant, async_client=True)
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: MessageListResponse = await api_instance.list_messages(
        assistant_id=assistant_id,
        chat_id=chat_id,
        **params
    )
    messages: List[Message] = [Message(**item) for item in response.data]
    return messages


def get_message(
    assistant_id: str,
    chat_id: str,
    message_id: str
) -> Message:
    """
    Get a message.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    :param message_id: The ID of the message.
    """

    api_instance = get_api_instance(ModuleType.assistant)
    response: MessageGetResponse = api_instance.get_message(
        assistant_id=assistant_id,
        chat_id=chat_id,
        message_id=message_id,
    )
    message: Message = Message(**response.data)
    return message


async def a_get_message(
    assistant_id: str,
    chat_id: str,
    message_id: str
) -> Message:
    """
    Get a message in async mode.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    :param message_id: The ID of the message.
    """

    api_instance = get_api_instance(ModuleType.assistant, async_client=True)
    response: MessageGetResponse = await api_instance.get_message(
        assistant_id=assistant_id,
        chat_id=chat_id,
        message_id=message_id,
    )
    message: Message = Message(**response.data)
    return message



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

    api_instance = get_api_instance(ModuleType.assistant)
    body = MessageCreateRequest(
        role=MessageRole.user,
        content=MessageContent(text=text),
        metadata=metadata,
    )
    response: MessageCreateResponse = api_instance.create_message(
        assistant_id=assistant_id,
        chat_id=chat_id,
        body=body
    )
    message: Message = Message(**response.data)
    return message


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

    api_instance = get_api_instance(ModuleType.assistant, async_client=True)
    body = MessageCreateRequest(
        role=MessageRole.user,
        content=MessageContent(text=text),
        metadata=metadata,
    )
    response: MessageCreateResponse = await api_instance.create_message(
        assistant_id=assistant_id,
        chat_id=chat_id,
        body=body
    )
    message: Message = Message(**response.data)
    return message


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

    api_instance = get_api_instance(ModuleType.assistant)
    body = MessageUpdateRequest(
        metadata=metadata,
    )
    response: MessageUpdateResponse = api_instance.update_message(
        assistant_id=assistant_id,
        chat_id=chat_id,
        message_id=message_id,
        body=body
    )
    message: Message = Message(**response.data)
    return message


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

    api_instance = get_api_instance(ModuleType.assistant, async_client=True)
    body = MessageUpdateRequest(
        metadata=metadata,
    )
    response: MessageUpdateResponse = await api_instance.update_message(
        assistant_id=assistant_id,
        chat_id=chat_id,
        message_id=message_id,
        body=body
    )
    message: Message = Message(**response.data)
    return message



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
    :param text: The text content of the message.
    :param metadata: The message metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The generated message object.
    """

    api_instance = get_api_instance(ModuleType.assistant)
    body = MessageGenerateRequest(
        system_prompt_variables=system_prompt_variables,
        stream=stream,
    )

    if not stream:
        response = api_instance.generate_message(
            assistant_id=assistant_id,
            chat_id=chat_id,
            body=body,
            stream=False,
        )
        message: Message = Message(**response["data"])
        return message
    else:
        response: Stream = api_instance.generate_message(
            assistant_id=assistant_id,
            chat_id=chat_id,
            body=body,
            stream=True,
            _preload_content=False
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
    :param text: The text content of the message.
    :param metadata: The message metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The generated message object.
    """

    api_instance = get_api_instance(ModuleType.assistant, async_client=True)
    body = MessageGenerateRequest(
        system_prompt_variables=system_prompt_variables,
        stream=stream,
    )

    if not stream:
        response = await api_instance.generate_message(
            assistant_id=assistant_id,
            chat_id=chat_id,
            body=body,
            stream=False,
        )
        message: Message = Message(**response["data"])
        return message
    else:
        response: AsyncStream = await api_instance.generate_message(
            assistant_id=assistant_id,
            chat_id=chat_id,
            body=body,
            stream=True,
            _preload_content=False
        )
        return response


