# -*- coding: utf-8 -*-

# chat_completion_function_parameters_property.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, List


__all__ = ["ChatCompletionFunctionParametersProperty"]


class ChatCompletionFunctionParametersProperty(BaseModel):
    type: str = Field(..., pattern="^(string|number|integer|boolean)$")
    description: str = Field("", max_length=256)
    enum: Optional[List[str]] = Field(None)
