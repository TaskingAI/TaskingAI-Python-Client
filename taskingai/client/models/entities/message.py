# -*- coding: utf-8 -*-

# message.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Dict
from .message_content import MessageContent

__all__ = ["Message"]


class Message(BaseModel):
    message_id: str = Field(..., min_length=20, max_length=30)
    chat_id: str = Field(..., min_length=20, max_length=30)
    assistant_id: str = Field(None, min_length=20, max_length=30)
    role: str = Field(..., min_length=1, max_length=20)
    content: MessageContent = Field(...)
    metadata: Dict[str, str] = Field({}, min_length=0, max_length=16)
    updated_timestamp: int = Field(..., ge=0)
    created_timestamp: int = Field(..., ge=0)
