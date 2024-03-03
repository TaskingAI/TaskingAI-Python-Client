# -*- coding: utf-8 -*-

# stream_api_chat_completion.py

"""
Stream API for chat completion

Author: James Yao
Organization: TaskingAI
Created: 02-Mar-2024
License: Apache 2.0
"""

from ..utils import get_api_client
from taskingai.client.stream import Stream, AsyncStream
from ..models import ChatCompletionRequest

__all__ = ["stream_api_chat_completion", "async_stream_api_chat_completion"]


def stream_api_chat_completion(payload: ChatCompletionRequest, **kwargs) -> Stream:
    # get api client
    sync_api_client = get_api_client(async_client=False)

    # request parameters
    path_params_dict = {}
    query_params_dict = {}
    header_params_dict = {"Accept": sync_api_client.select_header_accept(["application/json"])}
    body_params_dict = payload.model_dump()
    files_dict = {}

    # execute the request
    return sync_api_client.call_api(
        resource_path="/v1/inference/chat_completion",
        method="POST",
        path_params=path_params_dict,
        query_params=query_params_dict,
        header_params=header_params_dict,
        body=body_params_dict,
        post_params=[],
        files=files_dict,
        response_type=None,
        auth_settings=[],
        _return_http_data_only=None,
        _preload_content=None,
        _request_timeout=kwargs.get("timeout"),
        collection_formats={},
        stream=True,
    )


async def async_stream_api_chat_completion(payload: ChatCompletionRequest, **kwargs) -> AsyncStream:
    # get api client
    async_api_client = get_api_client(async_client=True)

    # request parameters
    path_params_dict = {}
    query_params_dict = {}
    header_params_dict = {"Accept": async_api_client.select_header_accept(["application/json"])}
    body_params_dict = payload.model_dump()
    files_dict = {}

    # execute the request
    return await async_api_client.call_api(
        resource_path="/v1/inference/chat_completion",
        method="POST",
        path_params=path_params_dict,
        query_params=query_params_dict,
        header_params=header_params_dict,
        body=body_params_dict,
        post_params=[],
        files=files_dict,
        response_type=None,
        auth_settings=[],
        _return_http_data_only=None,
        _preload_content=None,
        _request_timeout=kwargs.get("timeout"),
        collection_formats={},
        stream=True,
    )
