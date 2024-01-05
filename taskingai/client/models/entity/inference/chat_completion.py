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
    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"
    FUNCTION = "function"


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
    role: ChatCompletionRole = Field(Literal[ChatCompletionRole.SYSTEM])


class ChatCompletionUserMessage(ChatCompletionMessage):
    role: ChatCompletionRole = Field(Literal[ChatCompletionRole.USER])


class ChatCompletionAssistantMessage(ChatCompletionMessage):
    role: ChatCompletionRole = Field(Literal[ChatCompletionRole.ASSISTANT])
    function_calls: Optional[List[ChatCompletionFunctionCall]]


class ChatCompletionFunctionMessage(ChatCompletionMessage):
    role: ChatCompletionRole = Field(Literal[ChatCompletionRole.FUNCTION])
    id: str


class ChatCompletionFinishReason(str, Enum):
    STOP = "stop"
    LENGTH = "length"
    FUNCTION_CALLS = "function_calls"
    RECITATION = "recitation"
    ERROR = "error"
    UNKNOWN = "unknown"


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
