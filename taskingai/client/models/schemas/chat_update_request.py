# -*- coding: utf-8 -*-

# chat_update_request.py

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


__all__ = ["ChatUpdateRequest"]


class ChatUpdateRequest(BaseModel):
    metadata: Optional[Dict[str, str]] = Field(None)
