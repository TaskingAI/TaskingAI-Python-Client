# -*- coding: utf-8 -*-

# chat_completion_usage.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field


__all__ = ["ChatCompletionUsage"]


class ChatCompletionUsage(BaseModel):
    input_tokens: int = Field(...)
    output_tokens: int = Field(...)
