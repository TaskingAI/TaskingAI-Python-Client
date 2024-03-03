# -*- coding: utf-8 -*-

# action_authentication_type.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from enum import Enum

__all__ = ["ActionAuthenticationType"]


class ActionAuthenticationType(str, Enum):
    BEARER = "bearer"
    BASIC = "basic"
    CUSTOM = "custom"
    NONE = "none"
