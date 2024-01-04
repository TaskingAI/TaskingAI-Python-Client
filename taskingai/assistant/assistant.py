from typing import Optional, List, Dict

from taskingai.client.utils import get_api_instance, ModuleType
from taskingai.client.models import (
    Assistant,
    AssistantMemory,
    AssistantRetrieval,
    AssistantTool,
    AssistantToolType,
    AssistantRetrievalType
)

from taskingai.client.models import (
    AssistantCreateRequest,
    AssistantCreateResponse,
    AssistantUpdateRequest,
    AssistantUpdateResponse,
    AssistantGetResponse,
    AssistantListResponse,
)

__all__ = [
    "Assistant",
    "AssistantTool",
    "AssistantRetrieval",
    "AssistantToolType",
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
]


def list_assistants(
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

    api_instance = get_api_instance(ModuleType.ASSISTANT)
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: AssistantListResponse = api_instance.list_assistants(**params)
    assistants: List[Assistant] = [Assistant(**item) for item in response.data]
    return assistants


async def a_list_assistants(
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

    api_instance = get_api_instance(ModuleType.ASSISTANT, async_client=True)
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: AssistantListResponse = await api_instance.list_assistants(**params)
    assistants: List[Assistant] = [Assistant(**item) for item in response.data]
    return assistants



def get_assistant(assistant_id: str) -> Assistant:
    """
    Get an assistant.

    :param assistant_id: The ID of the assistant.
    """

    api_instance = get_api_instance(ModuleType.ASSISTANT)
    response: AssistantGetResponse = api_instance.get_assistant(assistant_id=assistant_id)
    assistant: Assistant = Assistant(**response.data)
    return assistant


async def a_get_assistant(assistant_id: str) -> Assistant:
    """
    Get an assistant in async mode.

    :param assistant_id: The ID of the assistant.
    """

    api_instance = get_api_instance(ModuleType.ASSISTANT, async_client=True)
    response: AssistantGetResponse = await api_instance.get_assistant(assistant_id=assistant_id)
    assistant: Assistant = Assistant(**response.data)
    return assistant


def create_assistant(
    model_id: str,
    memory: AssistantMemory,
    name: Optional[str] = None,
    description: Optional[str] = None,
    system_prompt_template: Optional[List[str]] = None,
    tools: Optional[List[AssistantTool]] = None,
    retrievals: Optional[List[AssistantRetrieval]] = None,
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
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created assistant object.
    """

    api_instance = get_api_instance(ModuleType.ASSISTANT)
    memory_dict = memory.model_dump()
    body = AssistantCreateRequest(
        model_id=model_id,
        name=name,
        description=description,
        memory=memory_dict,
        system_prompt_template=system_prompt_template,
        tools=tools,
        retrievals=retrievals,
        metadata=metadata,
    )
    response: AssistantCreateResponse = api_instance.create_assistant(body=body)
    assistant: Assistant = Assistant(**response.data)
    return assistant


async def a_create_assistant(
    model_id: str,
    memory: AssistantMemory,
    name: Optional[str] = None,
    description: Optional[str] = None,
    system_prompt_template: Optional[List[str]] = None,
    tools: Optional[List[AssistantTool]] = None,
    retrievals: Optional[List[AssistantRetrieval]] = None,
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
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created assistant object.
    """

    api_instance = get_api_instance(ModuleType.ASSISTANT, async_client=True)
    memory_dict = memory.model_dump()
    body = AssistantCreateRequest(
        model_id=model_id,
        name=name,
        description=description,
        memory=memory_dict,
        system_prompt_template=system_prompt_template,
        tools=tools,
        retrievals=retrievals,
        metadata=metadata,
    )
    response: AssistantCreateResponse = await api_instance.create_assistant(body=body)
    assistant: Assistant = Assistant(**response.data)
    return assistant


def update_assistant(
    assistant_id: str,
    model_id: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    system_prompt_template: Optional[List[str]] = None,
    memory: Optional[AssistantMemory] = None,
    tools: Optional[List[AssistantTool]] = None,
    retrievals: Optional[List[AssistantRetrieval]] = None,
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
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The updated assistant object.
    """

    api_instance = get_api_instance(ModuleType.ASSISTANT)
    body = AssistantUpdateRequest(
        model_id=model_id,
        name=name,
        description=description,
        system_prompt_template=system_prompt_template,
        memory=memory,
        tools=tools,
        retrievals=retrievals,
        metadata=metadata,
    )
    response: AssistantUpdateResponse = api_instance.update_assistant(assistant_id=assistant_id, body=body)
    assistant: Assistant = Assistant(**response.data)
    return assistant


async def a_update_assistant(
    assistant_id: str,
    model_id: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    system_prompt_template: Optional[List[str]] = None,
    memory: Optional[AssistantMemory] = None,
    tools: Optional[List[AssistantTool]] = None,
    retrievals: Optional[List[AssistantRetrieval]] = None,
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
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The updated assistant object.
    """

    api_instance = get_api_instance(ModuleType.ASSISTANT, async_client=True)
    body = AssistantUpdateRequest(
        model_id=model_id,
        name=name,
        description=description,
        system_prompt_template=system_prompt_template,
        memory=memory,
        tools=tools,
        retrievals=retrievals,
        metadata=metadata,
    )
    response: AssistantUpdateResponse = await api_instance.update_assistant(assistant_id=assistant_id, body=body)
    assistant: Assistant = Assistant(**response.data)
    return assistant


def delete_assistant(assistant_id: str) -> None:
    """
    Delete an assistant.

    :param assistant_id: The ID of the assistant.
    """

    api_instance = get_api_instance(ModuleType.ASSISTANT)
    api_instance.delete_assistant(assistant_id=assistant_id)


async def a_delete_assistant(assistant_id: str) -> None:
    """
    Delete an assistant in async mode.

    :param assistant_id: The ID of the assistant.
    """

    api_instance = get_api_instance(ModuleType.ASSISTANT, async_client=True)
    await api_instance.delete_assistant(assistant_id=assistant_id)

