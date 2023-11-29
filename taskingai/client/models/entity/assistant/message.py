from typing import Optional, Dict
from pydantic import Field, validator
from .._base import TaskingaiBaseModel
from enum import Enum

__all__ = [
    "Message",
    "MessageContent",
    "MessageRole",
    "ChatLog",
    "ChatLogType",
    "LogContent",
    "RetrievalLogContent",
    "ToolLogContent",
    "MessageGenerationResponseOption",
]

class MessageGenerationResponseOption(TaskingaiBaseModel):
    stream: bool
    debug: bool


class MessageRole(str, Enum):
    user = "user"
    assistant = "assistant"


class ChatLogType(str, Enum):
    retrieval = "retrieval"
    tool_call = "tool_call"
    tool_result = "tool_result"


class LogContent(TaskingaiBaseModel):
    pass


class RetrievalLogContent(LogContent):
    query: str
    result: str


class ToolLogContent(LogContent):
    tool_id: str
    type: str
    name: str
    input: str
    output: Optional[str]


class ChatLog(TaskingaiBaseModel):
    object: str
    type: ChatLogType
    session_id: str
    created_timestamp: int
    retrieval: Optional[RetrievalLogContent]
    tool: Optional[ToolLogContent]


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
