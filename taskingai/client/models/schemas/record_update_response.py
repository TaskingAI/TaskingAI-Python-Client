# -*- coding: utf-8 -*-

# record_update_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from ..entities.record import Record

__all__ = ["RecordUpdateResponse"]


class RecordUpdateResponse(BaseModel):
    status: str = Field("success")
    data: Record = Field(...)
