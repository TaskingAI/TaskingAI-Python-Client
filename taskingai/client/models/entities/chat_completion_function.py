# -*- coding: utf-8 -*-

# chat_completion_function.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from .chat_completion_function_parameters import ChatCompletionFunctionParameters

__all__ = ["ChatCompletionFunction"]


class ChatCompletionFunction(BaseModel):
    name: str = Field(...)
    description: str = Field(...)
    parameters: ChatCompletionFunctionParameters = Field(...)
