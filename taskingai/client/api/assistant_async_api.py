# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from taskingai.client.api_client import AsyncApiClient


class AsyncAssistantApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = AsyncApiClient()
        self.api_client = api_client

    async def create_assistant(self, body, **kwargs):  # noqa: E501
        """Create assistant  # noqa: E501

        Create an assistant with a model and instructions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_assistant(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AssistantCreateRequest body: (required)
        :return: AssistantCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.create_assistant_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = await self.create_assistant_with_http_info(body, **kwargs)  # noqa: E501
            return data

    async def create_assistant_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create assistant  # noqa: E501

        Create an assistant with a model and instructions.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_assistant_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AssistantCreateRequest body: (required)
        :return: AssistantCreateResponse
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
                    " to method create_assistant" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_assistant`")  # noqa: E501

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

        return await self.api_client.call_api(
            '/v1/assistants', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssistantCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def create_chat(self, body, assistant_id, **kwargs):  # noqa: E501
        """Create chat  # noqa: E501

        Create a new chat within your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_chat(body, assistant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChatCreateRequest body: (required)
        :param object assistant_id: (required)
        :return: ChatCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.create_chat_with_http_info(body, assistant_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.create_chat_with_http_info(body, assistant_id, **kwargs)  # noqa: E501
            return data

    async def create_chat_with_http_info(self, body, assistant_id, **kwargs):  # noqa: E501
        """Create chat  # noqa: E501

        Create a new chat within your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_chat_with_http_info(body, assistant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChatCreateRequest body: (required)
        :param object assistant_id: (required)
        :return: ChatCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'assistant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_chat" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_chat`")  # noqa: E501
        # verify the required parameter 'assistant_id' is set
        if ('assistant_id' not in params or
                params['assistant_id'] is None):
            raise ValueError("Missing the required parameter `assistant_id` when calling `create_chat`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assistant_id' in params:
            path_params['assistant_id'] = params['assistant_id']  # noqa: E501

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

        return await self.api_client.call_api(
            '/v1/assistants/{assistant_id}/chats', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChatCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def create_message(self, body, assistant_id, chat_id, **kwargs):  # noqa: E501
        """Create message  # noqa: E501

        Send a new message within a specific chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_message(body, assistant_id, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessageCreateRequest body: (required)
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :return: MessageCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.create_message_with_http_info(body, assistant_id, chat_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.create_message_with_http_info(body, assistant_id, chat_id, **kwargs)  # noqa: E501
            return data

    async def create_message_with_http_info(self, body, assistant_id, chat_id, **kwargs):  # noqa: E501
        """Create message  # noqa: E501

        Send a new message within a specific chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_message_with_http_info(body, assistant_id, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessageCreateRequest body: (required)
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :return: MessageCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'assistant_id', 'chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_message`")  # noqa: E501
        # verify the required parameter 'assistant_id' is set
        if ('assistant_id' not in params or
                params['assistant_id'] is None):
            raise ValueError(
                "Missing the required parameter `assistant_id` when calling `create_message`")  # noqa: E501
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in params or
                params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `create_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assistant_id' in params:
            path_params['assistant_id'] = params['assistant_id']  # noqa: E501
        if 'chat_id' in params:
            path_params['chat_id'] = params['chat_id']  # noqa: E501

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

        return await self.api_client.call_api(
            '/v1/assistants/{assistant_id}/chats/{chat_id}/messages', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MessageCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def delete_assistant(self, assistant_id, **kwargs):  # noqa: E501
        """Delete assistant  # noqa: E501

        Remove an existing assistant from your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_assistant(assistant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :return: AssistantDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.delete_assistant_with_http_info(assistant_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.delete_assistant_with_http_info(assistant_id, **kwargs)  # noqa: E501
            return data

    async def delete_assistant_with_http_info(self, assistant_id, **kwargs):  # noqa: E501
        """Delete assistant  # noqa: E501

        Remove an existing assistant from your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_assistant_with_http_info(assistant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :return: AssistantDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assistant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_assistant" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assistant_id' is set
        if ('assistant_id' not in params or
                params['assistant_id'] is None):
            raise ValueError(
                "Missing the required parameter `assistant_id` when calling `delete_assistant`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assistant_id' in params:
            path_params['assistant_id'] = params['assistant_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return await self.api_client.call_api(
            '/v1/assistants/{assistant_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssistantDeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def delete_chat(self, assistant_id, chat_id, **kwargs):  # noqa: E501
        """Delete chat  # noqa: E501

        Remove an existing chat from your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_chat(assistant_id, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :return: ChatDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.delete_chat_with_http_info(assistant_id, chat_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.delete_chat_with_http_info(assistant_id, chat_id, **kwargs)  # noqa: E501
            return data

    async def delete_chat_with_http_info(self, assistant_id, chat_id, **kwargs):  # noqa: E501
        """Delete chat  # noqa: E501

        Remove an existing chat from your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_chat_with_http_info(assistant_id, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :return: ChatDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assistant_id', 'chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_chat" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assistant_id' is set
        if ('assistant_id' not in params or
                params['assistant_id'] is None):
            raise ValueError("Missing the required parameter `assistant_id` when calling `delete_chat`")  # noqa: E501
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in params or
                params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `delete_chat`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assistant_id' in params:
            path_params['assistant_id'] = params['assistant_id']  # noqa: E501
        if 'chat_id' in params:
            path_params['chat_id'] = params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return await self.api_client.call_api(
            '/v1/assistants/{assistant_id}/chats/{chat_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChatDeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)


    async def generate_message(self, body, stream, assistant_id, chat_id, **kwargs):  # noqa: E501
        """Generate assistant message  # noqa: E501

        Generate a new message with the role of 'assistant'.
        :param MessageGenerateRequest body: (required)
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        return await self.generate_message_with_http_info(body, stream, assistant_id, chat_id, **kwargs)  # noqa: E501


    async def generate_message_with_http_info(self, body, stream, assistant_id, chat_id, **kwargs):  # noqa: E501
        """Generate assistant message  # noqa: E501

        Generate a new message with the role of 'assistant'.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_message_with_http_info(body, assistant_id, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessageGenerateRequest body: (required)
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :return: object
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'assistant_id', 'chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError(
                "Missing the required parameter `body` when calling `generate_message`")  # noqa: E501
        # verify the required parameter 'assistant_id' is set
        if ('assistant_id' not in params or
                params['assistant_id'] is None):
            raise ValueError(
                "Missing the required parameter `assistant_id` when calling `generate_message`")  # noqa: E501
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in params or
                params['chat_id'] is None):
            raise ValueError(
                "Missing the required parameter `chat_id` when calling `generate_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assistant_id' in params:
            path_params['assistant_id'] = params['assistant_id']  # noqa: E501
        if 'chat_id' in params:
            path_params['chat_id'] = params['chat_id']  # noqa: E501

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

        return await self.api_client.call_api(
            '/v1/assistants/{assistant_id}/chats/{chat_id}/generate', 'POST',
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

    async def get_assistant(self, assistant_id, **kwargs):  # noqa: E501
        """Get assistant  # noqa: E501

        Retrieve a single assistant by its unique ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_assistant(assistant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :return: AssistantGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.get_assistant_with_http_info(assistant_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.get_assistant_with_http_info(assistant_id, **kwargs)  # noqa: E501
            return data

    async def get_assistant_with_http_info(self, assistant_id, **kwargs):  # noqa: E501
        """Get assistant  # noqa: E501

        Retrieve a single assistant by its unique ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_assistant_with_http_info(assistant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :return: AssistantGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assistant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_assistant" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assistant_id' is set
        if ('assistant_id' not in params or
                params['assistant_id'] is None):
            raise ValueError("Missing the required parameter `assistant_id` when calling `get_assistant`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assistant_id' in params:
            path_params['assistant_id'] = params['assistant_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return await self.api_client.call_api(
            '/v1/assistants/{assistant_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssistantGetResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def get_chat(self, assistant_id, chat_id, **kwargs):  # noqa: E501
        """Get chat  # noqa: E501

        Retrieve the details of a specific chat by its unique ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chat(assistant_id, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :return: ChatGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.get_chat_with_http_info(assistant_id, chat_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.get_chat_with_http_info(assistant_id, chat_id, **kwargs)  # noqa: E501
            return data

    async def get_chat_with_http_info(self, assistant_id, chat_id, **kwargs):  # noqa: E501
        """Get chat  # noqa: E501

        Retrieve the details of a specific chat by its unique ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_chat_with_http_info(assistant_id, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :return: ChatGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assistant_id', 'chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_chat" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assistant_id' is set
        if ('assistant_id' not in params or
                params['assistant_id'] is None):
            raise ValueError("Missing the required parameter `assistant_id` when calling `get_chat`")  # noqa: E501
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in params or
                params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `get_chat`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assistant_id' in params:
            path_params['assistant_id'] = params['assistant_id']  # noqa: E501
        if 'chat_id' in params:
            path_params['chat_id'] = params['chat_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return await self.api_client.call_api(
            '/v1/assistants/{assistant_id}/chats/{chat_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChatGetResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def get_message(self, assistant_id, chat_id, message_id, **kwargs):  # noqa: E501
        """Get message  # noqa: E501

        Retrieve a specific message from a chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_message(assistant_id, chat_id, message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :param object message_id: (required)
        :return: MessageGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.get_message_with_http_info(assistant_id, chat_id, message_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.get_message_with_http_info(assistant_id, chat_id, message_id, **kwargs)  # noqa: E501
            return data

    async def get_message_with_http_info(self, assistant_id, chat_id, message_id, **kwargs):  # noqa: E501
        """Get message  # noqa: E501

        Retrieve a specific message from a chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_message_with_http_info(assistant_id, chat_id, message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :param object message_id: (required)
        :return: MessageGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assistant_id', 'chat_id', 'message_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assistant_id' is set
        if ('assistant_id' not in params or
                params['assistant_id'] is None):
            raise ValueError("Missing the required parameter `assistant_id` when calling `get_message`")  # noqa: E501
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in params or
                params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `get_message`")  # noqa: E501
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params or
                params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `get_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assistant_id' in params:
            path_params['assistant_id'] = params['assistant_id']  # noqa: E501
        if 'chat_id' in params:
            path_params['chat_id'] = params['chat_id']  # noqa: E501
        if 'message_id' in params:
            path_params['message_id'] = params['message_id']  # noqa: E501

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return await self.api_client.call_api(
            '/v1/assistants/{assistant_id}/chats/{chat_id}/messages/{message_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MessageGetResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def list_assistants(self, **kwargs):  # noqa: E501
        """List assistants  # noqa: E501

        Retrieve a list of all assistants available in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_assistants(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :return: AssistantListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.list_assistants_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = await self.list_assistants_with_http_info(**kwargs)  # noqa: E501
            return data

    async def list_assistants_with_http_info(self, **kwargs):  # noqa: E501
        """List assistants  # noqa: E501

        Retrieve a list of all assistants available in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_assistants_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :return: AssistantListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'order', 'after', 'before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_assistants" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return await self.api_client.call_api(
            '/v1/assistants', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssistantListResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def list_chats(self, assistant_id, **kwargs):  # noqa: E501
        """List chats  # noqa: E501

        Retrieve a list of all chats available in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_chats(assistant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :return: ChatListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.list_chats_with_http_info(assistant_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.list_chats_with_http_info(assistant_id, **kwargs)  # noqa: E501
            return data

    async def list_chats_with_http_info(self, assistant_id, **kwargs):  # noqa: E501
        """List chats  # noqa: E501

        Retrieve a list of all chats available in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_chats_with_http_info(assistant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :return: ChatListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assistant_id', 'limit', 'order', 'after', 'before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_chats" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assistant_id' is set
        if ('assistant_id' not in params or
                params['assistant_id'] is None):
            raise ValueError("Missing the required parameter `assistant_id` when calling `list_chats`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assistant_id' in params:
            path_params['assistant_id'] = params['assistant_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return await self.api_client.call_api(
            '/v1/assistants/{assistant_id}/chats', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChatListResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def list_messages(self, assistant_id, chat_id, **kwargs):  # noqa: E501
        """List messages  # noqa: E501

        Retrieve a paginated list of messages from a specific chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_messages(assistant_id, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :return: MessageListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.list_messages_with_http_info(assistant_id, chat_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.list_messages_with_http_info(assistant_id, chat_id, **kwargs)  # noqa: E501
            return data

    async def list_messages_with_http_info(self, assistant_id, chat_id, **kwargs):  # noqa: E501
        """List messages  # noqa: E501

        Retrieve a paginated list of messages from a specific chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_messages_with_http_info(assistant_id, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :return: MessageListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['assistant_id', 'chat_id', 'limit', 'order', 'after', 'before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_messages" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'assistant_id' is set
        if ('assistant_id' not in params or
                params['assistant_id'] is None):
            raise ValueError("Missing the required parameter `assistant_id` when calling `list_messages`")  # noqa: E501
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in params or
                params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `list_messages`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assistant_id' in params:
            path_params['assistant_id'] = params['assistant_id']  # noqa: E501
        if 'chat_id' in params:
            path_params['chat_id'] = params['chat_id']  # noqa: E501

        query_params = []
        if 'limit' in params:
            query_params.append(('limit', params['limit']))  # noqa: E501
        if 'order' in params:
            query_params.append(('order', params['order']))  # noqa: E501
        if 'after' in params:
            query_params.append(('after', params['after']))  # noqa: E501
        if 'before' in params:
            query_params.append(('before', params['before']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return await self.api_client.call_api(
            '/v1/assistants/{assistant_id}/chats/{chat_id}/messages', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MessageListResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def update_assistant(self, body, assistant_id, **kwargs):  # noqa: E501
        """Update assistant  # noqa: E501

        Update the properties of an existing assistant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_assistant(body, assistant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AssistantUpdateRequest body: (required)
        :param object assistant_id: (required)
        :return: AssistantUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.update_assistant_with_http_info(body, assistant_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.update_assistant_with_http_info(body, assistant_id, **kwargs)  # noqa: E501
            return data

    async def update_assistant_with_http_info(self, body, assistant_id, **kwargs):  # noqa: E501
        """Update assistant  # noqa: E501

        Update the properties of an existing assistant.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_assistant_with_http_info(body, assistant_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AssistantUpdateRequest body: (required)
        :param object assistant_id: (required)
        :return: AssistantUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'assistant_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_assistant" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_assistant`")  # noqa: E501
        # verify the required parameter 'assistant_id' is set
        if ('assistant_id' not in params or
                params['assistant_id'] is None):
            raise ValueError(
                "Missing the required parameter `assistant_id` when calling `update_assistant`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assistant_id' in params:
            path_params['assistant_id'] = params['assistant_id']  # noqa: E501

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

        return await self.api_client.call_api(
            '/v1/assistants/{assistant_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AssistantUpdateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def update_chat(self, body, assistant_id, chat_id, **kwargs):  # noqa: E501
        """Update chat  # noqa: E501

        Update the properties of a specific chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_chat(body, assistant_id, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChatUpdateRequest body: (required)
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :return: ChatUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.update_chat_with_http_info(body, assistant_id, chat_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.update_chat_with_http_info(body, assistant_id, chat_id, **kwargs)  # noqa: E501
            return data

    async def update_chat_with_http_info(self, body, assistant_id, chat_id, **kwargs):  # noqa: E501
        """Update chat  # noqa: E501

        Update the properties of a specific chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_chat_with_http_info(body, assistant_id, chat_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChatUpdateRequest body: (required)
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :return: ChatUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'assistant_id', 'chat_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_chat" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_chat`")  # noqa: E501
        # verify the required parameter 'assistant_id' is set
        if ('assistant_id' not in params or
                params['assistant_id'] is None):
            raise ValueError("Missing the required parameter `assistant_id` when calling `update_chat`")  # noqa: E501
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in params or
                params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `update_chat`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assistant_id' in params:
            path_params['assistant_id'] = params['assistant_id']  # noqa: E501
        if 'chat_id' in params:
            path_params['chat_id'] = params['chat_id']  # noqa: E501

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

        return await self.api_client.call_api(
            '/v1/assistants/{assistant_id}/chats/{chat_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChatUpdateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def update_message(self, body, assistant_id, chat_id, message_id, **kwargs):  # noqa: E501
        """Update message  # noqa: E501

        Modify the metadata of a specific message within a chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_message(body, assistant_id, chat_id, message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessageUpdateRequest body: (required)
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :param object message_id: (required)
        :return: MessageUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.update_message_with_http_info(body, assistant_id, chat_id, message_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.update_message_with_http_info(body, assistant_id, chat_id, message_id, **kwargs)  # noqa: E501
            return data

    async def update_message_with_http_info(self, body, assistant_id, chat_id, message_id, **kwargs):  # noqa: E501
        """Update message  # noqa: E501

        Modify the metadata of a specific message within a chat.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_message_with_http_info(body, assistant_id, chat_id, message_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param MessageUpdateRequest body: (required)
        :param object assistant_id: (required)
        :param object chat_id: (required)
        :param object message_id: (required)
        :return: MessageUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'assistant_id', 'chat_id', 'message_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_message" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_message`")  # noqa: E501
        # verify the required parameter 'assistant_id' is set
        if ('assistant_id' not in params or
                params['assistant_id'] is None):
            raise ValueError(
                "Missing the required parameter `assistant_id` when calling `update_message`")  # noqa: E501
        # verify the required parameter 'chat_id' is set
        if ('chat_id' not in params or
                params['chat_id'] is None):
            raise ValueError("Missing the required parameter `chat_id` when calling `update_message`")  # noqa: E501
        # verify the required parameter 'message_id' is set
        if ('message_id' not in params or
                params['message_id'] is None):
            raise ValueError("Missing the required parameter `message_id` when calling `update_message`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'assistant_id' in params:
            path_params['assistant_id'] = params['assistant_id']  # noqa: E501
        if 'chat_id' in params:
            path_params['chat_id'] = params['chat_id']  # noqa: E501
        if 'message_id' in params:
            path_params['message_id'] = params['message_id']  # noqa: E501

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

        return await self.api_client.call_api(
            '/v1/assistants/{assistant_id}/chats/{chat_id}/messages/{message_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='MessageUpdateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
