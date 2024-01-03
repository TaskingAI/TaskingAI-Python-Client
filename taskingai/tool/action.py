from typing import Optional, List, Dict

from taskingai.client.utils import get_api_instance, ModuleType
from taskingai.client.models import Action, ActionAuthentication, ActionAuthenticationType
from taskingai.client.models import (
    ActionBulkCreateRequest,
    ActionBulkCreateResponse,
    ActionUpdateRequest,
    ActionUpdateResponse,
    ActionGetResponse,
    ActionListResponse,
    ActionRunRequest,
    ActionRunResponse
)

__all__ = [
    "Action",
    "ActionAuthentication",
    "ActionAuthenticationType",
    "get_action",
    "list_actions",
    "bulk_create_actions",
    "update_action",
    "delete_action",
    "run_action",
    "a_get_action",
    "a_list_actions",
    "a_bulk_create_actions",
    "a_update_action",
    "a_delete_action",
    "a_run_action",
]


def list_actions(
        order: str = "desc",
        limit: int = 20,
        after: Optional[str] = None,
        before: Optional[str] = None,
) -> List[Action]:
    """
    List actions.

    :param order: The order of the actions. It can be "asc" or "desc".
    :param limit: The maximum number of actions to return.
    :param after: The cursor to get the next page of actions.
    :param before: The cursor to get the previous page of actions.
    :return: The list of actions.
    """
    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    api_instance = get_api_instance(ModuleType.tool)
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: ActionListResponse = api_instance.list_actions(**params)
    actions: List[Action] = [Action(**item) for item in response.data]
    return actions


async def a_list_actions(
        order: str = "desc",
        limit: int = 20,
        after: Optional[str] = None,
        before: Optional[str] = None,
) -> List[Action]:
    """
    List actions in async mode.

    :param order: The order of the actions. It can be "asc" or "desc".
    :param limit: The maximum number of actions to return.
    :param after: The cursor to get the next page of actions.
    :param before: The cursor to get the previous page of actions.
    :return: The list of actions.
    """
    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    api_instance = get_api_instance(ModuleType.tool, async_client=True)
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: ActionListResponse = await api_instance.list_actions(**params)
    actions: List[Action] = [Action(**item) for item in response.data]
    return actions



def get_action(action_id: str) -> Action:
    """
    Get an action.

    :param action_id: The ID of the action.
    """

    api_instance = get_api_instance(ModuleType.tool)
    response: ActionGetResponse = api_instance.get_action(action_id=action_id)
    action: Action = Action(**response.data)
    return action


async def a_get_action(action_id: str) -> Action:
    """
    Get an action in async mode.

    :param action_id: The ID of the action.
    """

    api_instance = get_api_instance(ModuleType.tool, async_client=True)
    response: ActionGetResponse = await api_instance.get_action(action_id=action_id)
    action: Action = Action(**response.data)
    return action

def bulk_create_actions(
    schema: Dict,
    authentication: Optional[ActionAuthentication] = None
) -> List[Action]:
    """
    Create actions from an OpenAPI schema.

    :param schema: The action schema is compliant with the OpenAPI Specification. If there are multiple paths and methods in the schema, the service will create multiple actions whose schema only has exactly one path and one method
    :param authentication: The action API authentication.
    :return: The created action object.
    """

    # todo verify schema
    api_instance = get_api_instance(ModuleType.tool)
    if authentication is None:
        authentication = ActionAuthentication(
            type=ActionAuthenticationType.NONE,
        )
    body = ActionBulkCreateRequest(
        schema=schema,
        authentication=authentication,
    )
    response: ActionBulkCreateResponse = api_instance.bulk_create_action(body=body)
    actions: List[Action] = [Action(**data) for data in response.data]
    return actions


async def a_bulk_create_actions(
    schema: Dict,
    authentication: Optional[ActionAuthentication] = None
) -> List[Action]:
    """
    Create actions from an OpenAPI schema in async mode.

    :param schema: The action schema is compliant with the OpenAPI Specification. If there are multiple paths and methods in the schema, the service will create multiple actions whose schema only has exactly one path and one method
    :param authentication: The action API authentication.
    :return: The created action object.
    """

    # todo verify schema
    api_instance = get_api_instance(ModuleType.tool, async_client=True)
    if authentication is None:
        authentication = ActionAuthentication(
            type=ActionAuthenticationType.NONE,
        )
    body = ActionBulkCreateRequest(
        schema=schema,
        authentication=authentication,
    )
    response: ActionBulkCreateResponse = await api_instance.bulk_create_action(body=body)
    actions: List[Action] = [Action(**data) for data in response.data]
    return actions


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
    api_instance = get_api_instance(ModuleType.tool)
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


async def a_update_action(
    action_id: str,
    schema: Optional[Dict] = None,
    authentication: Optional[ActionAuthentication] = None,
) -> Action:
    """
    Update an action in async mode.

    :param action_id: The ID of the action.
    :param schema: The action schema, which is compliant with the OpenAPI Specification. It should only have exactly one path and one method.
    :param authentication: The action API authentication.
    :return: The updated action object.
    """
    api_instance = get_api_instance(ModuleType.tool, async_client=True)
    body = ActionUpdateRequest(
        schema=schema,
        authentication=authentication,
    )
    response: ActionUpdateResponse = await api_instance.update_action(
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

    api_instance = get_api_instance(ModuleType.tool)
    api_instance.delete_action(action_id=action_id)


async def a_delete_action(action_id: str) -> None:
    """
    Delete an action in async mode.

    :param action_id: The ID of the action.
    """

    api_instance = get_api_instance(ModuleType.tool, async_client=True)
    await api_instance.delete_action(action_id=action_id)


def run_action(
    action_id: str,
    parameters: Dict,
) -> Dict:
    """
    Run an action.

    :param action_id: The ID of the action.
    :param parameters: The action parameters.
    :return: The action response.
    """

    api_instance = get_api_instance(ModuleType.tool)
    body = ActionRunRequest(
        parameters=parameters,
    )
    response: ActionRunResponse = api_instance.run_action(
        action_id=action_id,
        body=body
    )
    result = response.data
    return result


async def a_run_action(
    action_id: str,
    parameters: Dict,
) -> Dict:
    """
    Run an action in async mode.

    :param action_id: The ID of the action.
    :param parameters: The action parameters.
    :return: The action response.
    """

    api_instance = get_api_instance(ModuleType.tool, async_client=True)
    body = ActionRunRequest(
        parameters=parameters,
    )
    response: ActionRunResponse = await api_instance.run_action(
        action_id=action_id,
        body=body
    )
    result = response.data
    return result

