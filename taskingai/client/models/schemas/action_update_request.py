# -*- coding: utf-8 -*-

# action_update_request.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, Any, Dict
from ..entities.action_authentication import ActionAuthentication

__all__ = ["ActionUpdateRequest"]


class ActionUpdateRequest(BaseModel):
    openapi_schema: Optional[Dict[str, Any]] = Field(None)
    authentication: Optional[ActionAuthentication] = Field(None)
