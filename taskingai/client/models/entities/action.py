# -*- coding: utf-8 -*-

# action.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, Any, Dict
from .action_method import ActionMethod
from .action_param import ActionParam
from .action_param import ActionParam
from .action_body_type import ActionBodyType
from .action_param import ActionParam
from .chat_completion_function import ChatCompletionFunction
from .action_authentication import ActionAuthentication

__all__ = ["Action"]


class Action(BaseModel):
    action_id: str = Field(..., min_length=20, max_length=30)
    name: str = Field(..., min_length=1, max_length=128)
    operation_id: str = Field(...)
    description: str = Field(..., min_length=1, max_length=512)
    url: str = Field(...)
    method: ActionMethod = Field(...)
    body_type: ActionBodyType = Field(...)
    openapi_schema: Dict[str, Any] = Field(...)
    authentication: ActionAuthentication = Field(...)
    updated_timestamp: int = Field(..., ge=0)
    created_timestamp: int = Field(..., ge=0)
