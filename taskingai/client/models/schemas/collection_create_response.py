# -*- coding: utf-8 -*-

# collection_create_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from ..entities.collection import Collection

__all__ = ["CollectionCreateResponse"]


class CollectionCreateResponse(BaseModel):
    status: str = Field("success")
    data: Collection = Field(...)
