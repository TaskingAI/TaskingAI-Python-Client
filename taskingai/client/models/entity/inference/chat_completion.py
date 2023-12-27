from typing import Dict, Optional, Any, List
from pydantic import Field
from .._base import TaskingaiBaseModel
from enum import Enum
from abc import ABCMeta
from typing_extensions import Literal

__all__ = [
    "ChatCompletion",
    "ChatCompletionMessage",
    "ChatCompletionSystemMessage",
    "ChatCompletionUserMessage",
    "ChatCompletionAssistantMessage",
    "ChatCompletionFunctionMessage",
    "ChatCompletionRole",
    "ChatCompletionFunctionCall",
    "ChatCompletionFunction",
    "ChatCompletionFinishReason",
    "ChatCompletionChunk",
    "INFERENCE_CHAT_COMPLETION_STREAM_CAST_MAP"
]


class ChatCompletionRole(str, Enum):
    system = "system"
    assistant = "assistant"
    user = "user"
    function = "function"


class ChatCompletionFunctionCall(TaskingaiBaseModel):
    id: str
    arguments: Dict[str, Any]
    name: str


class ChatCompletionFunction(TaskingaiBaseModel):
    name: str
    description: str
    parameters: Dict


class ChatCompletionMessage(TaskingaiBaseModel, metaclass=ABCMeta):
    content: Optional[str]


class ChatCompletionSystemMessage(ChatCompletionMessage):
    role: ChatCompletionRole = Field(Literal[ChatCompletionRole.system])


class ChatCompletionUserMessage(ChatCompletionMessage):
    role: ChatCompletionRole = Field(Literal[ChatCompletionRole.user])


class ChatCompletionAssistantMessage(ChatCompletionMessage):
    role: ChatCompletionRole = Field(Literal[ChatCompletionRole.assistant])
    function_calls: Optional[List[ChatCompletionFunctionCall]]


class ChatCompletionFunctionMessage(ChatCompletionMessage):
    role: ChatCompletionRole = Field(Literal[ChatCompletionRole.function])
    id: str


class ChatCompletionFinishReason(str, Enum):
    stop = "stop"
    length = "length"
    function_calls = "function_calls"
    recitation = "recitation"
    error = "error"
    unknown = "unknown"


class ChatCompletion(TaskingaiBaseModel):
    object: str = Field(Literal["ChatCompletion"])
    finish_reason: ChatCompletionFinishReason
    message: ChatCompletionAssistantMessage
    created_timestamp: int


class ChatCompletionChunk(TaskingaiBaseModel):
    object: str
    role: ChatCompletionRole
    index: int
    delta: str
    created_timestamp: int


INFERENCE_CHAT_COMPLETION_STREAM_CAST_MAP = {
    "ChatCompletion": ChatCompletion,
    "ChatCompletionChunk": ChatCompletionChunk
}
