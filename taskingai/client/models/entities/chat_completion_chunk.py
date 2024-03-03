# -*- coding: utf-8 -*-

# chat_completion_chunk.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from .chat_completion_role import ChatCompletionRole

__all__ = ["ChatCompletionChunk"]


class ChatCompletionChunk(BaseModel):
    role: ChatCompletionRole = Field("assistant")
    index: int = Field(...)
    delta: str = Field(...)
    created_timestamp: int = Field(...)
