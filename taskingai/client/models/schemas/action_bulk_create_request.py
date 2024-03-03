# -*- coding: utf-8 -*-

# action_bulk_create_request.py

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
from ..entities.action_authentication import ActionAuthentication

__all__ = ["ActionBulkCreateRequest"]


class ActionBulkCreateRequest(BaseModel):
    openapi_schema: Dict = Field(...)
    authentication: ActionAuthentication = Field(...)
