# -*- coding: utf-8 -*-

# api_generate_message.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from ..utils import get_api_client
from ..models import MessageGenerateRequest, MessageGenerateResponse

__all__ = ["api_generate_message", "async_api_generate_message"]


def api_generate_message(
    assistant_id: str,
    chat_id: str,
    payload: MessageGenerateRequest,
    **kwargs,
) -> MessageGenerateResponse:
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
        response_type=MessageGenerateResponse,
        auth_settings=[],
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=kwargs.get("timeout"),
        collection_formats={},
    )


async def async_api_generate_message(
    assistant_id: str,
    chat_id: str,
    payload: MessageGenerateRequest,
    **kwargs,
) -> MessageGenerateResponse:
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
        response_type=MessageGenerateResponse,
        auth_settings=[],
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=kwargs.get("timeout"),
        collection_formats={},
    )
