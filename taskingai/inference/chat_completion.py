from typing import Any, Optional, List, Dict, Union
from ..client.stream import Stream, AsyncStream

from taskingai.client.models import *
from taskingai.client.apis import *
from taskingai.client.stream_apis import *

__all__ = [
    "ChatCompletion",
    "ChatCompletionChunk",
    "ChatCompletionFunctionCall",
    "ChatCompletionFunction",
    "Function",
    "FunctionCall",
    "FunctionMessage",
    "AssistantMessage",
    "UserMessage",
    "SystemMessage",
    "chat_completion",
    "a_chat_completion",
]

Function = ChatCompletionFunction
FunctionCall = ChatCompletionFunctionCall


class SystemMessage(ChatCompletionSystemMessage):
    def __init__(self, content: str):
        super().__init__(role=ChatCompletionRole.SYSTEM, content=content)


class UserMessage(ChatCompletionUserMessage):
    def __init__(self, content: str):
        super().__init__(role=ChatCompletionRole.USER, content=content)


class AssistantMessage(ChatCompletionAssistantMessage):
    def __init__(self, content: str = None, function_calls: Optional[List[FunctionCall]] = None):
        super().__init__(role=ChatCompletionRole.ASSISTANT, content=content, function_calls=function_calls)


class FunctionMessage(ChatCompletionFunctionMessage):
    def __init__(self, id: str, content: str):
        super().__init__(role=ChatCompletionRole.FUNCTION, id=id, content=content)


def _get_completion_dict_params(
    messages: List[Union[SystemMessage, UserMessage, AssistantMessage, FunctionMessage, Dict[str, Any]]],
    functions: Optional[List[Union[Function, Dict[str, Any]]]] = None,
):
    def _build_message(message: Union[SystemMessage, UserMessage, AssistantMessage, FunctionMessage, Dict[str, Any]]):
        if isinstance(message, Dict):
            if message["role"] == ChatCompletionRole.SYSTEM.value:
                return SystemMessage(**message)
            if message["role"] == ChatCompletionRole.USER.value:
                return UserMessage(**message)
            if message["role"] == ChatCompletionRole.ASSISTANT.value:
                return AssistantMessage(**message)
            if message["role"] == ChatCompletionRole.FUNCTION.value:
                return FunctionMessage(**message)
        return message

    messages = [_build_message(message) for message in messages]
    functions = [
        function if isinstance(function, Function) else Function(**function) for function in (functions or [])
    ] or None
    return messages, functions


def chat_completion(
    model_id: str,
    messages: List[Union[SystemMessage, UserMessage, AssistantMessage, FunctionMessage, Dict[str, Any]]],
    configs: Optional[Dict] = None,
    function_call: Optional[str] = None,
    functions: Optional[List[Union[Function, Dict[str, Any]]]] = None,
    stream: bool = False,
) -> Union[ChatCompletion, Stream]:
    """
    Chat completion model inference.

    :param model_id: The ID of the model.
    :param messages: The list of messages.
    :param configs: The configurations.
    :param function_call: The function call.
    :param functions: The list of functions.
    :param stream: Whether to request in stream mode.
    :return: The list of assistants.
    """

    messages, functions = _get_completion_dict_params(messages, functions)

    # only add non-None parameters
    body = ChatCompletionRequest(
        model_id=model_id,
        messages=messages,
        configs=configs,
        function_call=function_call,
        functions=functions,
        stream=stream,
    )
    if not stream:
        response: ChatCompletionResponse = api_chat_completion(payload=body)
        return response.data
    else:
        response: Stream = stream_api_chat_completion(payload=body, stream=True)
        return response


async def a_chat_completion(
    model_id: str,
    messages: List[Union[SystemMessage, UserMessage, AssistantMessage, FunctionMessage, Dict[str, Any]]],
    configs: Optional[Dict] = None,
    function_call: Optional[str] = None,
    functions: Optional[List[Union[Function, Dict[str, Any]]]] = None,
    stream: bool = False,
) -> Union[ChatCompletion, AsyncStream]:
    """
    Chat completion model inference in async mode.

    :param model_id: The ID of the model.
    :param messages: The list of messages.
    :param configs: The configurations.
    :param function_call: The function call.
    :param functions: The list of functions.
    :param stream: Whether to request in stream mode.
    :return: The list of assistants.
    """

    messages, functions = _get_completion_dict_params(messages, functions)

    # only add non-None parameters
    body = ChatCompletionRequest(
        model_id=model_id,
        messages=messages,
        configs=configs,
        function_call=function_call,
        functions=functions,
        stream=stream,
    )
    if not stream:
        response: ChatCompletionResponse = await async_api_chat_completion(payload=body)
        return response.data
    else:
        response: AsyncStream = await async_stream_api_chat_completion(payload=body, stream=True)
        return response
