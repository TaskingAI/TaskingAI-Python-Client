# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from ..api_client import SyncApiClient
from ..stream import Stream
from ..models import INFERENCE_CHAT_COMPLETION_STREAM_CAST_MAP

class InferenceApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = SyncApiClient()
        self.api_client = api_client

    def chat_completion(self, body, stream = False, **kwargs):  # noqa: E501
        """Chat Completion  # noqa: E501

        Model inference for chat completion.  # noqa: E501
        :param ChatCompletionRequest body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        cast_map = INFERENCE_CHAT_COMPLETION_STREAM_CAST_MAP
        response = self.chat_completion_with_http_info(body, stream, **kwargs)
        if not stream:
            return response
        else:
            return Stream(
                cast_map=cast_map,
                response=response,
                client=self.api_client
            )

    def chat_completion_with_http_info(self, body, stream, **kwargs):  # noqa: E501
        """Chat Completion  # noqa: E501

        Model inference for chat completion.  # noqa: E501
        :param ChatCompletionRequest body: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method chat_completion" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `chat_completion`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        response = self.api_client.call_api(
            '/v1/inference/chat_completion', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='object',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats,
            stream=stream
        )
        return response

    def text_embedding(self, body, **kwargs):  # noqa: E501
        """Text Embedding  # noqa: E501

        Model inference for text embedding.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.text_embedding(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TextEmbeddingRequest body: (required)
        :return: TextEmbeddingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        (data) = self.text_embedding_with_http_info(body, **kwargs)  # noqa: E501
        return data

    def text_embedding_with_http_info(self, body, **kwargs):  # noqa: E501
        """Text Embedding  # noqa: E501

        Model inference for text embedding.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.text_embedding_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param TextEmbeddingRequest body: (required)
        :return: TextEmbeddingResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method text_embedding" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `text_embedding`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'body' in params:
            body_params = params['body']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/v1/inference/text_embedding', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TextEmbeddingResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
