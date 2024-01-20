from typing import Dict, Any, Optional
from enum import Enum
from .._base import TaskingaiBaseModel


__all__ = [
    "ActionAuthenticationType",
    "ActionAuthentication",
    "Action",
]


class ActionAuthenticationType(str, Enum):
    BASIC = "basic"
    BEARER = "bearer"
    CUSTOM = "custom"
    NONE = "none"


class ActionAuthentication(TaskingaiBaseModel):
    type: ActionAuthenticationType
    secret: Optional[str] = None
    content: Optional[Dict] = None


class Action(TaskingaiBaseModel):
    object: str
    action_id: str
    name: str
    description: str
    openapi_schema: Dict[str, Any]
    authentication: ActionAuthentication
    created_timestamp: int

    class Config:
        allow_population_by_field_name = True
