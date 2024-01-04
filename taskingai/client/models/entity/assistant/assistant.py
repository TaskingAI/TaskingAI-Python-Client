from typing import List, Dict
from pydantic import field_validator
from .._base import TaskingaiBaseModel
from .assistant_memory import *
from enum import Enum

__all__ = [
    "Assistant",
    "AssistantMemoryType",
    "AssistantNaiveMemory",
    "AssistantZeroMemory",
    "AssistantMessageWindowMemory",
    "AssistantTool",
    "AssistantRetrieval",
    "AssistantToolType",
    "AssistantRetrievalType",
    "AssistantMemory"
]


class AssistantToolType(str, Enum):
    ACTION = "action"
    FUNCTION = "function"


class AssistantRetrievalType(str, Enum):
    COLLECTION = "collection"


class AssistantRetrieval(TaskingaiBaseModel):
    type: AssistantRetrievalType
    id: str


class AssistantTool(TaskingaiBaseModel):
    type: AssistantToolType
    id: str


class Assistant(TaskingaiBaseModel):
    object: str
    assistant_id: str
    model_id: str
    name: str
    description: str
    system_prompt_template: List[str]
    memory: AssistantMemory
    tools: List[AssistantTool]
    retrievals: List[AssistantRetrieval]
    metadata: Dict[str, str]
    created_timestamp: int


    @field_validator('memory', mode='before')
    def validate_memory(cls, memory_dict: Dict):
        memory: AssistantMemory = build_assistant_memory(memory_dict)
        if not memory:
            raise ValueError('Invalid input memory')
        return memory
