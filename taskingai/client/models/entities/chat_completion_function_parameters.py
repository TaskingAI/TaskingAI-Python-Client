# -*- coding: utf-8 -*-

# chat_completion_function_parameters.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import List, Dict
from .chat_completion_function_parameters_property import ChatCompletionFunctionParametersProperty

__all__ = ["ChatCompletionFunctionParameters"]


class ChatCompletionFunctionParameters(BaseModel):
    type: str = Field("object")
    properties: Dict[str, ChatCompletionFunctionParametersProperty] = Field(...)
    required: List[str] = Field([])
