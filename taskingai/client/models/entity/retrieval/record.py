from typing import Dict, Any
from .._base import TaskingaiBaseModel
from pydantic import Field

__all__ = [
    "Record",
]

class Record(TaskingaiBaseModel):
    object: str
    record_id: str
    collection_id: str
    type: str
    num_chunks: int
    content: Dict[str, Any]
    metadata: Dict[str, str]
    created_timestamp: int
    status: str
