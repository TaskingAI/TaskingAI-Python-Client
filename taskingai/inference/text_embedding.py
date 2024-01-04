from typing import Optional, List, Dict, Union

from taskingai.client.utils import get_api_instance, ModuleType
from taskingai.client.models import (
    TextEmbeddingOutput,
    TextEmbeddingRequest,
    TextEmbeddingResponse
)

__all__ = [
    "TextEmbeddingOutput",
    "text_embedding",
    "a_text_embedding",
]


def text_embedding(
        model_id: str,
        input: Union[str, List[str]],
) -> Union[List[float] ,List[List[float]]]:
    """
    Chat completion model inference.

    :param model_id: The ID of the embedding model.
    :param input: The input text or list of input texts.
    :return: The list of assistants.
    """
    api_instance = get_api_instance(ModuleType.INFERENCE)
    # only add non-None parameters
    body = TextEmbeddingRequest(
        model_id=model_id,
        input=input
    )
    response: TextEmbeddingResponse = api_instance.text_embedding(body=body)
    results = []
    for data in response.data:
        text_embedding_result: TextEmbeddingOutput = TextEmbeddingOutput(**data)
        results.append(text_embedding_result.embedding)

    if isinstance(input, str):
        return results[0]
    else:
        return results


async def a_text_embedding(
        model_id: str,
        input: Union[str, List[str]],
) -> Union[List[float] ,List[List[float]]]:
    """
    Chat completion model inference in async mode.

    :param model_id: The ID of the embedding model.
    :param input: The input text or list of input texts.
    :return: The list of assistants.
    """
    api_instance = get_api_instance(ModuleType.INFERENCE, async_client=True)
    # only add non-None parameters
    body = TextEmbeddingRequest(
        model_id=model_id,
        input=input
    )
    response: TextEmbeddingResponse = await api_instance.text_embedding(body=body)
    results = []
    for data in response.data:
        text_embedding_result: TextEmbeddingOutput = TextEmbeddingOutput(**data)
        results.append(text_embedding_result.embedding)

    if isinstance(input, str):
        return results[0]
    else:
        return results
