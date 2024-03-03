# -*- coding: utf-8 -*-

# chat_memory.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from .assistant_memory_type import AssistantMemoryType
from .chat_memory_message import ChatMemoryMessage

__all__ = ["ChatMemory"]


class ChatMemory(BaseModel):
    type: AssistantMemoryType = Field(...)
    messages: List[ChatMemoryMessage] = Field([])
    max_messages: Optional[int] = Field(None, ge=1, le=1024)
    max_tokens: Optional[int] = Field(None, ge=1, le=8192)
