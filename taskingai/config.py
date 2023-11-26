import logging
import sys
from typing import NamedTuple, List
import os

import certifi

from taskingai.client.utils import check_kwargs
from taskingai.client.exceptions import ApiKeyError
from taskingai.client.constants import PARENT_LOGGER_NAME, DEFAULT_PARENT_LOGGER_LEVEL
from taskingai.client.configuration import Configuration as OpenApiConfiguration

__all__ = ["Config", "init"]

_logger = logging.getLogger(__name__)
_parent_logger = logging.getLogger(PARENT_LOGGER_NAME)
_parent_logger.setLevel(DEFAULT_PARENT_LOGGER_LEVEL)


class ConfigBase(NamedTuple):
    # todo add more project information
    api_key: str = ""
    host: str = ""
    openapi_config: OpenApiConfiguration = None


class _CONFIG:
    """

    Order of configs to load:

    - configs specified explicitly in reset
    - environment variables
    - configs specified in the INI file
    - default configs
    """

    def __init__(self):
        self.reset()

    def validate(self):
        if not self._config.api_key:  # None or empty string invalid
            raise ApiKeyError("You haven't specified an Api-Key.")

    def reset(self, **kwargs):
        config = ConfigBase()

        # Get from kwargs first, then environment variables, then default
        api_key = (
            kwargs.pop("api_key", None) or os.getenv("TASKINGAI_API_KEY")
        )
        host = (
            kwargs.pop("host", None) or os.getenv("TASKINGAI_HOST") or "https://api.tasking.ai"
        )
        config = config._replace(api_key=api_key, host=host)

        # Set explicit config
        # config = config._replace(**self._preprocess_and_validate_config(kwargs))

        self._config = config

        # Set OpenAPI client config
        openapi_config = OpenApiConfiguration()
        openapi_config.ssl_ca_cert = certifi.where()
        openapi_config.api_key = config.api_key
        openapi_config.host = config.host

        config = config._replace(openapi_config=openapi_config)
        self._config = config

    def _preprocess_and_validate_config(self, config: dict) -> dict:
        """Normalize, filter, and validate config keys/values.

        Trims whitespace, removes invalid keys,
        and raises ValueError in case an invalid value was specified.
        """
        # general preprocessing and filtering
        result = {k: v for k, v in config.items() if k in ConfigBase._fields if v is not None}
        return result

    @property
    def API_KEY(self):
        return self._config.api_key

    @property
    def HOST(self):
        return self._config.host

    @property
    def OPENAPI_CONFIG(self):
        return self._config.openapi_config


def init(
    api_key: str = None,
    host: str = None,
    **kwargs
):
    """Initializes the TaskingAI client.

    :param api_key: Required if not set in config file or by environment variable ``TASKINGAI_API_KEY``.
    :param host: Optional. TaskingAI server host. Default: ``https://api.tasking.ai``.
    :param openapi_config: Optional. Set OpenAPI client configuration.
    """
    check_kwargs(init, kwargs)
    Config.reset(
        api_key=api_key,
        host=host,
        **kwargs
    )


Config = _CONFIG()

# Init
init()