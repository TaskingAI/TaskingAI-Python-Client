# -*- coding: utf-8 -*-

# assistant.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import List, Dict
from .assistant_memory import AssistantMemory
from .tool_ref import ToolRef
from .retrieval_ref import RetrievalRef
from .retrieval_config import RetrievalConfig

__all__ = ["Assistant"]


class Assistant(BaseModel):
    object: str = Field("Assistant")
    assistant_id: str = Field(..., min_length=20, max_length=30)
    model_id: str = Field(..., min_length=8, max_length=8)
    name: str = Field("", min_length=0, max_length=256)
    description: str = Field("", min_length=0, max_length=512)
    system_prompt_template: List[str] = Field([], min_length=0, max_length=32)
    memory: AssistantMemory = Field(...)
    tools: List[ToolRef] = Field([], min_length=0, max_length=32)
    retrievals: List[RetrievalRef] = Field([], min_length=0, max_length=32)
    retrieval_configs: RetrievalConfig = Field(...)
    metadata: Dict[str, str] = Field({}, min_length=0, max_length=16)
    updated_timestamp: int = Field(..., ge=0)
    created_timestamp: int = Field(..., ge=0)
