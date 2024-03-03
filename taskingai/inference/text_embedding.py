from typing import List, Union

from taskingai.client.models import *
from taskingai.client.apis import *

__all__ = [
    "TextEmbeddingOutput",
    "text_embedding",
    "a_text_embedding",
]


def text_embedding(
    model_id: str,
    input: Union[str, List[str]],
) -> Union[List[float], List[List[float]]]:
    """
    Chat completion model inference.

    :param model_id: The ID of the embedding model.
    :param input: The input text or list of input texts.
    :return: The list of assistants.
    """

    # only add non-None parameters
    body = TextEmbeddingRequest(model_id=model_id, input=input)
    response: TextEmbeddingResponse = api_text_embedding(payload=body)
    results = [data.embedding for data in response.data]

    if isinstance(input, str):
        return results[0]
    else:
        return results


async def a_text_embedding(
    model_id: str,
    input: Union[str, List[str]],
) -> Union[List[float], List[List[float]]]:
    """
    Chat completion model inference in async mode.

    :param model_id: The ID of the embedding model.
    :param input: The input text or list of input texts.
    :return: The list of assistants.
    """

    # only add non-None parameters
    body = TextEmbeddingRequest(model_id=model_id, input=input)
    response: TextEmbeddingResponse = await async_api_text_embedding(payload=body)
    results = [data.embedding for data in response.data]

    if isinstance(input, str):
        return results[0]
    else:
        return results
