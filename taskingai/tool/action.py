from typing import Any, Optional, List, Dict, Union

from taskingai.client.models import *
from taskingai.client.apis import *


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

    # only add non-None parameters
    payload = ActionListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: ActionListResponse = api_list_actions(payload=payload)
    return response.data


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

    # only add non-None parameters
    payload = ActionListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: ActionListResponse = await async_api_list_actions(payload)
    return response.data


def get_action(action_id: str) -> Action:
    """
    Get an action.

    :param action_id: The ID of the action.
    """

    response: ActionGetResponse = api_get_action(action_id=action_id)
    return response.data


async def a_get_action(action_id: str) -> Action:
    """
    Get an action in async mode.

    :param action_id: The ID of the action.
    """

    response: ActionGetResponse = await async_api_get_action(action_id=action_id)
    return response.data


def bulk_create_actions(
    openapi_schema: Dict,
    authentication: Optional[Union[ActionAuthentication, Dict[str, Any]]] = None,
) -> List[Action]:
    """
    Create actions from an OpenAPI schema.

    :param openapi_schema: The action schema is compliant with the OpenAPI Specification. If there are multiple paths and methods in the openapi_schema, the service will create multiple actions whose openapi_schema only has exactly one path and one method
    :param authentication: The action API authentication.
    :return: The created action object.
    """

    authentication = (
        authentication
        if isinstance(authentication, ActionAuthentication)
        else ActionAuthentication(**(authentication or ActionAuthentication(type=ActionAuthenticationType.NONE)))
    )

    body = ActionBulkCreateRequest(
        openapi_schema=openapi_schema,
        authentication=authentication,
    )
    response: ActionBulkCreateResponse = api_bulk_create_actions(payload=body)
    return response.data


async def a_bulk_create_actions(
    openapi_schema: Dict,
    authentication: Optional[Union[ActionAuthentication, Dict[str, Any]]] = None,
) -> List[Action]:
    """
    Create actions from an OpenAPI schema in async mode.

    :param openapi_schema: The action schema is compliant with the OpenAPI Specification. If there are multiple paths and methods in the openapi_schema, the service will create multiple actions whose openapi_schema only has exactly one path and one method
    :param authentication: The action API authentication.
    :return: The created action object.
    """

    authentication = (
        authentication
        if isinstance(authentication, ActionAuthentication)
        else ActionAuthentication(**(authentication or ActionAuthentication(type=ActionAuthenticationType.NONE)))
    )

    body = ActionBulkCreateRequest(
        openapi_schema=openapi_schema,
        authentication=authentication,
    )
    response: ActionBulkCreateResponse = await async_api_bulk_create_actions(payload=body)
    return response.data


def update_action(
    action_id: str,
    openapi_schema: Optional[Dict] = None,
    authentication: Optional[Union[ActionAuthentication, Dict[str, Any]]] = None,
) -> Action:
    """
    Update an action.

    :param action_id: The ID of the action.
    :param openapi_schema: The action schema, which is compliant with the OpenAPI Specification. It should only have exactly one path and one method.
    :param authentication: The action API authentication.
    :return: The updated action object.
    """
    if authentication:
        authentication = (
            authentication
            if isinstance(authentication, ActionAuthentication)
            else ActionAuthentication(**authentication)
        )
    body = ActionUpdateRequest(
        openapi_schema=openapi_schema,
        authentication=authentication,
    )
    response: ActionUpdateResponse = api_update_action(action_id=action_id, payload=body)
    return response.data


async def a_update_action(
    action_id: str,
    openapi_schema: Optional[Dict] = None,
    authentication: Optional[Union[ActionAuthentication, Dict[str, Any]]] = None,
) -> Action:
    """
    Update an action in async mode.

    :param action_id: The ID of the action.
    :param openapi_schema: The action schema, which is compliant with the OpenAPI Specification. It should only have exactly one path and one method.
    :param authentication: The action API authentication.
    :return: The updated action object.
    """
    if authentication:
        authentication = (
            authentication
            if isinstance(authentication, ActionAuthentication)
            else ActionAuthentication(**authentication)
        )
    body = ActionUpdateRequest(
        openapi_schema=openapi_schema,
        authentication=authentication,
    )
    response: ActionUpdateResponse = await async_api_update_action(action_id=action_id, payload=body)
    return response.data


def delete_action(action_id: str) -> None:
    """
    Delete an action.

    :param action_id: The ID of the action.
    """

    api_delete_action(action_id=action_id)


async def a_delete_action(action_id: str) -> None:
    """
    Delete an action in async mode.

    :param action_id: The ID of the action.
    """

    await async_api_delete_action(action_id=action_id)


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

    body = ActionRunRequest(
        parameters=parameters,
    )
    response: ActionRunResponse = api_run_action(action_id=action_id, payload=body)
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

    body = ActionRunRequest(
        parameters=parameters,
    )
    response: ActionRunResponse = await async_api_run_action(action_id=action_id, payload=body)
    result = response.data
    return result
