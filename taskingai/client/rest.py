# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0
"""

from __future__ import absolute_import

import io
import json
import logging
from urllib.parse import urlencode


# python 2 and python 3 compatibility library
import httpx
from httpx import HTTPError
from .stream import Stream, AsyncStream
from typing import Union

logger = logging.getLogger(__name__)


class RESTResponse(io.IOBase):
    def __init__(self, resp):
        self.httpx_response = resp
        self.status = resp.status_code  # httpx uses status_code
        self.reason = resp.reason_phrase  # httpx uses reason_phrase
        self.data = resp.content  # httpx uses content for the response body

    def getheaders(self):
        """Returns a dictionary of the response headers."""
        return self.httpx_response.headers  # httpx headers are a dict-like object

    def getheader(self, name, default=None):
        """Returns a given response header."""
        return self.httpx_response.headers.get(name, default)  # Using dict get method


class RESTSyncClientObject(object):
    def __init__(self, configuration, pools_size=4, maxsize=None):
        # set default user agent
        if maxsize is None:
            maxsize = configuration.connection_pool_maxsize if configuration.connection_pool_maxsize is not None else 4

        limits = httpx.Limits(max_connections=maxsize, max_keepalive_connections=pools_size)

        # SSL configuration
        verify = configuration.ssl_ca_cert or True
        if not configuration.verify_ssl:
            verify = False

        # proxy configuration
        proxies = None
        if configuration.proxy:
            proxies = {
                "http://": configuration.proxy,
                "https://": configuration.proxy,
            }

        # create httpx client
        self.client = httpx.Client(
            limits=limits,
            verify=verify,
            proxies=proxies,
        )

        # set client cert if provided
        if configuration.cert_file and configuration.key_file:
            self.client.cert = (configuration.cert_file, configuration.key_file)

    def _stream_generator(self, method, url, query_params, headers, request_body, _request_timeout):
        """Generator function for streaming requests."""
        with self.client.stream(
            method, url, params=query_params, headers=headers, content=request_body, timeout=_request_timeout
        ) as response:
            for line in response.iter_lines():
                yield line

    def request(
        self,
        method,
        url,
        stream=False,
        query_params=None,
        headers=None,
        body=None,
        post_params=None,
        files=None,
        _preload_content=True,
        _request_timeout=None,
    ) -> Union[RESTResponse, Stream]:
        """
        Perform synchronous HTTP requests.

        :param method: HTTP request method (e.g., 'GET', 'POST', 'PUT', etc.).
        :param url: URL for the HTTP request.
        :param query_params: Query parameters to be included in the URL.
        :param headers: HTTP request headers.
        :param body: Request body for 'application/json' content type.
        :param post_params: Request post parameters for content types
                            'application/x-www-form-urlencoded' and
                            'multipart/form-data'.
        :param files: Request files for 'multipart/form-data' content type.
        :param _preload_content: If False, the httpx.Response object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: Timeout setting for this request. If a single
                                 number is provided, it will be the total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.

        This method is synchronous and should be called with 'await' in an
        asynchronous context. It uses httpx.AsyncClient for making HTTP requests.
        """
        method = method.upper()
        assert method in ["GET", "HEAD", "DELETE", "POST", "PUT", "PATCH", "OPTIONS"]

        if post_params and body:
            raise ValueError("body parameter cannot be used with post_params parameter.")

        if files and body:
            raise ValueError("body parameter cannot be used with files parameter.")

        if post_params and files:
            raise ValueError("post_params parameter cannot be used with files parameter.")

        headers = headers or {}
        request_content = None
        request_files = None

        # Determine the correct content type and prepare data accordingly
        if post_params:
            if "Content-Type" not in headers or headers["Content-Type"] == "application/x-www-form-urlencoded":
                headers["Content-Type"] = "application/x-www-form-urlencoded"
                request_content = urlencode(post_params)
            elif headers["Content-Type"] == "multipart/form-data":
                # In the case of multipart, we leave it to httpx to encode the files and data
                request_content = post_params
        elif body:
            if "Content-Type" not in headers:
                headers["Content-Type"] = "application/json"
            if body is not None:
                request_content = json.dumps(body)
        elif files:
            request_files = files

        try:
            if stream:
                return Stream(
                    stream_generator=self._stream_generator(
                        method, url, query_params, headers, request_content, _request_timeout
                    )
                )
            else:
                r = self.client.request(
                    method,
                    url,
                    params=query_params,
                    headers=headers,
                    content=request_content,
                    files=request_files,
                    timeout=_request_timeout,
                )
        except HTTPError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

        if not 200 <= r.status <= 299:
            raise ApiException(http_resp=r)

        return r

    def GET(self, url, stream=False, headers=None, query_params=None, _preload_content=True, _request_timeout=None):
        return self.request(
            "GET",
            url,
            stream=stream,
            headers=headers,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            query_params=query_params,
        )

    def HEAD(self, url, stream=False, headers=None, query_params=None, _preload_content=True, _request_timeout=None):
        return self.request(
            "HEAD",
            url,
            stream=stream,
            headers=headers,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            query_params=query_params,
        )

    def OPTIONS(
        self,
        url,
        stream=False,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return self.request(
            "OPTIONS",
            url,
            stream=stream,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    def DELETE(
        self,
        url,
        stream=False,
        headers=None,
        query_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return self.request(
            "DELETE",
            url,
            stream=stream,
            headers=headers,
            query_params=query_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    def POST(
        self,
        url,
        stream=False,
        headers=None,
        query_params=None,
        post_params=None,
        files=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return self.request(
            "POST",
            url,
            stream=stream,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            files=files,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    def PUT(
        self,
        url,
        stream=False,
        headers=None,
        query_params=None,
        post_params=None,
        files=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return self.request(
            "PUT",
            url,
            headers=headers,
            stream=stream,
            query_params=query_params,
            post_params=post_params,
            files=files,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    def PATCH(
        self,
        url,
        stream=False,
        headers=None,
        query_params=None,
        post_params=None,
        files=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return self.request(
            "PATCH",
            url,
            stream=stream,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            files=files,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )


class RESTAsyncClientObject(object):
    def __init__(self, configuration, pools_size=4, maxsize=None):
        cert = None
        if configuration.cert_file and configuration.key_file:
            cert = (configuration.cert_file, configuration.key_file)
        self.client = httpx.AsyncClient(
            proxies=configuration.proxy, verify=configuration.verify_ssl, cert=cert, http1=True
        )

    async def _async_stream_generator(self, method, url, query_params, headers, request_body, _request_timeout):
        """Asynchronous generator function for streaming requests."""
        async with self.client.stream(
            method, url, params=query_params, headers=headers, content=request_body, timeout=_request_timeout
        ) as response:
            async for line in response.aiter_lines():
                yield line

    async def request(
        self,
        method,
        url,
        stream=False,
        query_params=None,
        headers=None,
        body=None,
        post_params=None,
        files=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        """
        Perform asynchronous HTTP requests.

        :param method: HTTP request method (e.g., 'GET', 'POST', 'PUT', etc.).
        :param url: URL for the HTTP request.
        :param query_params: Query parameters to be included in the URL.
        :param headers: HTTP request headers.
        :param body: Request body for 'application/json' content type.
        :param post_params: Request post parameters for content types
                            'application/x-www-form-urlencoded' and
                            'multipart/form-data'.
        :param files: Request files for 'multipart/form-data' content type.
        :param _preload_content: If False, the httpx.Response object will
                                 be returned without reading/decoding response
                                 data. Default is True.
        :param _request_timeout: Timeout setting for this request. If a single
                                 number is provided, it will be the total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.

        This method is asynchronous and should be called with 'await' in an
        asynchronous context. It uses httpx.AsyncClient for making HTTP requests.
        """
        method = method.upper()
        assert method in ["GET", "HEAD", "DELETE", "POST", "PUT", "PATCH", "OPTIONS"]

        if post_params and body:
            raise ValueError("body parameter cannot be used with post_params parameter.")

        if files and body:
            raise ValueError("body parameter cannot be used with files parameter.")

        if post_params and files:
            raise ValueError("post_params parameter cannot be used with files parameter.")

        headers = headers or {}
        request_content = None
        request_files = None

        # Determine the correct content type and prepare data accordingly
        if post_params:
            if "Content-Type" not in headers or headers["Content-Type"] == "application/x-www-form-urlencoded":
                headers["Content-Type"] = "application/x-www-form-urlencoded"
                request_content = urlencode(post_params)
            elif headers["Content-Type"] == "multipart/form-data":
                # In the case of multipart, we leave it to httpx to encode the files and data
                request_content = post_params
        elif body:
            if "Content-Type" not in headers:
                headers["Content-Type"] = "application/json"
            if body is not None:
                request_content = json.dumps(body)
        elif files:
            request_files = files

        try:
            if stream:
                # Return an asynchronous stream generator
                return AsyncStream(
                    async_stream_generator=self._async_stream_generator(
                        method, url, query_params, headers, request_content, _request_timeout
                    )
                )
            else:
                # For non-streaming requests
                r = await self.client.request(
                    method,
                    url,
                    params=query_params,
                    headers=headers,
                    content=request_content,
                    files=request_files,
                    timeout=_request_timeout,
                )

        except HTTPError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

        if not 200 <= r.status <= 299:
            raise ApiException(http_resp=r)

        return r

    async def GET(
        self, url, stream=False, headers=None, query_params=None, _preload_content=True, _request_timeout=None
    ):
        return await self.request(
            "GET",
            url,
            stream=stream,
            headers=headers,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            query_params=query_params,
        )

    async def HEAD(
        self, url, stream=False, headers=None, query_params=None, _preload_content=True, _request_timeout=None
    ):
        return await self.request(
            "HEAD",
            url,
            stream=stream,
            headers=headers,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            query_params=query_params,
        )

    async def OPTIONS(
        self,
        url,
        stream=False,
        headers=None,
        query_params=None,
        post_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return await self.request(
            "OPTIONS",
            url,
            stream=stream,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    async def DELETE(
        self,
        url,
        stream=False,
        headers=None,
        query_params=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return await self.request(
            "DELETE",
            url,
            stream=stream,
            headers=headers,
            query_params=query_params,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    async def POST(
        self,
        url,
        stream=False,
        headers=None,
        query_params=None,
        post_params=None,
        files=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return await self.request(
            "POST",
            url,
            stream=stream,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            files=files,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    async def PUT(
        self,
        url,
        stream=False,
        headers=None,
        query_params=None,
        post_params=None,
        files=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return await self.request(
            "PUT",
            url,
            stream=stream,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            files=files,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )

    async def PATCH(
        self,
        url,
        stream=False,
        headers=None,
        query_params=None,
        post_params=None,
        files=None,
        body=None,
        _preload_content=True,
        _request_timeout=None,
    ):
        return await self.request(
            "PATCH",
            url,
            stream=stream,
            headers=headers,
            query_params=query_params,
            post_params=post_params,
            files=files,
            _preload_content=_preload_content,
            _request_timeout=_request_timeout,
            body=body,
        )


class ApiException(Exception):
    def __init__(self, status=None, reason=None, http_resp=None):
        if http_resp:
            self.status = http_resp.status
            self.reason = http_resp.reason
            self.body = http_resp.data
            self.headers = http_resp.getheaders()
        else:
            self.status = status
            self.reason = reason
            self.body = None
            self.headers = None

    def __str__(self):
        """Custom error messages for exception"""
        error_message = "({0})\n" "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
