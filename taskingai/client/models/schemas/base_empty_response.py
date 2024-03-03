# -*- coding: utf-8 -*-

# base_empty_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field


__all__ = ["BaseEmptyResponse"]


class BaseEmptyResponse(BaseModel):
    status: str = Field("success")
