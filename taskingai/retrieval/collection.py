from typing import Optional, List, Dict

from taskingai.client.models import *
from taskingai.client.apis import *

__all__ = [
    "Collection",
    "get_collection",
    "list_collections",
    "create_collection",
    "update_collection",
    "delete_collection",
    "a_get_collection",
    "a_list_collections",
    "a_create_collection",
    "a_update_collection",
    "a_delete_collection",
]


def list_collections(
    *,
    order: str = "desc",
    limit: int = 20,
    after: Optional[str] = None,
    before: Optional[str] = None,
) -> List[Collection]:
    """
    List collections.

    :param order: The order of the collections. It can be "asc" or "desc".
    :param limit: The maximum number of collections to return.
    :param after: The cursor to get the next page of collections.
    :param before: The cursor to get the previous page of collections.
    :return: The list of collections.
    """

    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    # only add non-None parameters
    payload = CollectionListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: CollectionListResponse = api_list_collections(payload=payload)
    return response.data


async def a_list_collections(
    *,
    order: str = "desc",
    limit: int = 20,
    after: Optional[str] = None,
    before: Optional[str] = None,
) -> List[Collection]:
    """
    List collections.

    :param order: The order of the collections. It can be "asc" or "desc".
    :param limit: The maximum number of collections to return.
    :param after: The cursor to get the next page of collections.
    :param before: The cursor to get the previous page of collections.
    :return: The list of collections.
    """

    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    # only add non-None parameters
    payload = CollectionListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: CollectionListResponse = await async_api_list_collections(payload=payload)
    return response.data


def get_collection(collection_id: str) -> Collection:
    """
    Get a collection.

    :param collection_id: The ID of the collection.
    """

    response: CollectionGetResponse = api_get_collection(collection_id=collection_id)
    return response.data


async def a_get_collection(collection_id: str) -> Collection:
    """
    Get a collection in async mode.

    :param collection_id: The ID of the collection.
    """

    response: CollectionGetResponse = await async_api_get_collection(collection_id=collection_id)
    return response.data


def create_collection(
    *,
    embedding_model_id: str,
    capacity: int = 1000,
    name: Optional[str] = None,
    type: Optional[CollectionType] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Collection:
    """
    Create a collection.

    :param embedding_model_id: The ID of an available embedding model in the project.
    :param capacity: The maximum number of embeddings that can be stored in the collection.
    :param name: The name of the collection.
    :param description: The description of the collection.
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created collection object.
    """

    body = CollectionCreateRequest(
        embedding_model_id=embedding_model_id,
        capacity=capacity,
        name=name or "",
        type=type or CollectionType.TEXT,
        description=description or "",
        metadata=metadata or {},
    )
    response: CollectionCreateResponse = api_create_collection(payload=body)
    return response.data


async def a_create_collection(
    *,
    embedding_model_id: str,
    capacity: int = 1000,
    name: Optional[str] = None,
    type: Optional[CollectionType] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Collection:
    """
    Create a collection in async mode.

    :param embedding_model_id: The ID of an available embedding model in the project.
    :param capacity: The maximum number of embeddings that can be stored in the collection.
    :param name: The name of the collection.
    :param description: The description of the collection.
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created collection object.
    """

    # todo verify parameters
    body = CollectionCreateRequest(
        embedding_model_id=embedding_model_id,
        capacity=capacity,
        name=name or "",
        type=type or CollectionType.TEXT,
        description=description or "",
        metadata=metadata or {},
    )
    response: CollectionCreateResponse = await async_api_create_collection(payload=body)
    return response.data


def update_collection(
    collection_id: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Collection:
    """
    Update a collection.

    :param collection_id: The ID of the collection.
    :param schema: The collection schema, which is compliant with the OpenAPI Specification. It should only have exactly one path and one method.
    :param authentication: The collection API authentication.
    :return: The updated collection object.
    """
    # todo: verify at least one parameter is not None
    body = CollectionUpdateRequest(
        name=name,
        description=description,
        metadata=metadata,
    )
    response: CollectionUpdateResponse = api_update_collection(collection_id=collection_id, payload=body)
    return response.data


async def a_update_collection(
    collection_id: str,
    *,
    name: Optional[str] = None,
    description: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Collection:
    """
    Update a collection in async mode.

    :param collection_id: The ID of the collection.
    :param schema: The collection schema, which is compliant with the OpenAPI Specification. It should only have exactly one path and one method.
    :param authentication: The collection API authentication.
    :return: The updated collection object.
    """
    body = CollectionUpdateRequest(
        name=name,
        description=description,
        metadata=metadata,
    )
    response: CollectionUpdateResponse = await async_api_update_collection(collection_id=collection_id, payload=body)
    return response.data


def delete_collection(collection_id: str) -> None:
    """
    Delete a collection.

    :param collection_id: The ID of the collection.
    """

    api_delete_collection(collection_id=collection_id)


async def a_delete_collection(collection_id: str) -> None:
    """
    Delete a collection in async mode.

    :param collection_id: The ID of the collection.
    """

    await async_api_delete_collection(collection_id=collection_id)
