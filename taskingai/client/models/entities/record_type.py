# -*- coding: utf-8 -*-

# record_type.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from enum import Enum

__all__ = ["RecordType"]


class RecordType(str, Enum):
    TEXT = "text"
    FILE = "file"
    WEB = "web"
    QA_SHEET = "qa_sheet"
