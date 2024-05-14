# -*- coding: utf-8 -*-

# chunk.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict


__all__ = ["Chunk"]


class Chunk(BaseModel):
    object: str = Field("Chunk")
    chunk_id: str = Field(..., min_length=20, max_length=30)
    record_id: Optional[str] = Field(..., min_length=20, max_length=30)
    collection_id: str = Field(..., min_length=20, max_length=30)
    content: str = Field(..., min_length=1)
    num_tokens: int = Field(..., ge=0)
    metadata: Dict = Field({}, min_length=0, max_length=16)
    score: Optional[float] = Field(None, ge=0, le=1)
    updated_timestamp: int = Field(..., ge=0)
    created_timestamp: int = Field(..., ge=0)
