# -*- coding: utf-8 -*-

# status.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from enum import Enum

__all__ = ["Status"]


class Status(str, Enum):
    CREATING = "creating"
    READY = "ready"
    DELETING = "deleting"
    ERROR = "error"
    PARTIAL = "partial"
