from typing import Optional, Dict
from pydantic import Field, validator
from .._base import TaskingaiBaseModel
from enum import Enum

__all__ = [
    "Message",
    "MessageContent",
    "MessageRole",
    "MessageGenerationLog",
    "MessageChunk"
]


class MessageRole(str, Enum):
    user = "user"
    assistant = "assistant"


class MessageGenerationLog(TaskingaiBaseModel):
    object: str
    type: str
    session_id: str
    created_timestamp: int
    content: Dict


class MessageContent(TaskingaiBaseModel):
    text: Optional[str]


class Message(TaskingaiBaseModel):
    object: str
    message_id: str
    chat_id: str
    assistant_id: Optional[str]
    role: MessageRole
    content: MessageContent
    metadata: Dict[str, str]
    created_timestamp: int


class MessageChunk(TaskingaiBaseModel):
    object: str
    role: MessageRole
    index: int
    delta: str
    created_timestamp: int
