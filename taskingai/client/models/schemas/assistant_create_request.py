# -*- coding: utf-8 -*-

# assistant_create_request.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import List, Dict
from ..entities.assistant_memory import AssistantMemory
from ..entities.tool_ref import ToolRef
from ..entities.retrieval_ref import RetrievalRef
from ..entities.retrieval_config import RetrievalConfig

__all__ = ["AssistantCreateRequest"]


class AssistantCreateRequest(BaseModel):
    model_id: str = Field(...)
    name: str = Field("")
    description: str = Field("")
    system_prompt_template: List[str] = Field([])
    memory: AssistantMemory = Field(...)
    tools: List[ToolRef] = Field([])
    retrievals: List[RetrievalRef] = Field([])
    retrieval_configs: RetrievalConfig = Field(...)
    metadata: Dict[str, str] = Field({})
