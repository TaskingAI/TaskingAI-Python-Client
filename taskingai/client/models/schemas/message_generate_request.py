# -*- coding: utf-8 -*-

# message_generate_request.py

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


__all__ = ["MessageGenerateRequest"]


class MessageGenerateRequest(BaseModel):
    system_prompt_variables: Dict[str, str] = Field({}, min_length=0, max_length=16)
    stream: bool = Field(False)
    debug: bool = Field(False)
