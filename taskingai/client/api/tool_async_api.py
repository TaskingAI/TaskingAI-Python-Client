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


class AsyncToolApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = AsyncApiClient()
        self.api_client = api_client

    async def bulk_create_action(self, body, **kwargs):  # noqa: E501
        """Bulk create action  # noqa: E501

        Bulk create actions with an OpenAPI schema. If there are multiple paths and methods in the schema, multiple actions will be created.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_create_action(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ActionBulkCreateRequest body: (required)
        :return: ActionBulkCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.bulk_create_action_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = await self.bulk_create_action_with_http_info(body, **kwargs)  # noqa: E501
            return data

    async def bulk_create_action_with_http_info(self, body, **kwargs):  # noqa: E501
        """Bulk create action  # noqa: E501

        Bulk create actions with an OpenAPI schema. If there are multiple paths and methods in the schema, multiple actions will be created.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.bulk_create_action_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ActionBulkCreateRequest body: (required)
        :return: ActionBulkCreateResponse
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
                    " to method bulk_create_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `bulk_create_action`")  # noqa: E501

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
            '/v1/actions/bulk_create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActionBulkCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def create_function(self, body, **kwargs):  # noqa: E501
        """Create function  # noqa: E501

        This operation creates a new function in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_function(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FunctionCreateRequest body: (required)
        :return: FunctionCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.create_function_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = await self.create_function_with_http_info(body, **kwargs)  # noqa: E501
            return data

    async def create_function_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create function  # noqa: E501

        This operation creates a new function in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_function_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FunctionCreateRequest body: (required)
        :return: FunctionCreateResponse
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
                    " to method create_function" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_function`")  # noqa: E501

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
            '/v1/functions', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FunctionCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def delete_action(self, action_id, **kwargs):  # noqa: E501
        """Delete an action  # noqa: E501

        Remove an existing action from your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_action(action_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object action_id: (required)
        :return: ActionDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.delete_action_with_http_info(action_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.delete_action_with_http_info(action_id, **kwargs)  # noqa: E501
            return data

    async def delete_action_with_http_info(self, action_id, **kwargs):  # noqa: E501
        """Delete an action  # noqa: E501

        Remove an existing action from your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_action_with_http_info(action_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object action_id: (required)
        :return: ActionDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['action_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'action_id' is set
        if ('action_id' not in params or
                params['action_id'] is None):
            raise ValueError("Missing the required parameter `action_id` when calling `delete_action`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'action_id' in params:
            path_params['action_id'] = params['action_id']  # noqa: E501

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
            '/v1/actions/{action_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActionDeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def delete_function(self, function_id, **kwargs):  # noqa: E501
        """Delete function  # noqa: E501

        Remove an existing function from your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_function(function_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object function_id: (required)
        :return: FunctionDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.delete_function_with_http_info(function_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.delete_function_with_http_info(function_id, **kwargs)  # noqa: E501
            return data

    async def delete_function_with_http_info(self, function_id, **kwargs):  # noqa: E501
        """Delete function  # noqa: E501

        Remove an existing function from your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_function_with_http_info(function_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object function_id: (required)
        :return: FunctionDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['function_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_function" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'function_id' is set
        if ('function_id' not in params or
                params['function_id'] is None):
            raise ValueError("Missing the required parameter `function_id` when calling `delete_function`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'function_id' in params:
            path_params['function_id'] = params['function_id']  # noqa: E501

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
            '/v1/functions/{function_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FunctionDeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def get_action(self, action_id, **kwargs):  # noqa: E501
        """Get action  # noqa: E501

        This operation returns a single action in your project by its unique ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_action(action_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object action_id: (required)
        :return: ActionGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.get_action_with_http_info(action_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.get_action_with_http_info(action_id, **kwargs)  # noqa: E501
            return data

    async def get_action_with_http_info(self, action_id, **kwargs):  # noqa: E501
        """Get action  # noqa: E501

        This operation returns a single action in your project by its unique ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_action_with_http_info(action_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object action_id: (required)
        :return: ActionGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['action_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'action_id' is set
        if ('action_id' not in params or
                params['action_id'] is None):
            raise ValueError("Missing the required parameter `action_id` when calling `get_action`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'action_id' in params:
            path_params['action_id'] = params['action_id']  # noqa: E501

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
            '/v1/actions/{action_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActionGetResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def get_function(self, function_id, **kwargs):  # noqa: E501
        """Get function  # noqa: E501

        This operation returns a single function in your project by its unique ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_function(function_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object function_id: (required)
        :return: FunctionGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.get_function_with_http_info(function_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.get_function_with_http_info(function_id, **kwargs)  # noqa: E501
            return data

    async def get_function_with_http_info(self, function_id, **kwargs):  # noqa: E501
        """Get function  # noqa: E501

        This operation returns a single function in your project by its unique ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_function_with_http_info(function_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object function_id: (required)
        :return: FunctionGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['function_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_function" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'function_id' is set
        if ('function_id' not in params or
                params['function_id'] is None):
            raise ValueError("Missing the required parameter `function_id` when calling `get_function`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'function_id' in params:
            path_params['function_id'] = params['function_id']  # noqa: E501

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
            '/v1/functions/{function_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FunctionGetResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def list_actions(self, **kwargs):  # noqa: E501
        """List actions  # noqa: E501

        This operation returns a list of all your actions in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_actions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :param object offset:
        :return: ActionListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.list_actions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = await self.list_actions_with_http_info(**kwargs)  # noqa: E501
            return data

    async def list_actions_with_http_info(self, **kwargs):  # noqa: E501
        """List actions  # noqa: E501

        This operation returns a list of all your actions in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_actions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :param object offset:
        :return: ActionListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'order', 'after', 'before', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_actions" % key
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
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

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
            '/v1/actions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActionListResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def list_functions(self, **kwargs):  # noqa: E501
        """List functions  # noqa: E501

        This operation returns a list of all your functions in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_functions(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :param object offset:
        :return: FunctionListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.list_functions_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = await self.list_functions_with_http_info(**kwargs)  # noqa: E501
            return data

    async def list_functions_with_http_info(self, **kwargs):  # noqa: E501
        """List functions  # noqa: E501

        This operation returns a list of all your functions in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_functions_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :param object offset:
        :return: FunctionListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['limit', 'order', 'after', 'before', 'offset']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_functions" % key
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
        if 'offset' in params:
            query_params.append(('offset', params['offset']))  # noqa: E501

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
            '/v1/functions', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FunctionListResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def run_action(self, body, action_id, **kwargs):  # noqa: E501
        """Run an action  # noqa: E501

        Run and test an action with API call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.run_action(body, action_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ActionRunRequest body: (required)
        :param object action_id: (required)
        :return: ActionRunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.run_action_with_http_info(body, action_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.run_action_with_http_info(body, action_id, **kwargs)  # noqa: E501
            return data

    async def run_action_with_http_info(self, body, action_id, **kwargs):  # noqa: E501
        """Run an action  # noqa: E501

        Run and test an action with API call.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.run_action_with_http_info(body, action_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ActionRunRequest body: (required)
        :param object action_id: (required)
        :return: ActionRunResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'action_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method run_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `run_action`")  # noqa: E501
        # verify the required parameter 'action_id' is set
        if ('action_id' not in params or
                params['action_id'] is None):
            raise ValueError("Missing the required parameter `action_id` when calling `run_action`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'action_id' in params:
            path_params['action_id'] = params['action_id']  # noqa: E501

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
            '/v1/actions/{action_id}/run', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActionRunResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def update_action(self, body, action_id, **kwargs):  # noqa: E501
        """Update action  # noqa: E501

        Update an existing action with an OpenAPI schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_action(body, action_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ActionUpdateRequest body: (required)
        :param object action_id: (required)
        :return: ActionUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.update_action_with_http_info(body, action_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.update_action_with_http_info(body, action_id, **kwargs)  # noqa: E501
            return data

    async def update_action_with_http_info(self, body, action_id, **kwargs):  # noqa: E501
        """Update action  # noqa: E501

        Update an existing action with an OpenAPI schema.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_action_with_http_info(body, action_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ActionUpdateRequest body: (required)
        :param object action_id: (required)
        :return: ActionUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'action_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_action" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_action`")  # noqa: E501
        # verify the required parameter 'action_id' is set
        if ('action_id' not in params or
                params['action_id'] is None):
            raise ValueError("Missing the required parameter `action_id` when calling `update_action`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'action_id' in params:
            path_params['action_id'] = params['action_id']  # noqa: E501

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
            '/v1/actions/{action_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ActionUpdateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    async def update_function(self, body, function_id, **kwargs):  # noqa: E501
        """Update function  # noqa: E501

        Update a function in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_function(body, function_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FunctionUpdateRequest body: (required)
        :param object function_id: (required)
        :return: FunctionUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return await self.update_function_with_http_info(body, function_id, **kwargs)  # noqa: E501
        else:
            (data) = await self.update_function_with_http_info(body, function_id, **kwargs)  # noqa: E501
            return data

    async def update_function_with_http_info(self, body, function_id, **kwargs):  # noqa: E501
        """Update function  # noqa: E501

        Update a function in your project.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_function_with_http_info(body, function_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param FunctionUpdateRequest body: (required)
        :param object function_id: (required)
        :return: FunctionUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'function_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_function" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_function`")  # noqa: E501
        # verify the required parameter 'function_id' is set
        if ('function_id' not in params or
                params['function_id'] is None):
            raise ValueError("Missing the required parameter `function_id` when calling `update_function`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'function_id' in params:
            path_params['function_id'] = params['function_id']  # noqa: E501

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
            '/v1/functions/{function_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='FunctionUpdateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
