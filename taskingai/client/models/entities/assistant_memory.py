# -*- coding: utf-8 -*-

# assistant_memory.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional
from .assistant_memory_type import AssistantMemoryType

__all__ = ["AssistantMemory"]


class AssistantMemory(BaseModel):
    type: AssistantMemoryType = Field(...)
    max_tokens: Optional[int] = Field(None, ge=0, le=8192)
