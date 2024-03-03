# -*- coding: utf-8 -*-

# text_embedding_output.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import List


__all__ = ["TextEmbeddingOutput"]


class TextEmbeddingOutput(BaseModel):
    index: int = Field(...)
    embedding: List[float] = Field(...)
