# -*- coding: utf-8 -*-

# collection_update_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from ..entities.collection import Collection

__all__ = ["CollectionUpdateResponse"]


class CollectionUpdateResponse(BaseModel):
    status: str = Field("success")
    data: Collection = Field(...)
