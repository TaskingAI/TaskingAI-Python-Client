from typing import Optional, Dict
from .._base import TaskingaiBaseModel
from enum import Enum

__all__ = ["Message", "MessageContent", "MessageRole", "MessageChunk"]


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"


class MessageContent(TaskingaiBaseModel):
    text: str


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
