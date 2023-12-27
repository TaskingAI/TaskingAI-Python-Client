from typing import Optional, List, Dict, Union, Any
from ..client.stream import Stream, AsyncStream

from taskingai.client.utils import get_api_instance, ModuleType
from taskingai.client.models import (
    ChatCompletionRequest,
    ChatCompletionResponse,
    ChatCompletion,
    ChatCompletionChunk,
    ChatCompletionFunctionMessage,
    ChatCompletionAssistantMessage,
    ChatCompletionUserMessage,
    ChatCompletionSystemMessage,
    ChatCompletionFunctionCall as FunctionCall,
    ChatCompletionFunction as Function,
    ChatCompletionRole,
)

__all__ = [
    "ChatCompletion",
    "ChatCompletionChunk",
    "FunctionCall",
    "Function",
    "FunctionMessage",
    "AssistantMessage",
    "UserMessage",
    "SystemMessage",
    "chat_completion",
    "a_chat_completion",
]


class SystemMessage(ChatCompletionSystemMessage):
    def __init__(self, content: str):
        super().__init__(
            role=ChatCompletionRole.system,
            content=content
        )


class UserMessage(ChatCompletionUserMessage):
    def __init__(self, content: str):
        super().__init__(
            role=ChatCompletionRole.user,
            content=content
        )


class AssistantMessage(ChatCompletionAssistantMessage):
    def __init__(self, content: str = None, function_calls: Optional[List[FunctionCall]] = None):
        super().__init__(
            role=ChatCompletionRole.assistant,
            content=content,
            function_calls=function_calls
        )


class FunctionMessage(ChatCompletionFunctionMessage):
    def __init__(self, id: str, content: str):
        super().__init__(
            role=ChatCompletionRole.function,
            id=id,
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
        stream: bool = False
) -> Union[ChatCompletion, Stream]:
    """
    Chat completion model inference.

    :param model_id: The ID of the model.
    :param messages: The list of messages.
    :param configs: The configurations.
    :param function_call: The function call.
    :param functions: The list of functions.
    :return: The list of assistants.
    """
    api_instance = get_api_instance(ModuleType.inference)
    # only add non-None parameters
    body = ChatCompletionRequest(
        model_id=model_id,
        messages=messages,
        configs=configs,
        function_call=function_call,
        functions=functions,
        stream=stream
    )
    if not stream:
        response: ChatCompletionResponse = api_instance.chat_completion(body=body)
        chat_completion_result: ChatCompletion = ChatCompletion(**response["data"])
        return chat_completion_result
    else:
        response: Stream = api_instance.chat_completion(body=body, stream=True)
        return response


async def a_chat_completion(
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
        stream: bool = False
) -> Union[ChatCompletion, AsyncStream]:
    """
    Chat completion model inference in async mode.

    :param model_id: The ID of the model.
    :param messages: The list of messages.
    :param configs: The configurations.
    :param function_call: The function call.
    :param functions: The list of functions.
    :return: The list of assistants.
    """
    api_instance = get_api_instance(ModuleType.inference, async_client=True)
    # only add non-None parameters
    body = ChatCompletionRequest(
        model_id=model_id,
        messages=messages,
        configs=configs,
        function_call=function_call,
        functions=functions,
        stream=stream
    )
    if not stream:
        response: ChatCompletionResponse = await api_instance.chat_completion(body=body)
        chat_completion_result: ChatCompletion = ChatCompletion(**response["data"])
        return chat_completion_result
    else:
        response: AsyncStream = await api_instance.chat_completion(body=body, stream=True)
        return response




# todo: chat_completion_stream
