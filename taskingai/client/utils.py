import inspect
import logging
from pathlib import Path
import httpx
from taskingai.client.api import *
from taskingai.client.api_client import SyncApiClient, AsyncApiClient
from .constants import ModuleType

def check_kwargs(caller, given):
    argspec = inspect.getfullargspec(caller)
    diff = set(given).difference(argspec.args)
    if diff:
        logging.exception(caller.__name__ + ' had unexpected keyword argument(s): ' + ', '.join(diff), exc_info=False)


def get_version():
    from taskingai import __version__
    return __version__


def get_user_agent():
    client_id = f'python-client-{get_version()}'
    user_agent_details = {'httpx': httpx.__version__}
    user_agent = '{} ({})'.format(client_id, ', '.join([f'{k}:{v}' for k, v in user_agent_details.items()]))
    return user_agent

sync_api_instance_dict = {
    ModuleType.assistant: None,
    ModuleType.tool: None,
    ModuleType.retrieval: None,
    ModuleType.inference: None
}

async_api_instance_dict = {
    ModuleType.assistant: None,
    ModuleType.tool: None,
    ModuleType.retrieval: None,
    ModuleType.inference: None
}

def get_api_instance(module: ModuleType, async_client=False):
    from taskingai.config import Config
    client_config = Config.OPENAPI_CONFIG
    client_config.api_key = client_config.api_key or {}

    api_instance = None

    if async_client:
        api_client = AsyncApiClient(configuration=client_config)
        api_client.user_agent = get_user_agent()

        if async_api_instance_dict.get(module) is None:
            if module == ModuleType.assistant:
                async_api_instance_dict[module] = AsyncAssistantApi(api_client)
            elif module == ModuleType.tool:
                async_api_instance_dict[module] = AsyncToolApi(api_client)
            elif module == ModuleType.retrieval:
                async_api_instance_dict[module] = AsyncRetrievalApi(api_client)
            elif module == ModuleType.inference:
                async_api_instance_dict[module] = AsyncInferenceApi(api_client)

        api_instance = async_api_instance_dict[module]

    else:
        api_client = SyncApiClient(configuration=client_config)
        api_client.user_agent = get_user_agent()

        if sync_api_instance_dict.get(module) is None:

            if module == ModuleType.assistant:
                sync_api_instance_dict[module] = AssistantApi(api_client)
            elif module == ModuleType.tool:
                sync_api_instance_dict[module] = ToolApi(api_client)
            elif module == ModuleType.retrieval:
                sync_api_instance_dict[module] = RetrievalApi(api_client)
            elif module == ModuleType.inference:
                sync_api_instance_dict[module] = InferenceApi(api_client)

        api_instance = sync_api_instance_dict[module]

    if api_instance is None:
        raise NotImplementedError(f"Cannot find api instance for module {module} with async={async_client}")

    return api_instance
