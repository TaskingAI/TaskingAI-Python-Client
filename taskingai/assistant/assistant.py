from typing import Any, Optional, List, Dict, Union
from taskingai.client.models import *
from taskingai.client.apis import *

__all__ = [
    "Assistant",
    "AssistantTool",
    "AssistantRetrieval",
    "AssistantToolType",
    "ToolRef",
    "ToolType",
    "RetrievalRef",
    "RetrievalType",
    "RetrievalConfig",
    "RetrievalMethod",
    "AssistantRetrievalType",
    "get_assistant",
    "list_assistants",
    "create_assistant",
    "update_assistant",
    "delete_assistant",
    "a_get_assistant",
    "a_list_assistants",
    "a_create_assistant",
    "a_update_assistant",
    "a_delete_assistant",
    "clean_chat_context",
    "a_clean_chat_context",
]

AssistantTool = ToolRef
AssistantRetrieval = RetrievalRef
AssistantToolType = ToolType
AssistantRetrievalType = RetrievalType
DEFAULT_RETRIEVAL_CONFIG = RetrievalConfig(top_k=3, method=RetrievalMethod.USER_MESSAGE)


def _get_assistant_dict_params(
    memory: Optional[Union[AssistantMemory, Dict[str, Any]]] = None,
    tools: Optional[List[Union[AssistantTool, Dict[str, Any]]]] = None,
    retrievals: Optional[List[Union[AssistantRetrieval, Dict[str, Any]]]] = None,
    retrieval_configs: Optional[Union[RetrievalConfig, Dict[str, Any]]] = None,
):
    memory = memory if isinstance(memory, AssistantMemory) else (AssistantMemory(**memory) if memory else None)
    tools = [tool if isinstance(tool, AssistantTool) else AssistantTool(**tool) for tool in (tools or [])] or None
    retrievals = [
        retrieval if isinstance(retrieval, AssistantRetrieval) else AssistantRetrieval(**retrieval)
        for retrieval in (retrievals or [])
    ] or None
    retrieval_configs = (
        retrieval_configs
        if isinstance(retrieval_configs, RetrievalConfig)
        else RetrievalConfig(**retrieval_configs)
        if retrieval_configs
        else None
    )
    return memory, tools, retrievals, retrieval_configs


def list_assistants(
    *,
    order: str = "desc",
    limit: int = 20,
    after: Optional[str] = None,
    before: Optional[str] = None,
) -> List[Assistant]:
    """
    List assistants.

    :param order: The order of the assistants. It can be "asc" or "desc".
    :param limit: The maximum number of assistants to return.
    :param after: The cursor to get the next page of assistants.
    :param before: The cursor to get the previous page of assistants.
    :return: The list of assistants.
    """

    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    # only add non-None parameters
    payload = AssistantListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: AssistantListResponse = api_list_assistants(payload)
    assistants: List[Assistant] = response.data
    return assistants


async def a_list_assistants(
    *,
    order: str = "desc",
    limit: int = 20,
    after: Optional[str] = None,
    before: Optional[str] = None,
) -> List[Assistant]:
    """
    List assistants in async mode.

    :param order: The order of the assistants. It can be "asc" or "desc".
    :param limit: The maximum number of assistants to return.
    :param after: The cursor to get the next page of assistants.
    :param before: The cursor to get the previous page of assistants.
    :return: The list of assistants.
    """

    if after and before:
        raise ValueError("Only one of after and before can be specified.")

    # only add non-None parameters
    payload = AssistantListRequest(
        order=order,
        limit=limit,
        after=after,
        before=before,
    )
    response: AssistantListResponse = await async_api_list_assistants(payload)
    return response.data


def get_assistant(assistant_id: str) -> Assistant:
    """
    Get an assistant.

    :param assistant_id: The ID of the assistant.
    """

    response: AssistantGetResponse = api_get_assistant(assistant_id=assistant_id)
    return response.data


