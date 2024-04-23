# -*- coding: utf-8 -*-

# chat_create_request.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Dict


__all__ = ["ChatCreateRequest"]


class ChatCreateRequest(BaseModel):
    name: str = Field("")
    metadata: Dict[str, str] = Field({})
