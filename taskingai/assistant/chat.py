from typing import Optional, List, Dict

from taskingai.client.models import *
from taskingai.client.apis import *

__all__ = [
    "Chat",
    "get_chat",
    "list_chats",
    "create_chat",
    "update_chat",
    "delete_chat",
    "a_get_chat",
    "a_list_chats",
    "a_create_chat",
    "a_update_chat",
    "a_delete_chat",
]


def list_chats(
    assistant_id: str,
    order: str = "desc",
    limit: int = 20,
    after: Optional[str] = None,
    before: Optional[str] = None,
) -> List[Chat]:
    """
    List chats.
    :param assistant_id: The ID of the assistant.
    :param order: The order of the chats. It can be "asc" or "desc".
    :param limit: The maximum number of chats to return.
    :param after: The cursor to get the next page of chats.
    :param before: The cursor to get the previous page of chats.
    :return: The list of chats.
    """
    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    # only add non-None parameters
    payload = ChatListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: ChatListResponse = api_list_chats(
        assistant_id=assistant_id,
        payload=payload,
    )
    return response.data


async def a_list_chats(
    assistant_id: str,
    order: str = "desc",
    limit: int = 20,
    after: Optional[str] = None,
    before: Optional[str] = None,
) -> List[Chat]:
    """
    List chats in async mode.
    :param assistant_id: The ID of the assistant.
    :param order: The order of the chats. It can be "asc" or "desc".
    :param limit: The maximum number of chats to return.
    :param after: The cursor to get the next page of chats.
    :param before: The cursor to get the previous page of chats.
    :return: The list of chats.
    """
    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    # only add non-None parameters
    payload = ChatListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: ChatListResponse = await async_api_list_chats(
        assistant_id=assistant_id,
        payload=payload,
    )
    return response.data


def get_chat(assistant_id: str, chat_id: str) -> Chat:
    """
    Get a chat.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    """

    response: ChatGetResponse = api_get_chat(
        assistant_id=assistant_id,
        chat_id=chat_id,
    )
    return response.data


async def a_get_chat(assistant_id: str, chat_id: str) -> Chat:
    """
    Get a chat in async mode.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    """

    response: ChatGetResponse = await async_api_get_chat(
        assistant_id=assistant_id,
        chat_id=chat_id,
    )
    return response.data


def create_chat(
    assistant_id: str,
    name: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Chat:
    """
    Create a chat.

    :param assistant_id: The ID of the assistant.
    :param name: The name of the chat.
    :param metadata: The chat metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created chat object.
    """

    body = ChatCreateRequest(
        name=name,
        metadata=metadata or {},
    )
    response: ChatCreateResponse = api_create_chat(assistant_id=assistant_id, payload=body)
    return response.data


async def a_create_chat(
    assistant_id: str,
    name: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Chat:
    """
    Create a chat in async mode.

    :param assistant_id: The ID of the assistant.
    :param name: The name of the chat.
    :param metadata: The chat metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created chat object.
    """

    body = ChatCreateRequest(
        name=name,
        metadata=metadata or {},
    )
    response: ChatCreateResponse = await async_api_create_chat(assistant_id=assistant_id, payload=body)
    return response.data


def update_chat(
    assistant_id: str,
    chat_id: str,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Chat:
    """
    Update a chat.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    :param name: The name of the chat.
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The updated chat object.
    """

    body = ChatUpdateRequest(
        name=name,
        metadata=metadata,
    )
    response: ChatUpdateResponse = api_update_chat(assistant_id=assistant_id, chat_id=chat_id, payload=body)
    return response.data


async def a_update_chat(
    assistant_id: str,
    chat_id: str,
    name: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Chat:
    """
    Update a chat in async mode.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    :param name: The name of the chat.
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The updated chat object.
    """

    body = ChatUpdateRequest(
        name=name,
        metadata=metadata,
    )
    response: ChatUpdateResponse = await async_api_update_chat(assistant_id=assistant_id, chat_id=chat_id, payload=body)
    return response.data


def delete_chat(
    assistant_id: str,
    chat_id: str,
) -> None:
    """
    Delete a chat.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    """

    api_delete_chat(assistant_id=assistant_id, chat_id=chat_id)


async def a_delete_chat(
    assistant_id: str,
    chat_id: str,
) -> None:
    """
    Delete a chat in async mode.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    """

    await async_api_delete_chat(assistant_id=assistant_id, chat_id=chat_id)
