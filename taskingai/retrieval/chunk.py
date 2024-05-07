from typing import List, Optional, Dict

from taskingai.client.models import *
from taskingai.client.apis import *

__all__ = [
    "Chunk",
    "list_chunks",
    "a_list_chunks",
    "get_chunk",
    "a_get_chunk",
    "create_chunk",
    "a_create_chunk",
    "update_chunk",
    "a_update_chunk",
    "delete_chunk",
    "a_delete_chunk",
    "query_chunks",
    "a_query_chunks",
]


def list_chunks(
    collection_id: str,
    *,
    order: str = "desc",
    limit: int = 20,
    after: Optional[str] = None,
    before: Optional[str] = None,
) -> List[Chunk]:
    """
    List chunks.

    :param collection_id: The ID of the collection.
    :param order: The order of the chunks. It can be "asc" or "desc".
    :param limit: The maximum number of assistants to return.
    :param after: The cursor to get the next page of chunks.
    :param before: The cursor to get the previous page of chunks.
    :return: The list of chunks.
    """

    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    # only add non-None parameters
    payload = ChunkListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: ChunkListResponse = api_list_chunks(collection_id=collection_id, payload=payload)
    return response.data


async def a_list_chunks(
    collection_id: str,
    *,
    order: str = "desc",
    limit: int = 20,
    after: Optional[str] = None,
    before: Optional[str] = None,
) -> List[Chunk]:
    """
    List chunks in async mode.
    :param collection_id: The ID of the collection.
    :param order: The order of the chunks. It can be "asc" or "desc".
    :param limit: The maximum number of chunks to return.
    :param after: The cursor to get the next page of chunks.
    :param before: The cursor to get the previous page of chunks.
    :return: The list of chunks.
    """

    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    # only add non-None parameters
    payload = ChunkListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: ChunkListResponse = await async_api_list_chunks(collection_id=collection_id, payload=payload)
    return response.data


def get_chunk(collection_id: str, chunk_id: str) -> Chunk:
    """
    Get a chunk.

    :param collection_id: The ID of the collection.
    :param chunk_id: The ID of the chunk.
    """

    response: ChunkGetResponse = api_get_chunk(
        collection_id=collection_id,
        chunk_id=chunk_id,
    )
    return response.data


async def a_get_chunk(collection_id: str, chunk_id: str) -> Chunk:
    """
    Get a chunk in async mode.

    :param collection_id: The ID of the collection.
    :param chunk_id: The ID of the chunk.
    """

    response: ChunkGetResponse = await async_api_get_chunk(
        collection_id=collection_id,
        chunk_id=chunk_id,
    )
    return response.data


def create_chunk(
    collection_id: str,
    *,
    content: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Chunk:
    """
    Create a chunk.

    :param collection_id: The ID of the collection.
    :param content: The content of the chunk.
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created chunk object.
    """

    body = ChunkCreateRequest(
        content=content,
        metadata=metadata or {},
    )
    response: ChunkCreateResponse = api_create_chunk(collection_id=collection_id, payload=body)
    return response.data


async def a_create_chunk(
    collection_id: str,
    *,
    content: str,
    metadata: Optional[Dict[str, str]] = None,
) -> Chunk:
    """
    Create a chunk in async mode.

    :param collection_id: The ID of the collection.
    :param content: The content of the chunk.
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created chunk object.
    """

    body = ChunkCreateRequest(
        content=content,
        metadata=metadata or {},
    )
    response: ChunkCreateResponse = await async_api_create_chunk(collection_id=collection_id, payload=body)
    return response.data


def update_chunk(
    collection_id: str,
    chunk_id: str,
    *,
    content: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Chunk:
    """
    Update a chunk.

    :param collection_id: The ID of the collection.
    :param chunk_id: The ID of the chunk.
    :param content: The content of the chunk.
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less
    than 64 and value's length is less than 512.
    :return: The collection object.
    """

    body = ChunkUpdateRequest(
        content=content,
        metadata=metadata,
    )
    response: ChunkUpdateResponse = api_update_chunk(collection_id=collection_id, chunk_id=chunk_id, payload=body)
    return response.data


async def a_update_chunk(
    collection_id: str,
    chunk_id: str,
    *,
    content: Optional[str] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Chunk:
    """
    Update a chunk in async mode.

    :param collection_id: The ID of the collection.
    :param chunk_id: The ID of the chunk.
    :param content: The content of the chunk.
    :param metadata: The collection metadata. It can store up to 16 key-value pairs where each key's length is less
    than 64 and value's length is less than 512.
    :return: The collection object.
    """

    body = ChunkUpdateRequest(
        content=content,
        metadata=metadata,
    )
    response: ChunkUpdateResponse = await async_api_update_chunk(
        collection_id=collection_id, chunk_id=chunk_id, payload=body
    )
    return response.data


def delete_chunk(
    collection_id: str,
    chunk_id: str,
) -> None:
    """
    Delete a chunk.

    :param collection_id: The ID of the collection.
    :param chunk_id: The ID of the chunk.
    """

    api_delete_chunk(collection_id=collection_id, chunk_id=chunk_id)


async def a_delete_chunk(
    collection_id: str,
    chunk_id: str,
) -> None:
    """
    Delete a chunk in async mode.

    :param collection_id: The ID of the collection.
    :param chunk_id: The ID of the chunk.
    """

    await async_api_delete_chunk(collection_id=collection_id, chunk_id=chunk_id)


def query_chunks(
    collection_id: str,
    *,
    query_text: str,
    top_k: int = 3,
    score_threshold: Optional[float] = None,
    max_tokens: Optional[int] = None,
) -> List[Chunk]:
    """
    Query chunks in a collection.
    :param collection_id: The ID of the collection.
    :param query_text: The query text.
    :param top_k: The number of most relevant chunks to return.
    :param max_tokens: The maximum number of tokens to return.
    """

    # only add non-None parameters
    body = ChunkQueryRequest(
        top_k=top_k,
        query_text=query_text,
        score_threshold=score_threshold,
        max_tokens=max_tokens,
    )
    response: ChunkQueryResponse = api_query_collection_chunks(
        collection_id=collection_id,
        payload=body,
    )
    return response.data


async def a_query_chunks(
    collection_id: str,
    *,
    query_text: str,
    top_k: int = 3,
    score_threshold: Optional[float] = None,
    max_tokens: Optional[int] = None,
) -> List[Chunk]:
    """
    Query chunks in a collection.
    :param collection_id: The ID of the collection.
    :param query_text: The query text.
    :param top_k: The number of most relevant chunks to return.
    :param max_tokens: The maximum number of tokens to return.
    """

    # only add non-None parameters
    body = ChunkQueryRequest(
        top_k=top_k,
        query_text=query_text,
        score_threshold=score_threshold,
        max_tokens=max_tokens,
    )
    response: ChunkQueryResponse = await async_api_query_collection_chunks(
        collection_id=collection_id,
        payload=body,
    )
    return response.data
