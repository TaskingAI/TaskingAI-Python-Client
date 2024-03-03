# -*- coding: utf-8 -*-

# chat_memory_message.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional


__all__ = ["ChatMemoryMessage"]


class ChatMemoryMessage(BaseModel):
    role: str = Field(...)
    content: str = Field(...)
    token_count: Optional[int] = Field(None)
