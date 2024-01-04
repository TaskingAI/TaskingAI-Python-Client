from typing import Optional, List, Dict, Any

from taskingai.client.utils import get_api_instance, ModuleType
from taskingai.client.models import Function
from taskingai.client.models import FunctionCreateRequest, FunctionCreateResponse, \
    FunctionUpdateRequest, FunctionUpdateResponse, \
    FunctionGetResponse, FunctionListResponse

__all__ = [
    "Function",
    "get_function",
    "list_functions",
    "create_function",
    "update_function",
    "delete_function",
    "a_get_function",
    "a_list_functions",
    "a_create_function",
    "a_update_function",
    "a_delete_function",
]


def list_functions(
        order: str = "desc",
        limit: int = 20,
        after: Optional[str] = None,
        before: Optional[str] = None,
) -> List[Function]:
    """
    List functions.

    :param order: The order of the functions. It can be "asc" or "desc".
    :param limit: The maximum number of functions to return.
    :param after: The cursor to get the next page of functions.
    :param before: The cursor to get the previous page of functions.
    :return: The list of functions.
    """
    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    api_instance = get_api_instance(ModuleType.TOOL)
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: FunctionListResponse = api_instance.list_functions(**params)
    functions: List[Function] = [Function(**item) for item in response.data]
    return functions


async def a_list_functions(
        order: str = "desc",
        limit: int = 20,
        after: Optional[str] = None,
        before: Optional[str] = None,
) -> List[Function]:
    """
    List functions in async mode.

    :param order: The order of the functions. It can be "asc" or "desc".
    :param limit: The maximum number of functions to return.
    :param after: The cursor to get the next page of functions.
    :param before: The cursor to get the previous page of functions.
    :return: The list of functions.
    """
    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    api_instance = get_api_instance(ModuleType.TOOL, async_client=True)
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: FunctionListResponse = await api_instance.list_functions(**params)
    functions: List[Function] = [Function(**item) for item in response.data]
    return functions



def get_function(function_id: str) -> Function:
    """
    Get a function.

    :param function_id: The ID of the function.
    """

    api_instance = get_api_instance(ModuleType.TOOL)
    response: FunctionGetResponse = api_instance.get_function(function_id=function_id)
    function: Function = Function(**response.data)
    return function


async def a_get_function(function_id: str) -> Function:
    """
    Get a function in async mode.

    :param function_id: The ID of the function.
    """

    api_instance = get_api_instance(ModuleType.TOOL, async_client=True)
    response: FunctionGetResponse = await api_instance.get_function(function_id=function_id)
    function: Function = Function(**response.data)
    return function


def create_function(
        name: str,
        description: str,
        parameters: Dict,
) -> Function:
    """
    Create a function.

    :param name: The name of the function. It shoule be a meaningful function name, consists of letters, digits and underscore "_" and its first character cannot be a digit.
    :param description: The description of the function.
    :param parameters: The parameters of the function.
    :return: The created function object.
    """

    # todo verify parameters
    api_instance = get_api_instance(ModuleType.TOOL)
    body = FunctionCreateRequest(
        name=name,
        description=description,
        parameters=parameters,
    )
    response: FunctionCreateResponse = api_instance.create_function(body=body)
    function: Function = Function(**response.data)
    return function


async def a_create_function(
        name: str,
        description: str,
        parameters: Dict,
) -> Function:
    """
    Create a function in async mode.

    :param name: The name of the function. It shoule be a meaningful function name, consists of letters, digits and underscore "_" and its first character cannot be a digit.
    :param description: The description of the function.
    :param parameters: The parameters of the function.
    :return: The created function object.
    """

    # todo verify parameters
    api_instance = get_api_instance(ModuleType.TOOL, async_client=True)
    body = FunctionCreateRequest(
        name=name,
        description=description,
        parameters=parameters,
    )
    response: FunctionCreateResponse = await api_instance.create_function(body=body)
    function: Function = Function(**response.data)
    return function


def update_function(
    function_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    parameters: Optional[Dict] = None,
) -> Function:
    """
    Update a function.

    :param function_id: The ID of the function.
    :param schema: The function schema, which is compliant with the OpenAPI Specification. It should only have exactly one path and one method.
    :param authentication: The function API authentication.
    :return: The updated function object.
    """
    #todo: verify schema
    api_instance = get_api_instance(ModuleType.TOOL)
    body = FunctionUpdateRequest(
        name=name,
        description=description,
        parameters=parameters,
    )
    response: FunctionUpdateResponse = api_instance.update_function(
        function_id=function_id,
        body=body
    )
    function: Function = Function(**response.data)
    return function


async def a_update_function(
    function_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    parameters: Optional[Dict] = None,
) -> Function:
    """
    Update a function in async mode.

    :param function_id: The ID of the function.
    :param schema: The function schema, which is compliant with the OpenAPI Specification. It should only have exactly one path and one method.
    :param authentication: The function API authentication.
    :return: The updated function object.
    """
    api_instance = get_api_instance(ModuleType.TOOL, async_client=True)
    body = FunctionUpdateRequest(
        name=name,
        description=description,
        parameters=parameters,
    )
    response: FunctionUpdateResponse = await api_instance.update_function(
        function_id=function_id,
        body=body
    )
    function: Function = Function(**response.data)
    return function


def delete_function(function_id: str) -> None:
    """
    Delete a function.

    :param function_id: The ID of the function.
    """

    api_instance = get_api_instance(ModuleType.TOOL)
    api_instance.delete_function(function_id=function_id)


async def a_delete_function(function_id: str) -> None:
    """
    Delete a function in async mode.

    :param function_id: The ID of the function.
    """

    api_instance = get_api_instance(ModuleType.TOOL, async_client=True)
    await api_instance.delete_function(function_id=function_id)


