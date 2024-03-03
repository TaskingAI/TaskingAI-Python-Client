# -*- coding: utf-8 -*-

# message_create_request.py

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
from ..entities.message_content import MessageContent

__all__ = ["MessageCreateRequest"]


class MessageCreateRequest(BaseModel):
    role: str = Field(...)
    content: MessageContent = Field(...)
    metadata: Dict[str, str] = Field({})
