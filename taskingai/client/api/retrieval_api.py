# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from taskingai.client.api_client import SyncApiClient


class RetrievalApi(object):

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = SyncApiClient()
        self.api_client = api_client

    def create_collection(self, body, **kwargs):  # noqa: E501
        """Create collection  # noqa: E501

        This operation creates a new retrieval collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_collection(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CollectionCreateRequest body: (required)
        :return: CollectionCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_collection_with_http_info(body, **kwargs)  # noqa: E501
        else:
            (data) = self.create_collection_with_http_info(body, **kwargs)  # noqa: E501
            return data

    def create_collection_with_http_info(self, body, **kwargs):  # noqa: E501
        """Create collection  # noqa: E501

        This operation creates a new retrieval collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_collection_with_http_info(body, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CollectionCreateRequest body: (required)
        :return: CollectionCreateResponse
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
                    " to method create_collection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_collection`")  # noqa: E501

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
            '/v1/collections', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def create_record(self, body, collection_id, **kwargs):  # noqa: E501
        """Create record  # noqa: E501

        Create a new record in a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_text_record(body, collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordCreateRequest body: (required)
        :param object collection_id: (required)
        :return: RecordCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.create_record_with_http_info(body, collection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.create_record_with_http_info(body, collection_id, **kwargs)  # noqa: E501
            return data

    def create_record_with_http_info(self, body, collection_id, **kwargs):  # noqa: E501
        """Create record  # noqa: E501

        Create a new record in a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_record_with_http_info(body, collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordCreateRequest body: (required)
        :param object collection_id: (required)
        :return: RecordCreateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'collection_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create_record" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `create_record`")  # noqa: E501
        # verify the required parameter 'collection_id' is set
        if ('collection_id' not in params or
                params['collection_id'] is None):
            raise ValueError("Missing the required parameter `collection_id` when calling `create_record`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection_id' in params:
            path_params['collection_id'] = params['collection_id']  # noqa: E501

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
            '/v1/collections/{collection_id}/records', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RecordCreateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_collection(self, collection_id, **kwargs):  # noqa: E501
        """Delete collection  # noqa: E501

        This operation deletes a specific collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_collection(collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object collection_id: (required)
        :return: DeleteCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_collection_with_http_info(collection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_collection_with_http_info(collection_id, **kwargs)  # noqa: E501
            return data

    def delete_collection_with_http_info(self, collection_id, **kwargs):  # noqa: E501
        """Delete collection  # noqa: E501

        This operation deletes a specific collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_collection_with_http_info(collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object collection_id: (required)
        :return: DeleteCollectionResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_collection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection_id' is set
        if ('collection_id' not in params or
                params['collection_id'] is None):
            raise ValueError("Missing the required parameter `collection_id` when calling `delete_collection`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection_id' in params:
            path_params['collection_id'] = params['collection_id']  # noqa: E501

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

        return self.api_client.call_api(
            '/v1/collections/{collection_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='DeleteCollectionResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_record(self, collection_id, record_id, **kwargs):  # noqa: E501
        """Delete record  # noqa: E501

        Delete a specific record from a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_record(collection_id, record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object collection_id: (required)
        :param object record_id: (required)
        :return: RecordDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.delete_record_with_http_info(collection_id, record_id, **kwargs)  # noqa: E501
        else:
            (data) = self.delete_record_with_http_info(collection_id, record_id, **kwargs)  # noqa: E501
            return data

    def delete_record_with_http_info(self, collection_id, record_id, **kwargs):  # noqa: E501
        """Delete record  # noqa: E501

        Delete a specific record from a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_record_with_http_info(collection_id, record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object collection_id: (required)
        :param object record_id: (required)
        :return: RecordDeleteResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection_id', 'record_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_record" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection_id' is set
        if ('collection_id' not in params or
                params['collection_id'] is None):
            raise ValueError("Missing the required parameter `collection_id` when calling `delete_record`")  # noqa: E501
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params or
                params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id` when calling `delete_record`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection_id' in params:
            path_params['collection_id'] = params['collection_id']  # noqa: E501
        if 'record_id' in params:
            path_params['record_id'] = params['record_id']  # noqa: E501

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

        return self.api_client.call_api(
            '/v1/collections/{collection_id}/records/{record_id}', 'DELETE',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RecordDeleteResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_collection(self, collection_id, **kwargs):  # noqa: E501
        """Get collection  # noqa: E501

        This operation returns a single collection in your Text Base by its unique ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_collection(collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object collection_id: (required)
        :return: CollectionGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_collection_with_http_info(collection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_collection_with_http_info(collection_id, **kwargs)  # noqa: E501
            return data

    def get_collection_with_http_info(self, collection_id, **kwargs):  # noqa: E501
        """Get collection  # noqa: E501

        This operation returns a single collection in your Text Base by its unique ID.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_collection_with_http_info(collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object collection_id: (required)
        :return: CollectionGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_collection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection_id' is set
        if ('collection_id' not in params or
                params['collection_id'] is None):
            raise ValueError("Missing the required parameter `collection_id` when calling `get_collection`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection_id' in params:
            path_params['collection_id'] = params['collection_id']  # noqa: E501

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

        return self.api_client.call_api(
            '/v1/collections/{collection_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionGetResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_record(self, collection_id, record_id, **kwargs):  # noqa: E501
        """Get record  # noqa: E501

        Retrieve a specific record from a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_record(collection_id, record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object collection_id: (required)
        :param object record_id: (required)
        :return: RecordGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.get_record_with_http_info(collection_id, record_id, **kwargs)  # noqa: E501
        else:
            (data) = self.get_record_with_http_info(collection_id, record_id, **kwargs)  # noqa: E501
            return data

    def get_record_with_http_info(self, collection_id, record_id, **kwargs):  # noqa: E501
        """Get record  # noqa: E501

        Retrieve a specific record from a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_record_with_http_info(collection_id, record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object collection_id: (required)
        :param object record_id: (required)
        :return: RecordGetResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection_id', 'record_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_record" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection_id' is set
        if ('collection_id' not in params or
                params['collection_id'] is None):
            raise ValueError("Missing the required parameter `collection_id` when calling `get_record`")  # noqa: E501
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params or
                params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id` when calling `get_record`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection_id' in params:
            path_params['collection_id'] = params['collection_id']  # noqa: E501
        if 'record_id' in params:
            path_params['record_id'] = params['record_id']  # noqa: E501

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

        return self.api_client.call_api(
            '/v1/collections/{collection_id}/records/{record_id}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RecordGetResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_collections(self, **kwargs):  # noqa: E501
        """List collections  # noqa: E501

        This operation returns a list of your retrieval collections.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_collections(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :return: CollectionListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_collections_with_http_info(**kwargs)  # noqa: E501
        else:
            (data) = self.list_collections_with_http_info(**kwargs)  # noqa: E501
            return data

    def list_collections_with_http_info(self, **kwargs):  # noqa: E501
        """List collections  # noqa: E501

        This operation returns a list of your retrieval collections.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_collections_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :return: CollectionListResponse
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
                    " to method list_collections" % key
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

        return self.api_client.call_api(
            '/v1/collections', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionListResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list_records(self, collection_id, **kwargs):  # noqa: E501
        """List records  # noqa: E501

        Retrieve a paginated list of records from a specific collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_records(collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object collection_id: (required)
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :return: RecordListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.list_records_with_http_info(collection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.list_records_with_http_info(collection_id, **kwargs)  # noqa: E501
            return data

    def list_records_with_http_info(self, collection_id, **kwargs):  # noqa: E501
        """List records  # noqa: E501

        Retrieve a paginated list of records from a specific collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_records_with_http_info(collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param object collection_id: (required)
        :param object limit:
        :param object order:
        :param object after:
        :param object before:
        :return: RecordListResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['collection_id', 'limit', 'order', 'after', 'before']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list_records" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'collection_id' is set
        if ('collection_id' not in params or
                params['collection_id'] is None):
            raise ValueError("Missing the required parameter `collection_id` when calling `list_records`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection_id' in params:
            path_params['collection_id'] = params['collection_id']  # noqa: E501

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

        return self.api_client.call_api(
            '/v1/collections/{collection_id}/records', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RecordListResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def query_chunks(self, body, collection_id, **kwargs):  # noqa: E501
        """Query chunks  # noqa: E501

        Query the most relevant chunks from a specific collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_chunks(body, collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChunkQueryRequest body: (required)
        :param object collection_id: (required)
        :return: ChunkQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.query_chunks_with_http_info(body, collection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.query_chunks_with_http_info(body, collection_id, **kwargs)  # noqa: E501
            return data

    def query_chunks_with_http_info(self, body, collection_id, **kwargs):  # noqa: E501
        """Query chunks  # noqa: E501

        Query the most relevant chunks from a specific collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.query_chunks_with_http_info(body, collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param ChunkQueryRequest body: (required)
        :param object collection_id: (required)
        :return: ChunkQueryResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'collection_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method query_chunks" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `query_chunks`")  # noqa: E501
        # verify the required parameter 'collection_id' is set
        if ('collection_id' not in params or
                params['collection_id'] is None):
            raise ValueError("Missing the required parameter `collection_id` when calling `query_chunks`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection_id' in params:
            path_params['collection_id'] = params['collection_id']  # noqa: E501

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
            '/v1/collections/{collection_id}/chunks/query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChunkQueryResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_collection(self, body, collection_id, **kwargs):  # noqa: E501
        """Update collection  # noqa: E501

        This operation updates the metadata of a specific collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_collection(body, collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CollectionUpdateRequest body: (required)
        :param object collection_id: (required)
        :return: CollectionUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_collection_with_http_info(body, collection_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_collection_with_http_info(body, collection_id, **kwargs)  # noqa: E501
            return data

    def update_collection_with_http_info(self, body, collection_id, **kwargs):  # noqa: E501
        """Update collection  # noqa: E501

        This operation updates the metadata of a specific collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_collection_with_http_info(body, collection_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param CollectionUpdateRequest body: (required)
        :param object collection_id: (required)
        :return: CollectionUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'collection_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_collection" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_collection`")  # noqa: E501
        # verify the required parameter 'collection_id' is set
        if ('collection_id' not in params or
                params['collection_id'] is None):
            raise ValueError("Missing the required parameter `collection_id` when calling `update_collection`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection_id' in params:
            path_params['collection_id'] = params['collection_id']  # noqa: E501

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
            '/v1/collections/{collection_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='CollectionUpdateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_record(self, body, collection_id, record_id, **kwargs):  # noqa: E501
        """Update record  # noqa: E501

        Modify the metadata of a specific record within a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_record(body, collection_id, record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordUpdateRequest body: (required)
        :param object collection_id: (required)
        :param object record_id: (required)
        :return: RecordUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async_req'):
            return self.update_record_with_http_info(body, collection_id, record_id, **kwargs)  # noqa: E501
        else:
            (data) = self.update_record_with_http_info(body, collection_id, record_id, **kwargs)  # noqa: E501
            return data

    def update_record_with_http_info(self, body, collection_id, record_id, **kwargs):  # noqa: E501
        """Update record  # noqa: E501

        Modify the metadata of a specific record within a collection.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_record_with_http_info(body, collection_id, record_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param RecordUpdateRequest body: (required)
        :param object collection_id: (required)
        :param object record_id: (required)
        :return: RecordUpdateResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['body', 'collection_id', 'record_id']  # noqa: E501
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_record" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'body' is set
        if ('body' not in params or
                params['body'] is None):
            raise ValueError("Missing the required parameter `body` when calling `update_record`")  # noqa: E501
        # verify the required parameter 'collection_id' is set
        if ('collection_id' not in params or
                params['collection_id'] is None):
            raise ValueError("Missing the required parameter `collection_id` when calling `update_record`")  # noqa: E501
        # verify the required parameter 'record_id' is set
        if ('record_id' not in params or
                params['record_id'] is None):
            raise ValueError("Missing the required parameter `record_id` when calling `update_record`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        if 'collection_id' in params:
            path_params['collection_id'] = params['collection_id']  # noqa: E501
        if 'record_id' in params:
            path_params['record_id'] = params['record_id']  # noqa: E501

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
            '/v1/collections/{collection_id}/records/{record_id}', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='RecordUpdateResponse',  # noqa: E501
            auth_settings=auth_settings,
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
