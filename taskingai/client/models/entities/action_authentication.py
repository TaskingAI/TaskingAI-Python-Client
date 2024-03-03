# -*- coding: utf-8 -*-

# action_authentication.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict
from .action_authentication_type import ActionAuthenticationType

__all__ = ["ActionAuthentication"]


class ActionAuthentication(BaseModel):
    type: ActionAuthenticationType = Field(...)
    secret: Optional[str] = Field(None, min_length=1, max_length=1024)
    content: Optional[Dict] = Field(None)
