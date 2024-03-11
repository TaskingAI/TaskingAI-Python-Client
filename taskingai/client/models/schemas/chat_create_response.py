# -*- coding: utf-8 -*-

# chat_create_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from ..entities.chat import Chat

__all__ = ["ChatCreateResponse"]


class ChatCreateResponse(BaseModel):
    status: str = Field("success")
    data: Chat = Field(...)
