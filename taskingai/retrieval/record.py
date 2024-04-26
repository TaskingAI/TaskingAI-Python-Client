from typing import Any, Dict, List, Optional, Union

from taskingai.client.apis import *
from taskingai.client.models import *

__all__ = [
    "Record",
    "RecordType",
    "get_record",
    "list_records",
    "create_record",
    "update_record",
    "delete_record",
    "a_get_record",
    "a_list_records",
    "a_create_record",
    "a_update_record",
    "a_delete_record",
]


def _validate_record_type(
    type: Union[RecordType, str],
    content: Optional[str] = None,
    file_id: Optional[str] = None,
    url: Optional[str] = None,
):
    type = type if isinstance(type, RecordType) else RecordType(type)
    if type == RecordType.TEXT and not content:
        raise ValueError("A valid content must be provided when type is 'text'.")
    if type == RecordType.FILE and not file_id:
        raise ValueError("A valid file ID must be provided when type is 'file'.")
    if type == RecordType.WEB:
        if not url:
            raise ValueError("A valid url must be provided when type is 'web'.")
        if not url.startswith("https://"):
            raise ValueError("URL only supports https.")
    return type


def list_records(
    collection_id: str,
    *,
    order: str = "desc",
    limit: int = 20,
    after: Optional[str] = None,
    before: Optional[str] = None,
) -> List[Record]:
    """
    List records.

    :param collection_id: The ID of the collection.
    :param order: The order of the records. It can be "asc" or "desc".
    :param limit: The maximum number of assistants to return.
    :param after: The cursor to get the next page of records.
    :param before: The cursor to get the previous page of records.
    :return: The list of records.
    """

    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    # only add non-None parameters
    payload = RecordListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: RecordListResponse = api_list_records(collection_id=collection_id, payload=payload)
    return response.data


async def a_list_records(
    collection_id: str,
    *,
    order: str = "desc",
    limit: int = 20,
    after: Optional[str] = None,
    before: Optional[str] = None,
) -> List[Record]:
    """
    List records in async mode.
    :param collection_id: The ID of the collection.
    :param order: The order of the records. It can be "asc" or "desc".
    :param limit: The maximum number of records to return.
    :param after: The cursor to get the next page of records.
    :param before: The cursor to get the previous page of records.
    :return: The list of records.
    """

    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    # only add non-None parameters
    payload = RecordListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: RecordListResponse = await async_api_list_records(collection_id=collection_id, payload=payload)
    return response.data


def get_record(collection_id: str, record_id: str) -> Record:
    """
    Get a record.

    :param collection_id: The ID of the collection.
    :param record_id: The ID of the record.
    """

    response: RecordGetResponse = api_get_record(
        collection_id=collection_id,
        record_id=record_id,
    )
    return response.data


async def a_get_record(collection_id: str, record_id: str) -> Record:
    """
    Get a record in async mode.

    :param collection_id: The ID of the collection.
    :param record_id: The ID of the record.
    """

    response: RecordGetResponse = await async_api_get_record(
        collection_id=collection_id,
        record_id=record_id,
    )
    return response.data


