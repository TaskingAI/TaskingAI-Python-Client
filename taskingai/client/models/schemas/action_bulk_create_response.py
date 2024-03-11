# -*- coding: utf-8 -*-

# action_bulk_create_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import List
from ..entities.action import Action

__all__ = ["ActionBulkCreateResponse"]


class ActionBulkCreateResponse(BaseModel):
    status: str = Field("success")
    data: List[Action] = Field(...)
