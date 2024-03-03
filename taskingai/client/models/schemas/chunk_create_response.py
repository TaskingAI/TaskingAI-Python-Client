# -*- coding: utf-8 -*-

# chunk_create_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from ..entities.chunk import Chunk

__all__ = ["ChunkCreateResponse"]


class ChunkCreateResponse(BaseModel):
    status: str = Field("success")
    data: Chunk = Field(...)
