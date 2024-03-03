# -*- coding: utf-8 -*-

# chat_completion_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from ..entities.chat_completion import ChatCompletion

__all__ = ["ChatCompletionResponse"]


class ChatCompletionResponse(BaseModel):
    status: str = Field("success")
    data: ChatCompletion = Field(...)
