from typing import Optional, List, Dict

from taskingai.client.utils import get_api_instance, ModuleType
from taskingai.client.models import Chunk
from taskingai.client.models import ChunkQueryResponse, ChunkQueryRequest

__all__ = [
    "Chunk",
    "query_chunks",
    "a_query_chunks",
]


def query_chunks(
        collection_id: str,
        query_text: str,
        top_k: int = 3,
) -> List[Chunk]:
    """
    List records.
    :param collection_id: The ID of the collection.
    :param query_text: The query text.
    :param top_k: The number of most relevant chunks to return.
    """

    api_instance = get_api_instance(ModuleType.RETRIEVAL)
    # only add non-None parameters
    body = ChunkQueryRequest(
        top_k=top_k,
        query_text=query_text,
    )
    response: ChunkQueryResponse = api_instance.query_chunks(
        collection_id=collection_id,
        body=body,
    )
    chunks: List[Chunk] = [Chunk(**item) for item in response.data]
    return chunks


async def a_query_chunks(
        collection_id: str,
        query_text: str,
        top_k: int = 3,
) -> List[Chunk]:
    """
    List records in async mode.
    :param collection_id: The ID of the collection.
    :param query_text: The query text.
    :param top_k: The number of most relevant chunks to return.
    """

    api_instance = get_api_instance(ModuleType.RETRIEVAL, async_client=True)
    # only add non-None parameters
    body = ChunkQueryRequest(
        top_k=top_k,
        query_text=query_text,
    )
    response: ChunkQueryResponse = await api_instance.query_chunks(
        collection_id=collection_id,
        body=body,
    )
    chunks: List[Chunk] = [Chunk(**item) for item in response.data]
    return chunks