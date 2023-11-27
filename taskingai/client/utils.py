import inspect
import logging
from pathlib import Path
import urllib3
from taskingai.config import Config
from taskingai.client.api import AssistantApi, ToolApi, RetrievalApi, InferenceApi
from taskingai.client.api_client import ApiClient

def check_kwargs(caller, given):
    argspec = inspect.getfullargspec(caller)
    diff = set(given).difference(argspec.args)
    if diff:
        logging.exception(caller.__name__ + ' had unexpected keyword argument(s): ' + ', '.join(diff), exc_info=False)


def get_version():
    return Path(__file__).parent.parent.joinpath('__version__').read_text().strip()


def get_user_agent():
    client_id = f'python-client-{get_version()}'
    user_agent_details = {'urllib3': urllib3.__version__}
    user_agent = '{} ({})'.format(client_id, ', '.join([f'{k}:{v}' for k, v in user_agent_details.items()]))
    return user_agent


def get_assistant_api_instance():
    client_config = Config.OPENAPI_CONFIG
    client_config.api_key = client_config.api_key or {}
    api_client = ApiClient(configuration=client_config)
    api_client.user_agent = get_user_agent()
    api_instance = AssistantApi(api_client)
    return api_instance


def get_tool_api_instance():
    client_config = Config.OPENAPI_CONFIG
    client_config.api_key = client_config.api_key or {}
    api_client = ApiClient(configuration=client_config)
    api_client.user_agent = get_user_agent()
    api_instance = ToolApi(api_client)
    return api_instance


def get_retrieval_api_instance():
    client_config = Config.OPENAPI_CONFIG
    client_config.api_key = client_config.api_key or {}
    api_client = ApiClient(configuration=client_config)
    api_client.user_agent = get_user_agent()
    api_instance = RetrievalApi(api_client)
    return api_instance


def get_inference_api_instance():
    client_config = Config.OPENAPI_CONFIG
    client_config.api_key = client_config.api_key or {}
    api_client = ApiClient(configuration=client_config)
    api_client.user_agent = get_user_agent()
    api_instance = InferenceApi(api_client)
    return api_instance