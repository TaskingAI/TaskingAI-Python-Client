# -*- coding: utf-8 -*-

# text_embedding_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import List
from ..entities.text_embedding_output import TextEmbeddingOutput
from ..entities.text_embedding_usage import TextEmbeddingUsage

__all__ = ["TextEmbeddingResponse"]


class TextEmbeddingResponse(BaseModel):
    status: str = Field("success")
    data: List[TextEmbeddingOutput] = Field(...)
    usage: TextEmbeddingUsage = Field(...)
