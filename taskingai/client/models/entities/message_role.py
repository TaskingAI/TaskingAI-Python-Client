# -*- coding: utf-8 -*-

# message_role.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from enum import Enum

__all__ = ["MessageRole"]


class MessageRole(str, Enum):
    USER = "user"
    ASSISTANT = "assistant"
