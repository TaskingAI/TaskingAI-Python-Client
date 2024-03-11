# -*- coding: utf-8 -*-

# chat_completion_function_call.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Any, Dict


__all__ = ["ChatCompletionFunctionCall"]


class ChatCompletionFunctionCall(BaseModel):
    id: str = Field(...)
    arguments: Dict[str, Any] = Field(...)
    name: str = Field(...)
