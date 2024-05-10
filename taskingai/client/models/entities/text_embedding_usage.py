# -*- coding: utf-8 -*-

# text_embedding_usage.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field


__all__ = ["TextEmbeddingUsage"]


class TextEmbeddingUsage(BaseModel):
    input_tokens: int = Field(...)
