# -*- coding: utf-8 -*-

# chat_list_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import List
from ..entities.chat import Chat

__all__ = ["ChatListResponse"]


class ChatListResponse(BaseModel):
    status: str = Field("success")
    data: List[Chat] = Field(...)
    fetched_count: int = Field(...)
    has_more: bool = Field(...)
