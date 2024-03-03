# -*- coding: utf-8 -*-

# api_list_chunks.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from ..utils import get_api_client, convert_query_params_dict
from ..models import ChunkListRequest, ChunkListResponse

__all__ = ["api_list_chunks", "async_api_list_chunks"]


def api_list_chunks(collection_id: str, payload: ChunkListRequest, **kwargs) -> ChunkListResponse:
    # get api client
    sync_api_client = get_api_client(async_client=False)

    # request parameters
    path_params_dict = {
        "collection_id": collection_id,
    }
    query_params_dict = convert_query_params_dict(payload.model_dump())
    header_params_dict = {"Accept": sync_api_client.select_header_accept(["application/json"])}
    body_params_dict = {}
    files_dict = {}

    # execute the request
    return sync_api_client.call_api(
        resource_path="/v1/collections/{collection_id}/chunks",
        method="GET",
        path_params=path_params_dict,
        query_params=query_params_dict,
        header_params=header_params_dict,
        body=body_params_dict,
        post_params=[],
        files=files_dict,
        response_type=ChunkListResponse,
        auth_settings=[],
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=kwargs.get("timeout"),
        collection_formats={},
    )


async def async_api_list_chunks(collection_id: str, payload: ChunkListRequest, **kwargs) -> ChunkListResponse:
    # get api client
    async_api_client = get_api_client(async_client=True)

    # request parameters
    path_params_dict = {
        "collection_id": collection_id,
    }
    query_params_dict = convert_query_params_dict(payload.model_dump())
    header_params_dict = {"Accept": async_api_client.select_header_accept(["application/json"])}
    body_params_dict = {}
    files_dict = {}

    # execute the request
    return await async_api_client.call_api(
        resource_path="/v1/collections/{collection_id}/chunks",
        method="GET",
        path_params=path_params_dict,
        query_params=query_params_dict,
        header_params=header_params_dict,
        body=body_params_dict,
        post_params=[],
        files=files_dict,
        response_type=ChunkListResponse,
        auth_settings=[],
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=kwargs.get("timeout"),
        collection_formats={},
    )
