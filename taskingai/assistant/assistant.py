from typing import Optional, List, Dict

from taskingai.client.utils import get_assistant_api_instance
from taskingai.client.models import Assistant, AssistantRetrieval, AssistantTool
from taskingai.client.models import AssistantCreateRequest, AssistantCreateResponse,\
    AssistantUpdateRequest, AssistantUpdateResponse,\
    AssistantGetResponse, AssistantListResponse

__all__ = [
    "Assistant",
    "get_assistant",
    "list_assistants",
    "create_assistant",
    "update_assistant",
    "delete_assistant",
]


def list_assistants(
    order: str = "desc",
    limit: int = 20,
    offset: Optional[int] = None,
    after: Optional[str] = None,
    before: Optional[str] = None,
) -> List[Assistant]:

    """
    List assistants.

    :param order: The order of the assistants. It can be "asc" or "desc".
    :param limit: The maximum number of assistants to return.
    :param offset: The offset of the assistants.
    :param after: The cursor to get the next page of assistants.
    :param before: The cursor to get the previous page of assistants.
    :return: The list of assistants.
    """
    # todo: verify only one of offset, after and before is not None
    api_instance = get_assistant_api_instance()
    # only add non-None parameters
    params = {
        "order": order,
        "limit": limit,
        "offset": offset,
        "after": after,
        "before": before,
    }
    params = {k: v for k, v in params.items() if v is not None}
    response: AssistantListResponse = api_instance.list_assistants(**params)
    assistants: List[Assistant] = [Assistant(**item) for item in response.data]
    return assistants



def get_assistant(assistant_id: str) -> Assistant:
    """
    Get an assistant.

    :param assistant_id: The ID of the assistant.
    """

    api_instance = get_assistant_api_instance()
    response: AssistantGetResponse = api_instance.get_assistant(assistant_id=assistant_id)
    assistant: Assistant = Assistant(**response.data)
    return assistant


def create_assistant(
    model_id: str,
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
    :param name: The assistant name.
    :param description: The assistant description.
    :param system_prompt_template: A list of system prompt chunks where prompt variables are wrapped by curly brackets, e.g. {{variable}}.
    :param tools: The assistant tools.
    :param retrievals: The assistant retrievals.
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The created assistant object.
    """

    api_instance = get_assistant_api_instance()
    body = AssistantCreateRequest(
        model_id=model_id,
        name=name,
        description=description,
        system_prompt_template=system_prompt_template,
        tools=tools,
        retrievals=retrievals,
        metadata=metadata,
    )
    response: AssistantCreateResponse = api_instance.create_assistant(body=body)
    assistant: Assistant = Assistant(**response.data)
    return assistant


def update_assistant(
    assistant_id: str,
    model_id: Optional[str] = None,
    name: Optional[str] = None,
    description: Optional[str] = None,
    system_prompt_template: Optional[List[str]] = None,
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
    :param tools: The assistant tools.
    :param retrievals: The assistant retrievals.
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The updated assistant object.
    """

    api_instance = get_assistant_api_instance()
    body = AssistantUpdateRequest(
        model_id=model_id,
        name=name,
        description=description,
        system_prompt_template=system_prompt_template,
        tools=tools,
        retrievals=retrievals,
        metadata=metadata,
    )
    response: AssistantUpdateResponse = api_instance.update_assistant(assistant_id=assistant_id, body=body)
    assistant: Assistant = Assistant(**response.data)
    return assistant


def delete_assistant(assistant_id: str) -> None:
    """
    Delete an assistant.

    :param assistant_id: The ID of the assistant.
    """

    api_instance = get_assistant_api_instance()
    api_instance.delete_assistant(assistant_id=assistant_id)

