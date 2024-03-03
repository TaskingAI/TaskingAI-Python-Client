# -*- coding: utf-8 -*-

# chunk_update_request.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict


__all__ = ["ChunkUpdateRequest"]


class ChunkUpdateRequest(BaseModel):
    content: Optional[str] = Field(None)
    metadata: Optional[Dict] = Field(None)
