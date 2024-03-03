import inspect
import logging
import httpx
from taskingai.client.api_client import SyncApiClient, AsyncApiClient
from enum import Enum


def check_kwargs(caller, given):
    argspec = inspect.getfullargspec(caller)
    diff = set(given).difference(argspec.args)
    if diff:
        logging.exception(caller.__name__ + " had unexpected keyword argument(s): " + ", ".join(diff), exc_info=False)


def get_version():
    from taskingai import __version__

    return __version__


def get_user_agent():
    client_id = f"python-client-{get_version()}"
    user_agent_details = {"httpx": httpx.__version__}
    user_agent = "{} ({})".format(client_id, ", ".join([f"{k}:{v}" for k, v in user_agent_details.items()]))
    return user_agent


def convert_query_params_dict(query_params_dict):
    """
    This helper function will convert the query_params_dict to a format where enum values are converted to their
    corresponding string values.
    """
    converted_dict = {}
    for key, value in query_params_dict.items():
        if isinstance(value, Enum):
            converted_dict[key] = value.value
        elif isinstance(value, bool):
            converted_dict[key] = str(value).lower()
        elif value is not None:
            converted_dict[key] = value
    return converted_dict


__sync_api_client = None
__async_api_client = None


def get_api_client(async_client: bool):
    global __sync_api_client, __async_api_client

    from taskingai.config import Config

    client_config = Config.OPENAPI_CONFIG
    client_config.api_key = client_config.api_key or {}

    if async_client:
        if not __async_api_client:
            __async_api_client = AsyncApiClient(configuration=client_config)
            __async_api_client.user_agent = get_user_agent()
        return __async_api_client

    else:
        if not __sync_api_client:
            __sync_api_client = SyncApiClient(configuration=client_config)
            __sync_api_client.user_agent = get_user_agent()
        return __sync_api_client
