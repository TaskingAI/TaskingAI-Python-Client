# -*- coding: utf-8 -*-

# text_splitter.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, List
from .text_splitter_type import TextSplitterType

__all__ = ["TextSplitter"]


class TextSplitter(BaseModel):
    type: TextSplitterType = Field("token")
    chunk_size: Optional[int] = Field(None, ge=50, le=1000)
    chunk_overlap: Optional[int] = Field(None, ge=0, le=200)
    separators: Optional[List[str]] = Field(None, min_length=1, max_length=16)
