from typing import Dict
from .._base import TaskingaiBaseModel

__all__ = [
    "Chat",
]

class Chat(TaskingaiBaseModel):
    object: str
    chat_id: str
    assistant_id: str
    metadata: Dict[str, str]
    created_timestamp: int
