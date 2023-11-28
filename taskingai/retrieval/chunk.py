from typing import Optional, List, Dict

from taskingai.client.utils import get_retrieval_api_instance
from taskingai.client.models import Chunk
from taskingai.client.models import ChunkQueryResponse, ChunkQueryRequest

__all__ = [
    "Chunk",
    "query_chunks",
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

    api_instance = get_retrieval_api_instance()
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
