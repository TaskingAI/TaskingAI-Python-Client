# -*- coding: utf-8 -*-

# record_update_request.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict
from ..entities.record_type import RecordType
from ..entities.text_splitter import TextSplitter

__all__ = ["RecordUpdateRequest"]


class RecordUpdateRequest(BaseModel):
    type: Optional[RecordType] = Field(None)
    title: Optional[str] = Field(None, min_length=0, max_length=256)
    content: Optional[str] = Field(None, min_length=1, max_length=32768)
    text_splitter: Optional[TextSplitter] = Field(None)
    metadata: Optional[Dict[str, str]] = Field(None, min_length=0, max_length=16)
