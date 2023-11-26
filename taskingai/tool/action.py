import time
from typing import NamedTuple, Optional, List

from taskingai.config import Config
from taskingai.client.utils import get_user_agent
from taskingai.client.api.tool_api import ToolApi
from taskingai.client.api_client import ApiClient
from taskingai.client.models import Action, ActionAuthenticationType
from taskingai.client.models import ActionCreateRequest, ActionCreateResponse, \
    ActionUpdateRequest, ActionUpdateResponse, \
    ActionGetResponse, ActionListResponse, ActionDeleteResponse

__all__ = [
    "get_action",
    "list_actions",
    "create_action",
    "update_action",
    "delete_action",
]


def _get_api_instance():
    client_config = Config.OPENAPI_CONFIG
    client_config.api_key = client_config.api_key or {}
    api_client = ApiClient(configuration=client_config)
    api_client.user_agent = get_user_agent()
    api_instance = ToolApi(api_client)
    return api_instance


def list_actions(
        order: str = "desc",
        limit: int = 20,
        offset: Optional[int] = None,
        after: Optional[str] = None,
        before: Optional[str] = None,
) -> List[Action]:
    """
    List actions.

    :param order: The order of the actions. It can be "asc" or "desc".
    :param limit: The maximum number of actions to return.
    :param offset: The offset of the actions.
    :param after: The cursor to get the next page of actions.
    :param before: The cursor to get the previous page of actions.
    :return: The list of actions.
    """

    api_instance = _get_api_instance()
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "offset": offset,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: ActionListResponse = api_instance.list_actions(**params)
    actions: List[Action] = [Action(**item) for item in response.data]
    return actions


def get_action(action_id: str) -> Action:
    """
    Get an action.

    :param action_id: The ID of the action.
    """

    api_instance = _get_api_instance()
    response: ActionGetResponse = api_instance.get_action(action_id=action_id)
    action: Action = Action(**response.data)
    return action


def create_action(
    schema: str,
    authentication: ActionAuthentication,
    system_prompt_template: Optional[List[str]] = None,
    metadata: Optional[dict] = None,
) -> Action:
    """
    Create an action.

    :param model_id: The ID of an available chat completion model in your project.
    :param name: The action name.
    :param description: The action description.
    :param system_prompt_template: A list of system prompt chunks where prompt variables are wrapped by curly brackets, e.g. {{variable}}.
    :param tools: The action tools.
    :param retrievals: The action retrievals.
    :param metadata: The action metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The action object.
    """

    api_instance = _get_api_instance()
    body = ActionCreateRequest(
        model_id=model_id,
        name=name,
        description=description,
        system_prompt_template=system_prompt_template,
        tools=tools,
        retrievals=retrievals,
        metadata=metadata,
    )
    response: ActionCreateResponse = api_instance.create_action(body=body)
    action: Action = Action(**response.data)
    return action


def update_action(
        action_id: str,
        model_id: Optional[str] = None,
        name: Optional[str] = None,
        description: Optional[str] = None,
        system_prompt_template: Optional[List[str]] = None,
        tools: Optional[List[ActionTool]] = None,
        retrievals: Optional[List[ActionRetrieval]] = None,
        metadata: Optional[dict] = None,
) -> Action:
    """
    Update an action.

    :param action_id: The ID of the action.
    :param model_id: The ID of an available chat completion model in your project.
    :param name: The action name.
    :param description: The action description.
    :param system_prompt_template: A list of system prompt chunks where prompt variables are wrapped by curly brackets, e.g. {{variable}}.
    :param tools: The action tools.
    :param retrievals: The action retrievals.
    :param metadata: The action metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The action object.
    """

    api_instance = _get_api_instance()
    body = ActionUpdateRequest(
        model_id=model_id,
        name=name,
        description=description,
        system_prompt_template=system_prompt_template,
        tools=tools,
        retrievals=retrievals,
        metadata=metadata,
    )
    response: ActionUpdateResponse = api_instance.update_action(action_id=action_id, body=body)
    action: Action = Action(**response.data)
    return action


def delete_action(action_id: str) -> None:
    """
    Delete an action.

    :param action_id: The ID of the action.
    """

    api_instance = _get_api_instance()
    api_instance.delete_action(action_id=action_id)

