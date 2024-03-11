# -*- coding: utf-8 -*-

# assistant_update_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from ..entities.assistant import Assistant

__all__ = ["AssistantUpdateResponse"]


class AssistantUpdateResponse(BaseModel):
    status: str = Field("success")
    data: Assistant = Field(...)
