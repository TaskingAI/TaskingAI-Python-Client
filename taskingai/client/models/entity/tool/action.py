from typing import Dict, Any, Optional
from enum import Enum
from .._base import TaskingaiBaseModel
from pydantic import Field


__all__ = [
    "ActionAuthenticationType",
    "ActionAuthentication",
    "Action",
]


class ActionAuthenticationType(str, Enum):
    basic = "basic"
    bearer = "bearer"
    custom = "custom"
    none = "none"


class ActionAuthentication(TaskingaiBaseModel):
    type: ActionAuthenticationType
    secret: Optional[str] = None
    content: Optional[Dict] = None


class Action(TaskingaiBaseModel):
    object: str
    action_id: str
    name: str
    description: str
    schema: Dict[str, Any] = Field(..., alias='schema')
    authentication: ActionAuthentication
    created_timestamp: int

    class Config:
        allow_population_by_field_name = True

