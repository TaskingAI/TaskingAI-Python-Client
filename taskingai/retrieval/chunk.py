from typing import List, Optional

from taskingai.client.models import *
from taskingai.client.apis import *

__all__ = [
    "Chunk",
    "query_chunks",
    "a_query_chunks",
]


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
    :param score_threshold: The minimum score threshold to return.
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
    :param score_threshold: The minimum score threshold to return.
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
