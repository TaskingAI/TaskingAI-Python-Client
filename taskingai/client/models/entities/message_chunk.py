# -*- coding: utf-8 -*-

# message_chunk.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from .message_role import MessageRole

__all__ = ["MessageChunk"]


class MessageChunk(BaseModel):
    role: MessageRole = Field(...)
    index: int = Field(...)
    delta: str = Field(...)
    created_timestamp: int = Field(..., ge=0)
