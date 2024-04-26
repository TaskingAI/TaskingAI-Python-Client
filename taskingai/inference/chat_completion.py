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


def _validate_chat_completion_params(
    messages: List[Union[SystemMessage, UserMessage, AssistantMessage, FunctionMessage, Dict[str, Any]]],
    functions: Optional[List[Union[Function, Dict[str, Any]]]] = None,
):
    """
    Get the completion dictionary parameters.

    :param messages: The list of messages. Each message can be a dictionary or an instance of a message class.
    :param functions: The list of functions.
    :return: The list of messages and functions.
    """

    def _validate_message(msg: Union[SystemMessage, UserMessage, AssistantMessage, FunctionMessage, Dict[str, Any]]):
        if isinstance(msg, Dict):
            if msg["role"] == ChatCompletionRole.SYSTEM.value:
                msg.pop("role")
                return SystemMessage(**msg)
            elif msg["role"] == ChatCompletionRole.USER.value:
                msg.pop("role")
                return UserMessage(**msg)
            elif msg["role"] == ChatCompletionRole.ASSISTANT.value:
                msg.pop("role")
                return AssistantMessage(**msg)
            elif msg["role"] == ChatCompletionRole.FUNCTION.value:
                msg.pop("role")
                return FunctionMessage(**msg)
            else:
                raise ValueError("Invalid message role.")

        elif (
            isinstance(msg, ChatCompletionSystemMessage)
            or isinstance(msg, ChatCompletionUserMessage)
            or isinstance(msg, ChatCompletionAssistantMessage)
            or isinstance(msg, ChatCompletionFunctionMessage)
        ):
            return msg

        raise ValueError("Invalid message type.")

    def _validate_function(func: Union[Function, Dict[str, Any]]):
        if isinstance(func, Dict):
            return Function(**func)
        elif isinstance(func, Function):
            return func
        raise ValueError("Invalid function type.")

    if not messages:
        raise ValueError("Messages cannot be empty.")
    messages = [_validate_message(msg) for msg in messages]
    if functions:
        functions = [_validate_function(func) for func in functions]
    return messages, functions


def chat_completion(
    model_id: str,
    *,
    messages: List[Union[SystemMessage, UserMessage, AssistantMessage, FunctionMessage, Dict[str, Any]]],
    configs: Optional[Dict] = None,
    function_call: Optional[str] = None,
    functions: Optional[List[Union[Function, Dict[str, Any]]]] = None,
    stream: bool = False,
) -> Union[ChatCompletion, Stream]:
    """
    Chat completion model inference.

    :param model_id: The ID of the model.
    :param messages: The list of messages. Each message can be a dictionary or an instance of a message class: SystemMessage, UserMessage, AssistantMessage, FunctionMessage.
    :param configs: The model configurations.
    :param function_call: Controls whether a specific function is invoked by the model. If set to 'none', the model will generate a message without calling a function. If set to 'auto', the model can choose between generating a message or calling a function. Defining a specific function using {'name': 'my_function'} instructs the model to call that particular function. By default, 'none' is selected when there are no chat_completion_functions available, and 'auto' is selected when one or more chat_completion_functions are present.
    :param functions: The list of functions.
    :param stream: Indicates whether the response should be streamed. If set to True, the response will be streamed using Server-Sent Events (SSE).
    :return: The list of assistants.
    """

    messages, functions = _validate_chat_completion_params(messages, functions)

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
    *,
    messages: List[Union[SystemMessage, UserMessage, AssistantMessage, FunctionMessage, Dict[str, Any]]],
    configs: Optional[Dict] = None,
    function_call: Optional[str] = None,
    functions: Optional[List[Union[Function, Dict[str, Any]]]] = None,
    stream: bool = False,
) -> Union[ChatCompletion, AsyncStream]:
    """
    Chat completion model inference in async mode.

    :param model_id: The ID of the model.
    :param messages: The list of messages. Each message can be a dictionary or an instance of a message class: SystemMessage, UserMessage, AssistantMessage, FunctionMessage.
    :param configs: The model configurations.
    :param function_call: Controls whether a specific function is invoked by the model. If set to 'none', the model will generate a message without calling a function. If set to 'auto', the model can choose between generating a message or calling a function. Defining a specific function using {'name': 'my_function'} instructs the model to call that particular function. By default, 'none' is selected when there are no chat_completion_functions available, and 'auto' is selected when one or more chat_completion_functions are present.
    :param functions: The list of functions.
    :param stream: Indicates whether the response should be streamed. If set to True, the response will be streamed using Server-Sent Events (SSE).
    :return: The list of assistants.
    """

    messages, functions = _validate_chat_completion_params(messages, functions)

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
