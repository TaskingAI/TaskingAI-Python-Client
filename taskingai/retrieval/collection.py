from typing import Optional, List, Dict, Any

from taskingai.client.utils import get_api_instance, ModuleType
from taskingai.client.models import Collection, CollectionConfig
from taskingai.client.models import CollectionCreateRequest, CollectionCreateResponse, \
    CollectionUpdateRequest, CollectionUpdateResponse, \
    CollectionGetResponse, CollectionListResponse

__all__ = [
    "Collection",
    "CollectionConfig",
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
        order: str = "desc",
        limit: int = 20,
        offset: Optional[int] = None,
        after: Optional[str] = None,
        before: Optional[str] = None,
) -> List[Collection]:
    """
    List collections.

    :param order: The order of the collections. It can be "asc" or "desc".
    :param limit: The maximum number of collections to return.
    :param offset: The offset of the collections.
    :param after: The cursor to get the next page of collections.
    :param before: The cursor to get the previous page of collections.
    :return: The list of collections.
    """
    offset_params = [offset, after, before]
    if sum([1 if param is not None else 0 for param in offset_params]) > 1:
        raise ValueError("Only one of offset, after and before can be specified.")

    api_instance = get_api_instance(ModuleType.retrieval)
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "offset": offset,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: CollectionListResponse = api_instance.list_collections(**params)
    collections: List[Collection] = [Collection(**item) for item in response.data]
    return collections


async def a_list_collections(
        order: str = "desc",
        limit: int = 20,
        offset: Optional[int] = None,
        after: Optional[str] = None,
        before: Optional[str] = None,
) -> List[Collection]:
    """
    List collections in async mode.

    :param order: The order of the collections. It can be "asc" or "desc".
    :param limit: The maximum number of collections to return.
    :param offset: The offset of the collections.
    :param after: The cursor to get the next page of collections.
    :param before: The cursor to get the previous page of collections.
    :return: The list of collections.
    """
    offset_params = [offset, after, before]
    if sum([1 if param is not None else 0 for param in offset_params]) > 1:
        raise ValueError("Only one of offset, after and before can be specified.")

    api_instance = get_api_instance(ModuleType.retrieval, async_client=True)
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "offset": offset,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: CollectionListResponse = await api_instance.list_collections(**params)
    collections: List[Collection] = [Collection(**item) for item in response.data]
    return collections


def get_collection(collection_id: str) -> Collection:
    """
    Get a collection.

    :param collection_id: The ID of the collection.
    """

    api_instance = get_api_instance(ModuleType.retrieval)
    response: CollectionGetResponse = api_instance.get_collection(collection_id=collection_id)
    collection: Collection = Collection(**response.data)
    return collection


async def a_get_collection(collection_id: str) -> Collection:
    """
    Get a collection in async mode.

    :param collection_id: The ID of the collection.
    """

    api_instance = get_api_instance(ModuleType.retrieval, async_client=True)
    response: CollectionGetResponse = await api_instance.get_collection(collection_id=collection_id)
    collection: Collection = Collection(**response.data)
    return collection


def create_collection(
        embedding_model_id: str,
        capacity: int = 1000,
        name: Optional[str] = None,
        description: Optional[str] = None,
        configs: Optional[CollectionConfig] = None,
        metadata: Optional[Dict[str, str]] = None,
) -> Collection:
    """
    Create a collection.

    :param embedding_model_id: The ID of an available embedding model in the project.
    :param capacity: The maximum number of embeddings that can be stored in the collection.
    :param name: The name of the collection.
    :param description: The description of the collection.
    :param configs: The collection configurations.
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created collection object.
    """

    # todo verify parameters
    api_instance = get_api_instance(ModuleType.retrieval)
    body = CollectionCreateRequest(
        embedding_model_id=embedding_model_id,
        capacity=capacity,
        name=name,
        description=description,
        configs=configs,
        metadata=metadata,
    )
    response: CollectionCreateResponse = api_instance.create_collection(body=body)
    collection: Collection = Collection(**response.data)
    return collection


async def a_create_collection(
        embedding_model_id: str,
        capacity: int = 1000,
        name: Optional[str] = None,
        description: Optional[str] = None,
        configs: Optional[CollectionConfig] = None,
        metadata: Optional[Dict[str, str]] = None,
) -> Collection:
    """
    Create a collection in async mode.

    :param embedding_model_id: The ID of an available embedding model in the project.
    :param capacity: The maximum number of embeddings that can be stored in the collection.
    :param name: The name of the collection.
    :param description: The description of the collection.
    :param configs: The collection configurations.
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created collection object.
    """

    # todo verify parameters
    api_instance = get_api_instance(ModuleType.retrieval, async_client=True)
    body = CollectionCreateRequest(
        embedding_model_id=embedding_model_id,
        capacity=capacity,
        name=name,
        description=description,
        configs=configs,
        metadata=metadata,
    )
    response: CollectionCreateResponse = await api_instance.create_collection(body=body)
    collection: Collection = Collection(**response.data)
    return collection


def update_collection(
        collection_id: str,
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
    #todo: verify at least one parameter is not None
    api_instance = get_api_instance(ModuleType.retrieval)
    body = CollectionUpdateRequest(
        name=name,
        description=description,
        metadata=metadata,
    )
    response: CollectionUpdateResponse = api_instance.update_collection(
        collection_id=collection_id,
        body=body
    )
    collection: Collection = Collection(**response.data)
    return collection


async def a_update_collection(
        collection_id: str,
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
    api_instance = get_api_instance(ModuleType.retrieval, async_client=True)
    body = CollectionUpdateRequest(
        name=name,
        description=description,
        metadata=metadata,
    )
    response: CollectionUpdateResponse = await api_instance.update_collection(
        collection_id=collection_id,
        body=body
    )
    collection: Collection = Collection(**response.data)
    return collection


def delete_collection(collection_id: str) -> None:
    """
    Delete a collection.

    :param collection_id: The ID of the collection.
    """

    api_instance = get_api_instance(ModuleType.retrieval)
    api_instance.delete_collection(collection_id=collection_id)


async def a_delete_collection(collection_id: str) -> None:
    """
    Delete a collection in async mode.

    :param collection_id: The ID of the collection.
    """

    api_instance = get_api_instance(ModuleType.retrieval, async_client=True)
    await api_instance.delete_collection(collection_id=collection_id)

