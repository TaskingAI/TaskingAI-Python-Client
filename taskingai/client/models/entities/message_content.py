# -*- coding: utf-8 -*-

# message_content.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field


__all__ = ["MessageContent"]


class MessageContent(BaseModel):
    text: str = Field(...)
