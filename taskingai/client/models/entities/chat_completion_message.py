# -*- coding: utf-8 -*-

# chat_completion_message.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional


__all__ = ["ChatCompletionMessage"]


class ChatCompletionMessage(BaseModel):
    content: Optional[str] = Field(None)
