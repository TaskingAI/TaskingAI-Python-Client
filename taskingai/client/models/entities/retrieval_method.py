# -*- coding: utf-8 -*-

# retrieval_method.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from enum import Enum

__all__ = ["RetrievalMethod"]


class RetrievalMethod(str, Enum):
    FUNCTION_CALL = "function_call"
    USER_MESSAGE = "user_message"
    MEMORY = "memory"
