# -*- coding: utf-8 -*-

# action_run_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Dict


__all__ = ["ActionRunResponse"]


class ActionRunResponse(BaseModel):
    status: str = Field("success")
    data: Dict = Field(...)
