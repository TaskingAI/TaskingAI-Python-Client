# -*- coding: utf-8 -*-

# record.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Dict
from .status import Status
from .record_type import RecordType

__all__ = ["Record"]


class Record(BaseModel):
    object: str = Field("Record")
    record_id: str = Field(..., min_length=20, max_length=30)
    collection_id: str = Field(..., min_length=20, max_length=30)
    title: str = Field("", min_length=0, max_length=255)
    status: Status = Field(...)
    num_chunks: int = Field(..., ge=0)
    type: RecordType = Field(...)
    content: str = Field(..., min_length=1, max_length=65535)
    metadata: Dict = Field({}, min_length=0, max_length=16)
    updated_timestamp: int = Field(..., ge=0)
    created_timestamp: int = Field(..., ge=0)
