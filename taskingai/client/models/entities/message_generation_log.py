# -*- coding: utf-8 -*-

# message_generation_log.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Any, Dict


__all__ = ["MessageGenerationLog"]


class MessageGenerationLog(BaseModel):
    object: str = Field("MessageGenerationLog")
    session_id: str = Field(..., min_length=20, max_length=30)
    event: str = Field(...)
    event_id: str = Field(..., min_length=20, max_length=30)
    event_step: str = Field(...)
    timestamp: int = Field(..., ge=0)
    content: Dict[str, Any] = Field(...)
