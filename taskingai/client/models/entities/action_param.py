# -*- coding: utf-8 -*-

# action_param.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, List


__all__ = ["ActionParam"]


class ActionParam(BaseModel):
    type: str = Field(...)
    description: str = Field(...)
    enum: Optional[List[str]] = Field(None)
    required: bool = Field(...)
