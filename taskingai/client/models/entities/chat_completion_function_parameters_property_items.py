# -*- coding: utf-8 -*-

# chat_completion_function_parameters_property_items.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field


__all__ = ["ChatCompletionFunctionParametersPropertyItems"]


class ChatCompletionFunctionParametersPropertyItems(BaseModel):
    type: str = Field(..., pattern="^(string|number|integer|boolean)$")
