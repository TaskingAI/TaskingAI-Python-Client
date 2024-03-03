# -*- coding: utf-8 -*-

# api_run_action.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from ..utils import get_api_client
from ..models import ActionRunRequest, ActionRunResponse

__all__ = ["api_run_action", "async_api_run_action"]


def api_run_action(action_id: str, payload: ActionRunRequest, **kwargs) -> ActionRunResponse:
    # get api client
    sync_api_client = get_api_client(async_client=False)

    # request parameters
    path_params_dict = {
        "action_id": action_id,
    }
    query_params_dict = {}
    header_params_dict = {"Accept": sync_api_client.select_header_accept(["application/json"])}
    body_params_dict = payload.model_dump()
    files_dict = {}

    # execute the request
    return sync_api_client.call_api(
        resource_path="/v1/actions/{action_id}/run",
        method="POST",
        path_params=path_params_dict,
        query_params=query_params_dict,
        header_params=header_params_dict,
        body=body_params_dict,
        post_params=[],
        files=files_dict,
        response_type=ActionRunResponse,
        auth_settings=[],
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=kwargs.get("timeout"),
        collection_formats={},
    )


async def async_api_run_action(action_id: str, payload: ActionRunRequest, **kwargs) -> ActionRunResponse:
    # get api client
    async_api_client = get_api_client(async_client=True)

    # request parameters
    path_params_dict = {
        "action_id": action_id,
    }
    query_params_dict = {}
    header_params_dict = {"Accept": async_api_client.select_header_accept(["application/json"])}
    body_params_dict = payload.model_dump()
    files_dict = {}

    # execute the request
    return await async_api_client.call_api(
        resource_path="/v1/actions/{action_id}/run",
        method="POST",
        path_params=path_params_dict,
        query_params=query_params_dict,
        header_params=header_params_dict,
        body=body_params_dict,
        post_params=[],
        files=files_dict,
        response_type=ActionRunResponse,
        auth_settings=[],
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=kwargs.get("timeout"),
        collection_formats={},
    )
