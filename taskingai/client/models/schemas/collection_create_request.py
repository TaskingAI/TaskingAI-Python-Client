# -*- coding: utf-8 -*-

# collection_create_request.py

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


__all__ = ["CollectionCreateRequest"]


class CollectionCreateRequest(BaseModel):
    name: str = Field("")
    description: str = Field("")
    capacity: int = Field(1000)
    embedding_model_id: str = Field(...)
    metadata: Dict[str, str] = Field({})
