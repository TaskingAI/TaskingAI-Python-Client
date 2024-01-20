from typing import Dict
from .._base import TaskingaiBaseModel

__all__ = [
    "Record",
]


class Record(TaskingaiBaseModel):
    object: str
    record_id: str
    collection_id: str
    type: str
    num_chunks: int
    content: str
    metadata: Dict[str, str]
    created_timestamp: int
    status: str