def create_record(
    collection_id: str,
    *,
    type: Union[RecordType, str],
    text_splitter: Union[TextSplitter, Dict[str, Any]],
    title: Optional[str] = None,
    content: Optional[str] = None,
    file_id: Optional[str] = None,
    url: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Record:
    """
    Create a record.

    :param collection_id: The ID of the collection.
    :param type: The type of the record. It can be "text", "web" or "file".
    :param text_splitter: The text splitter to split records into chunks.
    :param title: The title of the record.
    :param content: The content of the record. It is required when the type is "text".
    :param file_id: The file ID of the record. It is required when the type is "file".
    :param url: The URL of the record. It is required when the type is "web".
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created record object.
    """
    type = _validate_record_type(type, content, file_id, url)
    text_splitter = text_splitter if isinstance(text_splitter, TextSplitter) else TextSplitter(**text_splitter)

    body = RecordCreateRequest(
        title=title or "",
        type=type,
        text_splitter=text_splitter,
        content=content,
        file_id=file_id,
        url=url,
        metadata=metadata or {},
    )
    response: RecordCreateResponse = api_create_record(collection_id=collection_id, payload=body)
    return response.data


async def a_create_record(
    collection_id: str,
    *,
    type: Union[RecordType, str],
    text_splitter: Union[TextSplitter, Dict[str, Any]],
    title: Optional[str] = None,
    content: Optional[str] = None,
    file_id: Optional[str] = None,
    url: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Record:
    """
    Create a record in async mode.

    :param collection_id: The ID of the collection.
    :param type: The type of the record. It can be "text", "web" or "file".
    :param text_splitter: The text splitter to split records into chunks.
    :param title: The title of the record.
    :param content: The content of the record. It is required when the type is "text".
    :param file_id: The file ID of the record. It is required when the type is "file".
    :param url: The URL of the record. It is required when the type is "web".
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created record object.
    """

    type = _validate_record_type(type, content, file_id, url)
    text_splitter = text_splitter if isinstance(text_splitter, TextSplitter) else TextSplitter(**text_splitter)

    body = RecordCreateRequest(
        title=title or "",
        type=type,
        text_splitter=text_splitter,
        content=content,
        file_id=file_id,
        url=url,
        metadata=metadata or {},
    )
    response: RecordCreateResponse = await async_api_create_record(collection_id=collection_id, payload=body)
    return response.data


def update_record(
    record_id: str,
    collection_id: str,
    *,
    type: Optional[Union[RecordType, str]] = None,
    text_splitter: Optional[Union[TextSplitter, Dict[str, Any]]] = None,
    title: Optional[str] = None,
    content: Optional[str] = None,
    file_id: Optional[str] = None,
    url: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Record:
    """
    Update a record.

    :param collection_id: The ID of the collection.
    :param type: The type of the record. It can be "text", "web" or "file".
    :param text_splitter: The text splitter to split records into chunks.
    :param title: The title of the record.
    :param content: The content of the record. It is required when the type is "text".
    :param file_id: The file ID of the record. It is required when the type is "file".
    :param url: The URL of the record. It is required when the type is "web".
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created record object.
    """

    if type:
        type = type if isinstance(type, RecordType) else RecordType(type)
    if text_splitter:
        text_splitter = text_splitter if isinstance(text_splitter, TextSplitter) else TextSplitter(**text_splitter)

    body = RecordUpdateRequest(
        title=title,
        type=type,
        text_splitter=text_splitter,
        content=content,
        file_id=file_id,
        url=url,
        metadata=metadata or {},
    )
    response: RecordUpdateResponse = api_update_record(collection_id=collection_id, record_id=record_id, payload=body)
    return response.data


async def a_update_record(
    record_id: str,
    collection_id: str,
    *,
    type: Optional[Union[RecordType, str]] = None,
    text_splitter: Optional[Union[TextSplitter, Dict[str, Any]]] = None,
    title: Optional[str] = None,
    content: Optional[str] = None,
    file_id: Optional[str] = None,
    url: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Record:
    """
    Update a record in async mode.

    :param collection_id: The ID of the collection.
    :param type: The type of the record. It can be "text", "web" or "file".
    :param text_splitter: The text splitter to split records into chunks.
    :param title: The title of the record.
    :param content: The content of the record. It is required when the type is "text".
    :param file_id: The file ID of the record. It is required when the type is "file".
    :param url: The URL of the record. It is required when the type is "web".
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created record object.
    """

    if type:
        type = type if isinstance(type, RecordType) else RecordType(type)
    if text_splitter:
        text_splitter = text_splitter if isinstance(text_splitter, TextSplitter) else TextSplitter(**text_splitter)

    body = RecordUpdateRequest(
        title=title,
        type=type,
        text_splitter=text_splitter,
        content=content,
        file_id=file_id,
        url=url,
        metadata=metadata or {},
    )
    response: RecordUpdateResponse = await async_api_update_record(
        collection_id=collection_id, record_id=record_id, payload=body
    )
    return response.data


def delete_record(
    collection_id: str,
    record_id: str,
) -> None:
    """
    Delete a record.

    :param collection_id: The ID of the collection.
    :param record_id: The ID of the record.
    """

    api_delete_record(collection_id=collection_id, record_id=record_id)


async def a_delete_record(
    collection_id: str,
    record_id: str,
) -> None:
    """
    Delete a record in async mode.

    :param collection_id: The ID of the collection.
    :param record_id: The ID of the record.
    """

    await async_api_delete_record(collection_id=collection_id, record_id=record_id)
