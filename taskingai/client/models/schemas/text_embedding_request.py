# -*- coding: utf-8 -*-

# text_embedding_request.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Union
from ..entities.text_embedding_input_type import TextEmbeddingInputType

__all__ = ["TextEmbeddingRequest"]


class TextEmbeddingRequest(BaseModel):
    model_id: str = Field(..., min_length=1, max_length=255)
    input: Union[str, List[str]] = Field(...)
    input_type: Optional[TextEmbeddingInputType] = Field(None)
