# -*- coding: utf-8 -*-

# chunk_update_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from ..entities.chunk import Chunk

__all__ = ["ChunkUpdateResponse"]


class ChunkUpdateResponse(BaseModel):
    status: str = Field("success")
    data: Chunk = Field(...)
