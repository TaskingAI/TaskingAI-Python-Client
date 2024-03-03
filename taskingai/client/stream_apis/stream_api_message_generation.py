# -*- coding: utf-8 -*-

# api_generate_message.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 02-Mar-2024
License: Apache 2.0
"""

from ..utils import get_api_client
from taskingai.client.stream import Stream, AsyncStream
from ..models import MessageGenerateRequest

__all__ = ["stream_api_generate_message", "async_stream_api_generate_message"]


def stream_api_generate_message(assistant_id: str, chat_id: str, payload: MessageGenerateRequest, **kwargs) -> Stream:
    # get api client
    sync_api_client = get_api_client(async_client=False)

    # request parameters
    path_params_dict = {
        "assistant_id": assistant_id,
        "chat_id": chat_id,
    }
    query_params_dict = {}
    header_params_dict = {"Accept": sync_api_client.select_header_accept(["application/json"])}
    body_params_dict = payload.model_dump()
    files_dict = {}

    # execute the request
    return sync_api_client.call_api(
        resource_path="/v1/assistants/{assistant_id}/chats/{chat_id}/generate",
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


async def async_stream_api_generate_message(
    assistant_id: str, chat_id: str, payload: MessageGenerateRequest, **kwargs
) -> AsyncStream:
    # get api client
    async_api_client = get_api_client(async_client=True)

    # request parameters
    path_params_dict = {
        "assistant_id": assistant_id,
        "chat_id": chat_id,
    }
    query_params_dict = {}
    header_params_dict = {"Accept": async_api_client.select_header_accept(["application/json"])}
    body_params_dict = payload.model_dump()
    files_dict = {}

    # execute the request
    return await async_api_client.call_api(
        resource_path="/v1/assistants/{assistant_id}/chats/{chat_id}/generate",
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
