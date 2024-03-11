# -*- coding: utf-8 -*-

# chunk_list_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import List
from ..entities.chunk import Chunk

__all__ = ["ChunkListResponse"]


class ChunkListResponse(BaseModel):
    status: str = Field("success")
    data: List[Chunk] = Field(...)
    fetched_count: int = Field(...)
    has_more: bool = Field(...)
