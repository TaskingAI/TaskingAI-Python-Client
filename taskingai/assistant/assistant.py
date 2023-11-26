import time
from typing import NamedTuple, Optional, List

from taskingai.config import Config
from taskingai.client.utils import get_user_agent
from taskingai.client.api.assistant_api import AssistantApi
from taskingai.client.api_client import ApiClient
from taskingai.client.models import Assistant, AssistantRetrieval, AssistantTool
from taskingai.client.models import AssistantCreateRequest, AssistantCreateResponse,\
    AssistantUpdateRequest, AssistantUpdateResponse,\
    AssistantGetResponse, AssistantListResponse, AssistantDeleteResponse

__all__ = [
    "create_assistant",
]

def _get_api_instance():
    client_config = Config.OPENAPI_CONFIG
    client_config.api_key = client_config.api_key or {}
    api_client = ApiClient(configuration=client_config)
    api_client.user_agent = get_user_agent()
    api_instance = AssistantApi(api_client)
    return api_instance


def create_assistant(
    model_id: str,
    name: Optional[str] = None,
    description: Optional[str] = None,
    system_prompt_template: Optional[List[str]] = None,
    tools: Optional[List[AssistantTool]] = None,
    retrievals: Optional[List[AssistantRetrieval]] = None,
    metadata: Optional[dict] = None,
) -> Assistant:
    """Create an assistant.
    
    :param model_id: The ID of an available chat completion model in your project.
    :param name: The assistant name.
    :param description: The assistant description.
    :param system_prompt_template: A list of system prompt chunks where prompt variables are wrapped by curly brackets, e.g. {{variable}}.
    :param tools: The assistant tools.
    :param retrievals: The assistant retrievals.
    :param metadata: The assistant metadata. It can store up to 16 key-value pairs where each key's length is less than 64 and value's length is less than 512.
    :return: The assistant object.
    """

    api_instance = _get_api_instance()
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