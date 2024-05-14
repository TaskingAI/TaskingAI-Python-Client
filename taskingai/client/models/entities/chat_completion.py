# -*- coding: utf-8 -*-

# chat_completion.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from .chat_completion_finish_reason import ChatCompletionFinishReason
from .chat_completion_assistant_message import ChatCompletionAssistantMessage
from .chat_completion_usage import ChatCompletionUsage

__all__ = ["ChatCompletion"]


class ChatCompletion(BaseModel):
    object: str = Field("ChatCompletion")
    finish_reason: ChatCompletionFinishReason = Field(...)
    message: ChatCompletionAssistantMessage = Field(...)
    created_timestamp: int = Field(...)
    usage: ChatCompletionUsage = Field(...)
