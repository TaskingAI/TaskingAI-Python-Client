# -*- coding: utf-8 -*-

# chunk_query_response.py

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
from ..entities.chunk import Chunk

__all__ = ["ChunkQueryResponse"]


class ChunkQueryResponse(BaseModel):
    status: str = Field(...)
    data: List[Chunk] = Field(...)
    fetched_count: int = Field(..., ge=0)
