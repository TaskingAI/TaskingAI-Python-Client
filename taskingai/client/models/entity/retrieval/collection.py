from typing import Dict
from .._base import TaskingaiBaseModel

__all__ = [
    "Collection",
]


class Collection(TaskingaiBaseModel):
    object: str
    collection_id: str
    name: str
    description: str
    capacity: int
    num_records: int
    num_chunks: int
    embedding_model_id: str
    metadata: Dict[str, str]
    created_timestamp: int
    status: str
