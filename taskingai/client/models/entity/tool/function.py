from typing import Dict, Any, List
from .._base import TaskingaiBaseModel

__all__ = [
    "Function",
    "FunctionParameters",
]


class FunctionParameters(TaskingaiBaseModel):
    type: str
    properties: Dict[str, Any]
    required: List[str]


class Function(TaskingaiBaseModel):
    object: str
    function_id: str
    name: str
    description: str
    parameters: FunctionParameters
    created_timestamp: int
