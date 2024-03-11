# -*- coding: utf-8 -*-

# assistant_update_request.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict
from ..entities.assistant_memory import AssistantMemory
from ..entities.tool_ref import ToolRef
from ..entities.retrieval_ref import RetrievalRef
from ..entities.retrieval_config import RetrievalConfig

__all__ = ["AssistantUpdateRequest"]


class AssistantUpdateRequest(BaseModel):
    model_id: Optional[str] = Field(None)
    name: Optional[str] = Field(None)
    description: Optional[str] = Field(None)
    system_prompt_template: Optional[List[str]] = Field(None)
    memory: Optional[AssistantMemory] = Field(None)
    tools: Optional[List[ToolRef]] = Field(None)
    retrievals: Optional[List[RetrievalRef]] = Field(None)
    retrieval_configs: Optional[RetrievalConfig] = Field(None)
    metadata: Optional[Dict[str, str]] = Field(None)
