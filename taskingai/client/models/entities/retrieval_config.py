# -*- coding: utf-8 -*-

# retrieval_config.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional
from .retrieval_method import RetrievalMethod

__all__ = ["RetrievalConfig"]


class RetrievalConfig(BaseModel):
    top_k: int = Field(3, ge=1, le=20)
    max_tokens: Optional[int] = Field(None, ge=1, le=8192)
    method: RetrievalMethod = Field(...)
    function_description: Optional[str] = Field(None)
