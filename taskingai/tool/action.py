from typing import Optional, List, Dict

from taskingai.client.utils import get_tool_api_instance
from taskingai.client.models import Action, ActionAuthentication, ActionAuthenticationType
from taskingai.client.models import ActionCreateRequest, ActionCreateResponse, \
    ActionUpdateRequest, ActionUpdateResponse, \
    ActionGetResponse, ActionListResponse

__all__ = [
    "Action",
    "ActionAuthentication",
    "ActionAuthenticationType",
    "get_action",
    "list_actions",
    "create_action",
    "update_action",
    "delete_action",
]


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
    # todo: verify only one of offset, after and before is not None
    api_instance = get_tool_api_instance()
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

    api_instance = get_tool_api_instance()
    response: ActionGetResponse = api_instance.get_action(action_id=action_id)
    action: Action = Action(**response.data)
    return action


def create_action(
    schema: Dict,
    authentication: ActionAuthentication
) -> Action:
    """
    Create an action.

    :param schema: The action schema is compliant with the OpenAPI Specification. If there are multiple paths and methods in the schema, the service will create multiple actions whose schema only has exactly one path and one method
    :param authentication: The action API authentication.
    :return: The created action object.
    """

    # todo verify schema
    api_instance = get_tool_api_instance()
    body = ActionCreateRequest(
        schema=schema,
        authentication=authentication,
    )
    response: ActionCreateResponse = api_instance.create_action(body=body)
    action: Action = Action(**response.data)
    return action


def update_action(
    action_id: str,
    schema: Optional[Dict] = None,
    authentication: Optional[ActionAuthentication] = None,
) -> Action:
    """
    Update an action.

    :param action_id: The ID of the action.
    :param schema: The action schema, which is compliant with the OpenAPI Specification. It should only have exactly one path and one method.
    :param authentication: The action API authentication.
    :return: The updated action object.
    """
    #todo: verify schema
    api_instance = get_tool_api_instance()
    body = ActionUpdateRequest(
        schema=schema,
        authentication=authentication,
    )
    response: ActionUpdateResponse = api_instance.update_action(
        action_id=action_id,
        body=body
    )
    action: Action = Action(**response.data)
    return action


def delete_action(action_id: str) -> None:
    """
    Delete an action.

    :param action_id: The ID of the action.
    """

    api_instance = get_tool_api_instance()
    api_instance.delete_action(action_id=action_id)

