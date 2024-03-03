# -*- coding: utf-8 -*-

# retrieval_ref.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from .retrieval_type import RetrievalType

__all__ = ["RetrievalRef"]


class RetrievalRef(BaseModel):
    type: RetrievalType = Field(...)
    id: str = Field(...)
