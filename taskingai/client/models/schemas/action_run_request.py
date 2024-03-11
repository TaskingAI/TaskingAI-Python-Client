# -*- coding: utf-8 -*-

# action_run_request.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, Any, Dict


__all__ = ["ActionRunRequest"]


class ActionRunRequest(BaseModel):
    parameters: Optional[Dict[str, Any]] = Field(None)
