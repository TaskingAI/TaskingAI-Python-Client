from typing import Optional, Dict
from pydantic import Field, validator
from .._base import TaskingaiBaseModel
from enum import Enum

__all__ = [
    "Message",
    "MessageContent",
    "MessageRole",
    "MessageGenerationLog",
    "MessageGenerationLogType",
    "MessageLogContent",
    "MessageRetrievalLogContent",
    "MessageToolLogContent",
    "MessageGenerationResponseOption",
    "MessageChunk"
]


class MessageGenerationResponseOption(TaskingaiBaseModel):
    stream: bool
    debug: bool


class MessageRole(str, Enum):
    user = "user"
    assistant = "assistant"


class MessageGenerationLogType(str, Enum):
    retrieval = "retrieval"
    tool_call = "tool_call"
    tool_result = "tool_result"


class MessageLogContent(TaskingaiBaseModel):
    pass


class MessageRetrievalLogContent(MessageLogContent):
    query: str
    result: str


class MessageToolLogContent(MessageLogContent):
    tool_id: str
    type: str
    name: str
    input: str
    output: Optional[str]


class MessageGenerationLog(TaskingaiBaseModel):
    object: str
    type: MessageGenerationLogType
    session_id: str
    created_timestamp: int
    retrieval: Optional[MessageRetrievalLogContent]
    tool: Optional[MessageToolLogContent]


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
