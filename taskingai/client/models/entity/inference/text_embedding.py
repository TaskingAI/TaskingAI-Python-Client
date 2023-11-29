# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0
"""


from typing import List
from .._base import TaskingaiBaseModel

__all__ = [
    "TextEmbeddingOutput",
]

class TextEmbeddingOutput(TaskingaiBaseModel):

    index: int
    embedding: List[float]

    def to_dict(self):
        """Returns the model properties as a dict"""
        return self.model_dump()

    def to_str(self):
        """Returns the string representation of the model"""
        return self.model_dump_json()

