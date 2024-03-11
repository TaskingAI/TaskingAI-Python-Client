# -*- coding: utf-8 -*-

# chunk_create_request.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Dict


__all__ = ["ChunkCreateRequest"]


class ChunkCreateRequest(BaseModel):
    content: str = Field(...)
    metadata: Dict = Field({})
