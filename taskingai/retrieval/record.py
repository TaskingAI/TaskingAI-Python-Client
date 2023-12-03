from typing import Optional, List, Dict

from taskingai.client.utils import get_api_instance, ModuleType
from taskingai.client.models import Record
from taskingai.client.models import RecordCreateRequest, RecordCreateResponse, \
    RecordUpdateRequest, RecordUpdateResponse, \
    RecordGetResponse, RecordListResponse

__all__ = [
    "Record",
    "get_record",
    "list_records",
    "create_text_record",
    "update_record",
    "delete_record",
    "a_get_record",
    "a_list_records",
    "a_create_text_record",
    "a_update_record",
    "a_delete_record",
]


def list_records(
        collection_id: str,
        order: str = "desc",
        limit: int = 20,
        after: Optional[str] = None,
        before: Optional[str] = None,
) -> List[Record]:
    """
    List records.

    :param order: The order of the records. It can be "asc" or "desc".
    :param limit: The maximum number of assistants to return.
    :param after: The cursor to get the next page of records.
    :param before: The cursor to get the previous page of records.
    :return: The list of records.
    """

    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    api_instance = get_api_instance(ModuleType.retrieval)
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: RecordListResponse = api_instance.list_records(
        collection_id=collection_id,
        **params
    )
    records: List[Record] = [Record(**item) for item in response.data]
    return records


async def a_list_records(
        collection_id: str,
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

    api_instance = get_api_instance(ModuleType.retrieval, async_client=True)
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: RecordListResponse = await api_instance.list_records(
        collection_id=collection_id,
        **params
    )
    records: List[Record] = [Record(**item) for item in response.data]
    return records



def get_record(collection_id: str, record_id: str) -> Record:
    """
    Get a record.

    :param collection_id: The ID of the collection.
    :param record_id: The ID of the record.
    """

    api_instance = get_api_instance(ModuleType.retrieval)
    response: RecordGetResponse = api_instance.get_record(
        collection_id=collection_id,
        record_id=record_id,
    )
    record: Record = Record(**response.data)
    return record


async def a_get_record(collection_id: str, record_id: str) -> Record:
    """
    Get a record in async mode.

    :param collection_id: The ID of the collection.
    :param record_id: The ID of the record.
    """

    api_instance = get_api_instance(ModuleType.retrieval, async_client=True)
    response: RecordGetResponse = await api_instance.get_record(
        collection_id=collection_id,
        record_id=record_id,
    )
    record: Record = Record(**response.data)
    return record


def create_text_record(
    collection_id: str,
    # todo: support file
    text: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Record:
    """
    Create a record.

    :param collection_id: The ID of the collection.
    :param text: The text content of the record.
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created record object.
    """

    api_instance = get_api_instance(ModuleType.retrieval)
    body = RecordCreateRequest(
        type="text",
        text=text,
        metadata=metadata,
    )
    response: RecordCreateResponse = api_instance.create_record(
        collection_id=collection_id,
        body=body
    )
    record: Record = Record(**response.data)
    return record


async def a_create_text_record(
    collection_id: str,
    # todo: support file
    text: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Record:
    """
    Create a record in async mode.

    :param collection_id: The ID of the collection.
    :param text: The text content of the record.
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created record object.
    """

    api_instance = get_api_instance(ModuleType.retrieval, async_client=True)
    body = RecordCreateRequest(
        type="text",
        text=text,
        metadata=metadata,
    )
    response: RecordCreateResponse = await api_instance.create_record(
        collection_id=collection_id,
        body=body
    )
    record: Record = Record(**response.data)
    return record


def update_record(
    collection_id: str,
    record_id: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Record:
    """
    Update a record.

    :param collection_id: The ID of the collection.
    :param record_id: The ID of the record.
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The collection object.
    """

    api_instance = get_api_instance(ModuleType.retrieval)
    body = RecordUpdateRequest(
        metadata=metadata,
    )
    response: RecordUpdateResponse = api_instance.update_record(
        collection_id=collection_id,
        record_id=record_id,
        body=body
    )
    record: Record = Record(**response.data)
    return record


async def a_update_record(
    collection_id: str,
    record_id: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Record:
    """
    Update a record in async mode.

    :param collection_id: The ID of the collection.
    :param record_id: The ID of the record.
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The collection object.
    """

    api_instance = get_api_instance(ModuleType.retrieval, async_client=True)
    body = RecordUpdateRequest(
        metadata=metadata,
    )
    response: RecordUpdateResponse = await api_instance.update_record(
        collection_id=collection_id,
        record_id=record_id,
        body=body
    )
    record: Record = Record(**response.data)
    return record


def delete_record(
    collection_id: str,
    record_id: str,
) -> None:
    """
    Delete a record.

    :param collection_id: The ID of the collection.
    :param record_id: The ID of the record.
    """

    api_instance = get_api_instance(ModuleType.retrieval)
    api_instance.delete_record(collection_id=collection_id, record_id=record_id)


async def a_delete_record(
    collection_id: str,
    record_id: str,
) -> None:
    """
    Delete a record in async mode.

    :param collection_id: The ID of the collection.
    :param record_id: The ID of the record.
    """

    api_instance = get_api_instance(ModuleType.retrieval, async_client=True)
    await api_instance.delete_record(collection_id=collection_id, record_id=record_id)




