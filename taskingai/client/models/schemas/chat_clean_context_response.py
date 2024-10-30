# -*- coding: utf-8 -*-

# chat_completion_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from ..entities.message import Message

__all__ = ["ChatCleanContextResponse"]


class ChatCleanContextResponse(BaseModel):
    status: str = Field("success")
    data: Message = Field(...)
