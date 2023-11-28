from typing import Optional, List, Dict, Union

from taskingai.client.utils import get_inference_api_instance
from taskingai.client.models import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatCompletion,
    ChatCompletionFunctionMessage,
    ChatCompletionAssistantMessage,
    ChatCompletionUserMessage,
    ChatCompletionSystemMessage,
    ChatCompletionFunctionCall as FunctionCall,
    ChatCompletionFunction as Function,
    ChatCompletionRole,
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


class SystemMessage(ChatCompletionSystemMessage):
    def __init__(self, content: str):
        super().__init__(
            role=ChatCompletionRole.SYSTEM,
            content=content
        )


class UserMessage(ChatCompletionUserMessage):
    def __init__(self, content: str):
        super().__init__(
            role=ChatCompletionRole.USER,
            content=content
        )


class AssistantMessage(ChatCompletionAssistantMessage):
    def __init__(self, content: str = None, function_call: Optional[FunctionCall] = None):
        super().__init__(
            role=ChatCompletionRole.ASSISTANT,
            content=content,
            function_call=function_call
        )


class FunctionMessage(ChatCompletionFunctionMessage):
    def __init__(self, name: str, content: str):
        super().__init__(
            role=ChatCompletionRole.FUNCTION,
            name=name,
            content=content
        )


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
        configs=configs,
        function_call=function_call,
        functions=functions,
        stream=False
    )
    response: ChatCompletionResponse = api_instance.chat_completion(body=body)
    chat_completion_result: ChatCompletion = ChatCompletion(**response["data"])
    chat_completion_result.message = ChatCompletionAssistantMessage(**chat_completion_result.message)
    if chat_completion_result.message.function_call:
        chat_completion_result.message.function_call = FunctionCall(**chat_completion_result.message.function_call)
    return chat_completion_result


# todo: chat_completion_stream
