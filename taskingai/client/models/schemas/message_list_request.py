# -*- coding: utf-8 -*-

# message_list_request.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional
from ..entities.sort_order_enum import SortOrderEnum

__all__ = ["MessageListRequest"]


class MessageListRequest(BaseModel):
    limit: int = Field(20)
    order: Optional[SortOrderEnum] = Field(None)
    after: Optional[str] = Field(None)
    before: Optional[str] = Field(None)