async def a_get_assistant(assistant_id: str) -> Assistant:
    """
    Get an assistant in async mode.

    :param assistant_id: The ID of the assistant.
    """

    response: AssistantGetResponse = await async_api_get_assistant(assistant_id=assistant_id)
    return response.data


def create_assistant(
    *,
    model_id: str,
    memory: Union[AssistantMemory, Dict[str, Any]],
    name: Optional[str] = None,
    description: Optional[str] = None,
    system_prompt_template: Optional[List[str]] = None,
    tools: Optional[List[Union[AssistantTool, Dict[str, Any]]]] = None,
    retrievals: Optional[List[Union[AssistantRetrieval, Dict[str, Any]]]] = None,
    retrieval_configs: Optional[Union[RetrievalConfig, Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Assistant:
    """
    Create an assistant.

    :param model_id: The ID of an available chat completion model in your project.
    :param memory: The assistant memory.
    :param name: The assistant name.
    :param description: The assistant description.
    :param system_prompt_template: A list of system prompt chunks where prompt variables are wrapped by curly brackets, e.g. {{variable}}.
    :param tools: The assistant tools.
    :param retrievals: The assistant retrievals.
    :param retrieval_configs: The assistant retrieval configurations.
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created assistant object.
    """
    memory, tools, retrievals, retrieval_configs = _get_assistant_dict_params(
        memory=memory, tools=tools, retrievals=retrievals, retrieval_configs=retrieval_configs
    )

    body = AssistantCreateRequest(
        model_id=model_id,
        name=name or "",
        description=description or "",
        memory=memory,
        system_prompt_template=system_prompt_template or [],
        tools=tools or [],
        retrievals=retrievals or [],
        retrieval_configs=retrieval_configs or RetrievalConfig(top_k=3, method=RetrievalMethod.USER_MESSAGE),
        metadata=metadata or {},
    )
    response: AssistantCreateResponse = api_create_assistant(payload=body)
    return response.data


async def a_create_assistant(
    *,
    model_id: str,
    memory: Union[AssistantMemory, Dict[str, Any]],
    name: Optional[str] = None,
    description: Optional[str] = None,
    system_prompt_template: Optional[List[str]] = None,
    tools: Optional[List[Union[AssistantTool, Dict[str, Any]]]] = None,
    retrievals: Optional[List[Union[AssistantRetrieval, Dict[str, Any]]]] = None,
    retrieval_configs: Optional[Union[RetrievalConfig, Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Assistant:
    """
    Create an assistant in async mode.

    :param model_id: The ID of an available chat completion model in your project.
    :param memory: The assistant memory.
    :param name: The assistant name.
    :param description: The assistant description.
    :param system_prompt_template: A list of system prompt chunks where prompt variables are wrapped by curly brackets, e.g. {{variable}}.
    :param tools: The assistant tools.
    :param retrievals: The assistant retrievals.
    :param retrieval_configs: The assistant retrieval configurations.
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created assistant object.
    """
    memory, tools, retrievals, retrieval_configs = _get_assistant_dict_params(
        memory=memory, tools=tools, retrievals=retrievals, retrieval_configs=retrieval_configs
    )

    body = AssistantCreateRequest(
        model_id=model_id,
        name=name or "",
        description=description or "",
        memory=memory,
        system_prompt_template=system_prompt_template or [],
        tools=tools or [],
        retrievals=retrievals or [],
        retrieval_configs=retrieval_configs or DEFAULT_RETRIEVAL_CONFIG,
        metadata=metadata or {},
    )
    response: AssistantCreateResponse = await async_api_create_assistant(payload=body)
    return response.data


def update_assistant(
    assistant_id: str,
    *,
    model_id: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    system_prompt_template: Optional[List[str]] = None,
    memory: Optional[Union[AssistantMemory, Dict[str, Any]]] = None,
    tools: Optional[List[Union[AssistantTool, Dict[str, Any]]]] = None,
    retrievals: Optional[List[Union[AssistantRetrieval, Dict[str, Any]]]] = None,
    retrieval_configs: Optional[Union[RetrievalConfig, Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Assistant:
    """
    Update an assistant.

    :param assistant_id: The ID of the assistant.
    :param model_id: The ID of an available chat completion model in your project.
    :param name: The assistant name.
    :param description: The assistant description.
    :param system_prompt_template: A list of system prompt chunks where prompt variables are wrapped by curly brackets, e.g. {{variable}}.
    :param memory: The assistant memory.
    :param tools: The assistant tools.
    :param retrievals: The assistant retrievals.
    :param retrieval_configs: The assistant retrieval configurations.
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The updated assistant object.
    """

    memory, tools, retrievals, retrieval_configs = _get_assistant_dict_params(
        memory=memory, tools=tools, retrievals=retrievals, retrieval_configs=retrieval_configs
    )

    body = AssistantUpdateRequest(
        model_id=model_id,
        name=name,
        description=description,
        memory=memory,
        system_prompt_template=system_prompt_template,
        tools=tools,
        retrievals=retrievals,
        retrieval_configs=retrieval_configs,
        metadata=metadata,
    )
    response: AssistantUpdateResponse = api_update_assistant(assistant_id=assistant_id, payload=body)
    return response.data


async def a_update_assistant(
    assistant_id: str,
    *,
    model_id: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    system_prompt_template: Optional[List[str]] = None,
    memory: Optional[Union[AssistantMemory, Dict[str, Any]]] = None,
    tools: Optional[List[Union[AssistantTool, Dict[str, Any]]]] = None,
    retrievals: Optional[List[Union[AssistantRetrieval, Dict[str, Any]]]] = None,
    retrieval_configs: Optional[Union[RetrievalConfig, Dict[str, Any]]] = None,
    metadata: Optional[Dict[str, str]] = None,
) -> Assistant:
    """
    Update an assistant in async mode.

    :param assistant_id: The ID of the assistant.
    :param model_id: The ID of an available chat completion model in your project.
    :param name: The assistant name.
    :param description: The assistant description.
    :param system_prompt_template: A list of system prompt chunks where prompt variables are wrapped by curly brackets, e.g. {{variable}}.
    :param memory: The assistant memory.
    :param tools: The assistant tools.
    :param retrievals: The assistant retrievals.
    :param retrieval_configs: The assistant retrieval configurations.
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The updated assistant object.
    """

    memory, tools, retrievals, retrieval_configs = _get_assistant_dict_params(
        memory=memory, tools=tools, retrievals=retrievals, retrieval_configs=retrieval_configs
    )

    body = AssistantUpdateRequest(
        model_id=model_id,
        name=name,
        description=description,
        memory=memory,
        system_prompt_template=system_prompt_template,
        tools=tools,
        retrievals=retrievals,
        retrieval_configs=retrieval_configs,
        metadata=metadata,
    )
    response: AssistantUpdateResponse = await async_api_update_assistant(assistant_id=assistant_id, payload=body)
    return response.data


def delete_assistant(assistant_id: str) -> None:
    """
    Delete an assistant.

    :param assistant_id: The ID of the assistant.
    """

    api_delete_assistant(assistant_id=assistant_id)


async def a_delete_assistant(assistant_id: str) -> None:
    """
    Delete an assistant in async mode.

    :param assistant_id: The ID of the assistant.
    """

    await async_api_delete_assistant(assistant_id=assistant_id)


def clean_chat_context(assistant_id: str, chat_id: str) -> ChatCleanContextResponse:
    """
    Clean chat context.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    """

    api_clean_chat_context(assistant_id=assistant_id, chat_id=chat_id)


async def a_clean_chat_context(assistant_id: str, chat_id: str) -> ChatCleanContextResponse:
    """
    Clean chat context in async mode.

    :param assistant_id: The ID of the assistant.
    :param chat_id: The ID of the chat.
    """

    await async_api_clean_chat_context(assistant_id=assistant_id, chat_id=chat_id)
