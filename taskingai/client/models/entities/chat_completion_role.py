# -*- coding: utf-8 -*-

# chat_completion_role.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from enum import Enum

__all__ = ["ChatCompletionRole"]


class ChatCompletionRole(str, Enum):
    SYSTEM = "system"
    ASSISTANT = "assistant"
    USER = "user"
    FUNCTION = "function"
