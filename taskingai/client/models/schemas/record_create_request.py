# -*- coding: utf-8 -*-

# record_create_request.py

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
from ..entities.record_type import RecordType
from ..entities.text_splitter import TextSplitter

__all__ = ["RecordCreateRequest"]


class RecordCreateRequest(BaseModel):
    type: RecordType = Field("text")
    title: str = Field("", min_length=0, max_length=256)
    content: str = Field(..., min_length=1, max_length=32768)
    text_splitter: TextSplitter = Field(...)
    metadata: Dict[str, str] = Field({}, min_length=0, max_length=16)
