from typing import Dict, Optional
from pydantic import Field
from .._base import TaskingaiBaseModel

__all__ = [
    "CollectionConfig",
    "Collection",
]

class CollectionConfig(TaskingaiBaseModel):
    chunk_size: int = Field(200, ge=100, le=500)
    chunk_overlap: int = Field(0, ge=0, le=100)
    metric: str = Field("cosine")


class Collection(TaskingaiBaseModel):
    object: str
    collection_id: str
    name: str
    description: str
    capacity: int
    num_records: int
    num_chunks: int
    configs: CollectionConfig
    embedding_model_id: str
    metadata: Dict[str, str]
    created_timestamp: int
    status: str
