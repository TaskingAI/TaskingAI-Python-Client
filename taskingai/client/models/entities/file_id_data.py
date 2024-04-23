# -*- coding: utf-8 -*-

# file_id_data.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field


__all__ = ["FileIdData"]


class FileIdData(BaseModel):
    file_id: str = Field(...)
