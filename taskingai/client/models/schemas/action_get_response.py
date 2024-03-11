# -*- coding: utf-8 -*-

# action_get_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from ..entities.action import Action

__all__ = ["ActionGetResponse"]


class ActionGetResponse(BaseModel):
    status: str = Field("success")
    data: Action = Field(...)
