# -*- coding: utf-8 -*-

# collection.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from enum import Enum
from pydantic import BaseModel, Field
from typing import Dict


__all__ = ["Collection", "CollectionType"]


class CollectionType(str, Enum):
    TEXT = "text"
    QA = "qa"


class Collection(BaseModel):
    object: str = Field("Collection")
    type: CollectionType = Field(CollectionType.TEXT)
    collection_id: str = Field(..., min_length=24, max_length=24)
    name: str = Field("", min_length=0, max_length=256)
    description: str = Field("", min_length=0, max_length=512)
    avatar_url: str = Field("", min_length=0, max_length=1024, pattern=r"^(https://.+\.png)?$")
    capacity: int = Field(1000, ge=1)
    embedding_model_id: str = Field(..., min_length=8, max_length=8)
    metadata: Dict[str, str] = Field({}, min_length=0, max_length=16)
    updated_timestamp: int = Field(..., ge=0)
    created_timestamp: int = Field(..., ge=0)
    status: str = Field(...)
