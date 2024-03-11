# -*- coding: utf-8 -*-

# tool_ref.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from .tool_type import ToolType

__all__ = ["ToolRef"]


class ToolRef(BaseModel):
    type: ToolType = Field(...)
    id: str = Field(...)
