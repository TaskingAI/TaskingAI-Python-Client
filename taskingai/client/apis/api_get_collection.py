# -*- coding: utf-8 -*-

# api_get_collection.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
Created: 03-Mar-2024
License: Apache 2.0
"""

from ..utils import get_api_client
from ..models import CollectionGetResponse

__all__ = ["api_get_collection", "async_api_get_collection"]


def api_get_collection(collection_id: str, **kwargs) -> CollectionGetResponse:
    # get api client
    sync_api_client = get_api_client(async_client=False)

    # request parameters
    path_params_dict = {
        "collection_id": collection_id,
    }
    query_params_dict = {}
    header_params_dict = {"Accept": sync_api_client.select_header_accept(["application/json"])}
    body_params_dict = {}
    files_dict = {}

    # execute the request
    return sync_api_client.call_api(
        resource_path="/v1/collections/{collection_id}",
        method="GET",
        path_params=path_params_dict,
        query_params=query_params_dict,
        header_params=header_params_dict,
        body=body_params_dict,
        post_params=[],
        files=files_dict,
        response_type=CollectionGetResponse,
        auth_settings=[],
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=kwargs.get("timeout"),
        collection_formats={},
    )


async def async_api_get_collection(collection_id: str, **kwargs) -> CollectionGetResponse:
    # get api client
    async_api_client = get_api_client(async_client=True)

    # request parameters
    path_params_dict = {
        "collection_id": collection_id,
    }
    query_params_dict = {}
    header_params_dict = {"Accept": async_api_client.select_header_accept(["application/json"])}
    body_params_dict = {}
    files_dict = {}

    # execute the request
    return await async_api_client.call_api(
        resource_path="/v1/collections/{collection_id}",
        method="GET",
        path_params=path_params_dict,
        query_params=query_params_dict,
        header_params=header_params_dict,
        body=body_params_dict,
        post_params=[],
        files=files_dict,
        response_type=CollectionGetResponse,
        auth_settings=[],
        _return_http_data_only=True,
        _preload_content=True,
        _request_timeout=kwargs.get("timeout"),
        collection_formats={},
    )
