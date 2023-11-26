from typing import Optional, List, Dict

from taskingai.client.utils import get_assistant_api_instance
from taskingai.client.models import Chat
from taskingai.client.models import ChatCreateRequest, ChatCreateResponse, \
    ChatUpdateRequest, ChatUpdateResponse, \
    ChatGetResponse, ChatListResponse

__all__ = [
    "Chat",
    "get_chat",
    "list_chats",
    "create_chat",
    "update_chat",
    "delete_chat",
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

    api_instance = get_assistant_api_instance()
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: ChatListResponse = api_instance.list_chats(
        assistant_id=assistant_id,
        **params
    )
    chats: List[Chat] = [Chat(**item) for item in response.data]
    return chats


def get_chat(assistant_id: str, chat_id: str) -> Chat:
    """
    Get a chat.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    """

    api_instance = get_assistant_api_instance()
    response: ChatGetResponse = api_instance.get_chat(
        assistant_id=assistant_id,
        chat_id=chat_id,
    )
    chat: Chat = Chat(**response.data)
    return chat


def create_chat(
    assistant_id: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Chat:
    """
    Create a chat.

    :param assistant_id: The ID of the assistant.
    :param metadata: The chat metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created chat object.
    """

    api_instance = get_assistant_api_instance()
    body = ChatCreateRequest(
        metadata=metadata,
    )
    response: ChatCreateResponse = api_instance.create_chat(
        assistant_id=assistant_id,
        body=body
    )
    chat: Chat = Chat(**response.data)
    return chat


def update_chat(
    assistant_id: str,
    chat_id: str,
    metadata: Dict[str, str],
) -> Chat:
    """
    Update a chat.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The updated chat object.
    """

    api_instance = get_assistant_api_instance()
    body = ChatUpdateRequest(
        metadata=metadata,
    )
    response: ChatUpdateResponse = api_instance.update_chat(
        assistant_id=assistant_id,
        chat_id=chat_id,
        body=body
    )
    chat: Chat = Chat(**response.data)
    return chat


def delete_chat(
    assistant_id: str,
    chat_id: str,
) -> None:
    """
    Delete a chat.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    """

    api_instance = get_assistant_api_instance()
    api_instance.delete_chat(assistant_id=assistant_id, chat_id=chat_id)

