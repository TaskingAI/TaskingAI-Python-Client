# -*- coding: utf-8 -*-

# assistant_get_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from ..entities.assistant import Assistant

__all__ = ["AssistantGetResponse"]


class AssistantGetResponse(BaseModel):
    status: str = Field("success")
    data: Assistant = Field(...)
