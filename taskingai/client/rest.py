# coding: utf-8

"""
    TaskingAI API

    OpenAPI spec version: 0.1.0
"""

from __future__ import absolute_import

import io
import json
import logging
import re
import ssl

import certifi
# python 2 and python 3 compatibility library
import httpx
from httpx import HTTPError

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
        # 设置连接池的最大并发连接数
        if maxsize is None:
            maxsize = configuration.connection_pool_maxsize if configuration.connection_pool_maxsize is not None else 4

        # 设置连接限制
        limits = httpx.Limits(max_connections=maxsize, max_keepalive_connections=pools_size)

        # 设置 SSL 配置
        verify = configuration.ssl_ca_cert or True  # 如果提供了自定义 CA 证书则使用，否则默认启用 SSL 验证
        if not configuration.verify_ssl:
            verify = False  # 如果明确指定不进行 SSL 验证，则设置为 False

        # 设置代理
        proxies = None
        if configuration.proxy:
            proxies = {
                'http://': configuration.proxy,
                'https://': configuration.proxy,
            }

        # 创建 httpx 客户端
        self.client = httpx.Client(
            limits=limits,
            verify=verify,
            proxies=proxies,
        )

        # 如果有提供客户端证书，设置之
        if configuration.cert_file and configuration.key_file:
            self.client.cert = (configuration.cert_file, configuration.key_file)

    def request(self, method, url, query_params=None, headers=None,
                body=None, post_params=None, _preload_content=True,
                _request_timeout=None):
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
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS']

        if post_params and body:
            raise ValueError("body parameter cannot be used with post_params parameter.")

        headers = headers or {}
        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        request_body = json.dumps(body) if body is not None else None

        try:
            r = self.client.request(
                method, url,
                params=query_params,
                headers=headers,
                content=request_body,
                timeout=_request_timeout
            )
        except HTTPError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

        if not 200 <= r.status <= 299:
            raise ApiException(http_resp=r)

        return r

    def GET(self, url, headers=None, query_params=None, _preload_content=True,
            _request_timeout=None):
        return self.request("GET", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def HEAD(self, url, headers=None, query_params=None, _preload_content=True,
             _request_timeout=None):
        return self.request("HEAD", url,
                            headers=headers,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            query_params=query_params)

    def OPTIONS(self, url, headers=None, query_params=None, post_params=None,
                body=None, _preload_content=True, _request_timeout=None):
        return self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def DELETE(self, url, headers=None, query_params=None, body=None,
               _preload_content=True, _request_timeout=None):
        return self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def POST(self, url, headers=None, query_params=None, post_params=None,
             body=None, _preload_content=True, _request_timeout=None):
        return self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PUT(self, url, headers=None, query_params=None, post_params=None,
            body=None, _preload_content=True, _request_timeout=None):
        return self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    def PATCH(self, url, headers=None, query_params=None, post_params=None,
              body=None, _preload_content=True, _request_timeout=None):
        return self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)


class RESTAsyncClientObject(object):

    def __init__(self, configuration, pools_size=4, maxsize=None):
        cert = None
        if configuration.cert_file and configuration.key_file:
            cert = (configuration.cert_file, configuration.key_file)
        self.client = httpx.AsyncClient(
            proxies=configuration.proxy,
            verify=configuration.verify_ssl,
            cert=cert,
            http1=True
        )

    async def request(self, method, url, query_params=None, headers=None,
                      body=None, post_params=None, _preload_content=True,
                      _request_timeout=None):
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
        assert method in ['GET', 'HEAD', 'DELETE', 'POST', 'PUT', 'PATCH', 'OPTIONS']

        if post_params and body:
            raise ValueError("body parameter cannot be used with post_params parameter.")

        headers = headers or {}
        if 'Content-Type' not in headers:
            headers['Content-Type'] = 'application/json'

        request_body = json.dumps(body) if body is not None else None

        try:
            r = await self.client.request(
                method, url,
                params=query_params,
                headers=headers,
                content=request_body,
                timeout=_request_timeout
            )
        except HTTPError as e:
            msg = "{0}\n{1}".format(type(e).__name__, str(e))
            raise ApiException(status=0, reason=msg)

        if _preload_content:
            r = RESTResponse(r)

        if not 200 <= r.status <= 299:
            raise ApiException(http_resp=r)

        return r

    async def GET(self, url, headers=None, query_params=None, _preload_content=True,
                  _request_timeout=None):
        return await self.request("GET", url,
                                  headers=headers,
                                  _preload_content=_preload_content,
                                  _request_timeout=_request_timeout,
                                  query_params=query_params)

    async def HEAD(self, url, headers=None, query_params=None, _preload_content=True,
                   _request_timeout=None):
        return await self.request("HEAD", url,
                                  headers=headers,
                                  _preload_content=_preload_content,
                                  _request_timeout=_request_timeout,
                                  query_params=query_params)

    async def OPTIONS(self, url, headers=None, query_params=None, post_params=None,
                body=None, _preload_content=True, _request_timeout=None):
        return await self.request("OPTIONS", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    async def DELETE(self, url, headers=None, query_params=None, body=None,
               _preload_content=True, _request_timeout=None):
        return await self.request("DELETE", url,
                            headers=headers,
                            query_params=query_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    async def POST(self, url, headers=None, query_params=None, post_params=None,
             body=None, _preload_content=True, _request_timeout=None):
        return await self.request("POST", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    async def PUT(self, url, headers=None, query_params=None, post_params=None,
            body=None, _preload_content=True, _request_timeout=None):
        return await self.request("PUT", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)

    async def PATCH(self, url, headers=None, query_params=None, post_params=None,
              body=None, _preload_content=True, _request_timeout=None):
        return await self.request("PATCH", url,
                            headers=headers,
                            query_params=query_params,
                            post_params=post_params,
                            _preload_content=_preload_content,
                            _request_timeout=_request_timeout,
                            body=body)


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
        error_message = "({0})\n" \
                        "Reason: {1}\n".format(self.status, self.reason)
        if self.headers:
            error_message += "HTTP response headers: {0}\n".format(
                self.headers)

        if self.body:
            error_message += "HTTP response body: {0}\n".format(self.body)

        return error_message
