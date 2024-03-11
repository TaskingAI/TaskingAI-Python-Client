# -*- coding: utf-8 -*-

# tool_type.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from enum import Enum

__all__ = ["ToolType"]


class ToolType(str, Enum):
    ACTION = "action"
    PLUGIN = "plugin"
