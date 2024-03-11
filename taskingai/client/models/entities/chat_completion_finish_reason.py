# -*- coding: utf-8 -*-

# chat_completion_finish_reason.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from enum import Enum

__all__ = ["ChatCompletionFinishReason"]


class ChatCompletionFinishReason(str, Enum):
    STOP = "stop"
    LENGTH = "length"
    FUNCTION_CALLS = "function_calls"
    RECITATION = "recitation"
    ERROR = "error"
    UNKNOWN = "unknown"
