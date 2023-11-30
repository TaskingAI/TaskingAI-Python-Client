from typing import List, Dict
from .._base import TaskingaiBaseModel
from enum import Enum

__all__ = [
    "Assistant",
    "AssistantTool",
    "AssistantRetrieval",
    "AssistantToolType",
    "AssistantRetrievalType",
]


class AssistantToolType(str, Enum):
    action = "action"
    function = "function"


class AssistantRetrievalType(str, Enum):
    collection = "collection"


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
    tools: List[AssistantTool]
    retrievals: List[AssistantRetrieval]
    metadata: Dict[str, str]
    created_timestamp: int
