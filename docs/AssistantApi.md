# swagger_client.AssistantApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_assistant**](AssistantApi.md#create_assistant) | **POST** /api/v1/assistants | Create assistant
[**create_chat**](AssistantApi.md#create_chat) | **POST** /api/v1/assistants/{assistant_id}/chats | Create chat
[**delete_assistant**](AssistantApi.md#delete_assistant) | **DELETE** /api/v1/assistants/{assistant_id} | Delete assistant
[**delete_chat**](AssistantApi.md#delete_chat) | **DELETE** /api/v1/assistants/{assistant_id}/chats/{chat_id} | Delete chat
[**generate**](AssistantApi.md#generate) | **POST** /api/v1/assistants/{assistant_id}/chats/{chat_id}/generate | Generate
[**get_assistant**](AssistantApi.md#get_assistant) | **GET** /api/v1/assistants/{assistant_id} | Get assistant
[**get_chat**](AssistantApi.md#get_chat) | **GET** /api/v1/assistants/{assistant_id}/chats/{chat_id} | Get chat
[**get_message**](AssistantApi.md#get_message) | **GET** /api/v1/assistants/{assistant_id}/chats/{chat_id}/messages/{message_id} | Get message
[**list_assistants**](AssistantApi.md#list_assistants) | **GET** /api/v1/assistants | List assistants
[**list_chats**](AssistantApi.md#list_chats) | **GET** /api/v1/assistants/{assistant_id}/chats | List chats
[**list_messages**](AssistantApi.md#list_messages) | **GET** /api/v1/assistants/{assistant_id}/chats/{chat_id}/messages | List messages
[**update_assistant**](AssistantApi.md#update_assistant) | **POST** /api/v1/assistants/{assistant_id} | Update assistant
[**update_chat**](AssistantApi.md#update_chat) | **POST** /api/v1/assistants/{assistant_id}/chats/{chat_id} | Update chat
[**update_message**](AssistantApi.md#update_message) | **POST** /api/v1/assistants/{assistant_id}/chats/{chat_id}/messages/{message_id} | Update message

# **create_assistant**
> AssistantCreateResponseSchema create_assistant(body)

Create assistant

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
body = taskingai.AssistantCreateRequestBodySchema()  # AssistantCreateRequestBodySchema | 

try:
    # Create assistant
    api_response = api_instance.create_assistant(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->create_assistant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssistantCreateRequestBodySchema**](AssistantCreateRequestBodySchema.md)|  | 

### Return type

[**AssistantCreateResponseSchema**](AssistantCreateResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_chat**
> ChatCreateResponseSchema create_chat(body, assistant_id)

Create chat

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
body = taskingai.ChatCreateRequestBodySchema()  # ChatCreateRequestBodySchema | 
assistant_id = NULL  # object | 

try:
    # Create chat
    api_response = api_instance.create_chat(body, assistant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->create_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChatCreateRequestBodySchema**](ChatCreateRequestBodySchema.md)|  | 
 **assistant_id** | [**object**](.md)|  | 

### Return type

[**ChatCreateResponseSchema**](ChatCreateResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_assistant**
> BaseSuccessEmptyOutSchema delete_assistant(assistant_id)

Delete assistant

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
assistant_id = NULL  # object | 

try:
    # Delete assistant
    api_response = api_instance.delete_assistant(assistant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->delete_assistant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assistant_id** | [**object**](.md)|  | 

### Return type

[**BaseSuccessEmptyOutSchema**](BaseSuccessEmptyOutSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_chat**
> BaseSuccessEmptyOutSchema delete_chat(assistant_id, chat_id)

Delete chat

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
assistant_id = NULL  # object | 
chat_id = NULL  # object | 

try:
    # Delete chat
    api_response = api_instance.delete_chat(assistant_id, chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->delete_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assistant_id** | [**object**](.md)|  | 
 **chat_id** | [**object**](.md)|  | 

### Return type

[**BaseSuccessEmptyOutSchema**](BaseSuccessEmptyOutSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **generate**
> ChatGenerateResponseSchema generate(body, assistant_id, chat_id)

Generate

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
body = taskingai.ChatGenerateRequestBodySchema()  # ChatGenerateRequestBodySchema | 
assistant_id = NULL  # object | 
chat_id = NULL  # object | 

try:
    # Generate
    api_response = api_instance.generate(body, assistant_id, chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->generate: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChatGenerateRequestBodySchema**](ChatGenerateRequestBodySchema.md)|  | 
 **assistant_id** | [**object**](.md)|  | 
 **chat_id** | [**object**](.md)|  | 

### Return type

[**ChatGenerateResponseSchema**](ChatGenerateResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_assistant**
> AssistantGetResponseSchema get_assistant(assistant_id)

Get assistant

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
assistant_id = NULL  # object | 

try:
    # Get assistant
    api_response = api_instance.get_assistant(assistant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->get_assistant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assistant_id** | [**object**](.md)|  | 

### Return type

[**AssistantGetResponseSchema**](AssistantGetResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_chat**
> ChatGetResponseSchema get_chat(assistant_id, chat_id)

Get chat

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
assistant_id = NULL  # object | 
chat_id = NULL  # object | 

try:
    # Get chat
    api_response = api_instance.get_chat(assistant_id, chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->get_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assistant_id** | [**object**](.md)|  | 
 **chat_id** | [**object**](.md)|  | 

### Return type

[**ChatGetResponseSchema**](ChatGetResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_message**
> MessageGetResponseSchema get_message(assistant_id, chat_id, message_id)

Get message

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
assistant_id = NULL  # object | 
chat_id = NULL  # object | 
message_id = NULL  # object | 

try:
    # Get message
    api_response = api_instance.get_message(assistant_id, chat_id, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->get_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assistant_id** | [**object**](.md)|  | 
 **chat_id** | [**object**](.md)|  | 
 **message_id** | [**object**](.md)|  | 

### Return type

[**MessageGetResponseSchema**](MessageGetResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_assistants**
> AssistantListResponseSchema list_assistants(limit=limit, order=order, after=after, before=before, offset=offset)

List assistants

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
limit = 20  # object |  (optional) (default to 20)
order = desc  # object |  (optional) (default to desc)
after = NULL  # object |  (optional)
before = NULL  # object |  (optional)
offset = NULL  # object |  (optional)

try:
    # List assistants
    api_response = api_instance.list_assistants(limit=limit, order=order, after=after, before=before, offset=offset)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->list_assistants: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | [**object**](.md)|  | [optional] [default to 20]
 **order** | [**object**](.md)|  | [optional] [default to desc]
 **after** | [**object**](.md)|  | [optional] 
 **before** | [**object**](.md)|  | [optional] 
 **offset** | [**object**](.md)|  | [optional] 

### Return type

[**AssistantListResponseSchema**](AssistantListResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_chats**
> ChatListResponseSchema list_chats(assistant_id)

List chats

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
assistant_id = NULL  # object | 

try:
    # List chats
    api_response = api_instance.list_chats(assistant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->list_chats: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assistant_id** | [**object**](.md)|  | 

### Return type

[**ChatListResponseSchema**](ChatListResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_messages**
> MessageListResponseSchema list_messages(assistant_id, chat_id, limit=limit, order=order, after=after, before=before)

List messages

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
assistant_id = NULL  # object | 
chat_id = NULL  # object | 
limit = 20  # object |  (optional) (default to 20)
order = desc  # object |  (optional) (default to desc)
after = NULL  # object |  (optional)
before = NULL  # object |  (optional)

try:
    # List messages
    api_response = api_instance.list_messages(assistant_id, chat_id, limit=limit, order=order, after=after,
                                              before=before)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->list_messages: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **assistant_id** | [**object**](.md)|  | 
 **chat_id** | [**object**](.md)|  | 
 **limit** | [**object**](.md)|  | [optional] [default to 20]
 **order** | [**object**](.md)|  | [optional] [default to desc]
 **after** | [**object**](.md)|  | [optional] 
 **before** | [**object**](.md)|  | [optional] 

### Return type

[**MessageListResponseSchema**](MessageListResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_assistant**
> AssistantUpdateResponseSchema update_assistant(body, assistant_id)

Update assistant

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
body = taskingai.AssistantUpdateRequestBodySchema()  # AssistantUpdateRequestBodySchema | 
assistant_id = NULL  # object | 

try:
    # Update assistant
    api_response = api_instance.update_assistant(body, assistant_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->update_assistant: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AssistantUpdateRequestBodySchema**](AssistantUpdateRequestBodySchema.md)|  | 
 **assistant_id** | [**object**](.md)|  | 

### Return type

[**AssistantUpdateResponseSchema**](AssistantUpdateResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_chat**
> ChatUpdateResponseSchema update_chat(body, assistant_id, chat_id)

Update chat

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
body = taskingai.ChatUpdateRequestBodySchema()  # ChatUpdateRequestBodySchema | 
assistant_id = NULL  # object | 
chat_id = NULL  # object | 

try:
    # Update chat
    api_response = api_instance.update_chat(body, assistant_id, chat_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->update_chat: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChatUpdateRequestBodySchema**](ChatUpdateRequestBodySchema.md)|  | 
 **assistant_id** | [**object**](.md)|  | 
 **chat_id** | [**object**](.md)|  | 

### Return type

[**ChatUpdateResponseSchema**](ChatUpdateResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_message**
> MessageUpdateResponseSchema update_message(body, assistant_id, chat_id, message_id)

Update message

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.AssistantApi()
body = taskingai.MessageUpdateRequestBodySchema()  # MessageUpdateRequestBodySchema | 
assistant_id = NULL  # object | 
chat_id = NULL  # object | 
message_id = NULL  # object | 

try:
    # Update message
    api_response = api_instance.update_message(body, assistant_id, chat_id, message_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AssistantApi->update_message: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**MessageUpdateRequestBodySchema**](MessageUpdateRequestBodySchema.md)|  | 
 **assistant_id** | [**object**](.md)|  | 
 **chat_id** | [**object**](.md)|  | 
 **message_id** | [**object**](.md)|  | 

### Return type

[**MessageUpdateResponseSchema**](MessageUpdateResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

