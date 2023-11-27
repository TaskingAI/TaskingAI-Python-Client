from typing import Optional, List, Dict, Union

from taskingai.client.utils import get_inference_api_instance
from taskingai.client.models import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatCompletion,
    ChatCompletionFunctionMessage as FunctionMessage,
    ChatCompletionAssistantMessage as AssistantMessage,
    ChatCompletionUserMessage as UserMessage,
    ChatCompletionSystemMessage as SystemMessage,
    ChatCompletionFunctionCall as FunctionCall,
    ChatCompletionFunction as Function,
)

__all__ = [
    "chat_completion",
    "ChatCompletion",
    "FunctionCall",
    "Function",
    "FunctionMessage",
    "AssistantMessage",
    "UserMessage",
    "SystemMessage",
]


def chat_completion(
        model_id: str,
        messages: List[Union[
            SystemMessage,
            UserMessage,
            AssistantMessage,
            FunctionMessage
        ]],
        configs: Optional[Dict] = None,
        function_call: Optional[str] = None,
        functions: Optional[List[Function]] = None,
) -> ChatCompletion:
    """
    Chat completion model inference.

    :param model_id: The ID of the model.
    :param messages: The list of messages.
    :param configs: The configurations.
    :param function_call: The function call.
    :param functions: The list of functions.
    :return: The list of assistants.
    """
    api_instance = get_inference_api_instance()
    # only add non-None parameters
    body = ChatCompletionRequest(
        model_id=model_id,
        messages=messages,
        configs=configs
    )
    response: ChatCompletionResponse = api_instance.chat_completion(body=body)
    chat_completion_result: ChatCompletion = ChatCompletion(**response.data)
    return chat_completion_result


# todo: chat_completion_stream
