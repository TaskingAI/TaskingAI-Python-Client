# -*- coding: utf-8 -*-

# text_embedding_input_type.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from enum import Enum

__all__ = ["TextEmbeddingInputType"]


class TextEmbeddingInputType(str, Enum):
    DOCUMENT = "document"
    QUERY = "query"
