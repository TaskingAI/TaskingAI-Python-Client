# -*- coding: utf-8 -*-

# base_data_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Any


__all__ = ["BaseDataResponse"]


class BaseDataResponse(BaseModel):
    status: str = Field("success")
    data: Any = Field(...)
