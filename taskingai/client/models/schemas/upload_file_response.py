# -*- coding: utf-8 -*-

# upload_file_response.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from ..entities.file_id_data import FileIdData

__all__ = ["UploadFileResponse"]


class UploadFileResponse(BaseModel):
    status: str = Field("success")
    data: FileIdData = Field(...)
