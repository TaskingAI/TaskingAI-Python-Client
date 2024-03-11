# -*- coding: utf-8 -*-

# chunk_query_request.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional


__all__ = ["ChunkQueryRequest"]


class ChunkQueryRequest(BaseModel):
    top_k: int = Field(..., ge=1, le=20)
    max_tokens: Optional[int] = Field(None, ge=1)
    query_text: str = Field(..., min_length=1, max_length=32768)
