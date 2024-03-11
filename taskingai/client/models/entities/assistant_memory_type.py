# -*- coding: utf-8 -*-

# assistant_memory_type.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from enum import Enum

__all__ = ["AssistantMemoryType"]


class AssistantMemoryType(str, Enum):
    ZERO = "zero"
    NAIVE = "naive"
    MESSAGE_WINDOW = "message_window"
