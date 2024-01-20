from .._base import TaskingaiBaseModel

__all__ = [
    "Chunk",
]


class Chunk(TaskingaiBaseModel):
    object: str
    chunk_id: str
    record_id: str
    collection_id: str
    content: str
    score: float
