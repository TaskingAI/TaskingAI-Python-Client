# -*- coding: utf-8 -*-

# message_update_request.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, Dict


__all__ = ["MessageUpdateRequest"]


class MessageUpdateRequest(BaseModel):
    metadata: Optional[Dict[str, str]] = Field(None)
