# swagger_client.RetrievalApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_collection**](RetrievalApi.md#create_collection) | **POST** /api/v1/collections | Create collection
[**create_record**](RetrievalApi.md#create_record) | **POST** /api/v1/collections/{collection_id}/records | Create record
[**delete_collection**](RetrievalApi.md#delete_collection) | **DELETE** /api/v1/collections/{collection_id} | Delete collection
[**delete_record**](RetrievalApi.md#delete_record) | **DELETE** /api/v1/collections/{collection_id}/records/{record_id} | Delete record
[**get_collection**](RetrievalApi.md#get_collection) | **GET** /api/v1/collections/{collection_id} | Get collection
[**get_record**](RetrievalApi.md#get_record) | **GET** /api/v1/collections/{collection_id}/records/{record_id} | Get record
[**list_collections**](RetrievalApi.md#list_collections) | **GET** /api/v1/collections | List collections
[**list_records**](RetrievalApi.md#list_records) | **GET** /api/v1/collections/{collection_id}/records | List records
[**query_chunks**](RetrievalApi.md#query_chunks) | **POST** /api/v1/collections/{collection_id}/chunks/params | Query chunks
[**update_collection**](RetrievalApi.md#update_collection) | **POST** /api/v1/collections/{collection_id} | Update collection
[**update_record**](RetrievalApi.md#update_record) | **POST** /api/v1/collections/{collection_id}/records/{record_id} | Update record

# **create_collection**
> CollectionCreateResponseSchema create_collection(body)

Create collection

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.RetrievalApi()
body = taskingai.CollectionCreateRequestBodySchema()  # CollectionCreateRequestBodySchema | 

try:
    # Create collection
    api_response = api_instance.create_collection(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetrievalApi->create_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionCreateRequestBodySchema**](CollectionCreateRequestBodySchema.md)|  | 

### Return type

[**CollectionCreateResponseSchema**](CollectionCreateResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_record**
> RecordCreateResponseSchema create_record(body, collection_id)

Create record

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.RetrievalApi()
body = taskingai.RecordCreateRequestBodySchema()  # RecordCreateRequestBodySchema | 
collection_id = NULL  # object | 

try:
    # Create record
    api_response = api_instance.create_record(body, collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetrievalApi->create_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordCreateRequestBodySchema**](RecordCreateRequestBodySchema.md)|  | 
 **collection_id** | [**object**](.md)|  | 

### Return type

[**RecordCreateResponseSchema**](RecordCreateResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_collection**
> BaseSuccessEmptyOutSchema delete_collection(collection_id)

Delete collection

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.RetrievalApi()
collection_id = NULL  # object | 

try:
    # Delete collection
    api_response = api_instance.delete_collection(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetrievalApi->delete_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | [**object**](.md)|  | 

### Return type

[**BaseSuccessEmptyOutSchema**](BaseSuccessEmptyOutSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **delete_record**
> BaseSuccessEmptyOutSchema delete_record(collection_id, record_id)

Delete record

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.RetrievalApi()
collection_id = NULL  # object | 
record_id = NULL  # object | 

try:
    # Delete record
    api_response = api_instance.delete_record(collection_id, record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetrievalApi->delete_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | [**object**](.md)|  | 
 **record_id** | [**object**](.md)|  | 

### Return type

[**BaseSuccessEmptyOutSchema**](BaseSuccessEmptyOutSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_collection**
> CollectionGetResponseSchema get_collection(collection_id)

Get collection

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.RetrievalApi()
collection_id = NULL  # object | 

try:
    # Get collection
    api_response = api_instance.get_collection(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetrievalApi->get_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | [**object**](.md)|  | 

### Return type

[**CollectionGetResponseSchema**](CollectionGetResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_record**
> RecordGetResponseSchema get_record(collection_id, record_id)

Get record

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.RetrievalApi()
collection_id = NULL  # object | 
record_id = NULL  # object | 

try:
    # Get record
    api_response = api_instance.get_record(collection_id, record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetrievalApi->get_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | [**object**](.md)|  | 
 **record_id** | [**object**](.md)|  | 

### Return type

[**RecordGetResponseSchema**](RecordGetResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_collections**
> CollectionListResponseSchema list_collections()

List collections

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.RetrievalApi()

try:
    # List collections
    api_response = api_instance.list_collections()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetrievalApi->list_collections: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**CollectionListResponseSchema**](CollectionListResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_records**
> RecordListResponseSchema list_records(collection_id)

List records

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.RetrievalApi()
collection_id = NULL  # object | 

try:
    # List records
    api_response = api_instance.list_records(collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetrievalApi->list_records: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collection_id** | [**object**](.md)|  | 

### Return type

[**RecordListResponseSchema**](RecordListResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **query_chunks**
> ChunkQueryResponseSchema query_chunks(body, collection_id)

Query chunks

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.RetrievalApi()
body = taskingai.ChunkQueryRequestBodySchema()  # ChunkQueryRequestBodySchema | 
collection_id = NULL  # object | 

try:
    # Query chunks
    api_response = api_instance.query_chunks(body, collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetrievalApi->query_chunks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ChunkQueryRequestBodySchema**](ChunkQueryRequestBodySchema.md)|  | 
 **collection_id** | [**object**](.md)|  | 

### Return type

[**ChunkQueryResponseSchema**](ChunkQueryResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_collection**
> CollectionUpdateResponseSchema update_collection(body, collection_id)

Update collection

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.RetrievalApi()
body = taskingai.CollectionUpdateRequestBodySchema()  # CollectionUpdateRequestBodySchema | 
collection_id = NULL  # object | 

try:
    # Update collection
    api_response = api_instance.update_collection(body, collection_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetrievalApi->update_collection: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CollectionUpdateRequestBodySchema**](CollectionUpdateRequestBodySchema.md)|  | 
 **collection_id** | [**object**](.md)|  | 

### Return type

[**CollectionUpdateResponseSchema**](CollectionUpdateResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **update_record**
> RecordUpdateResponseSchema update_record(body, collection_id, record_id)

Update record

### Example

```python
from __future__ import print_function
import time
import taskingai
from taskingai.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = taskingai.RetrievalApi()
body = taskingai.RecordUpdateRequestBodySchema()  # RecordUpdateRequestBodySchema | 
collection_id = NULL  # object | 
record_id = NULL  # object | 

try:
    # Update record
    api_response = api_instance.update_record(body, collection_id, record_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RetrievalApi->update_record: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**RecordUpdateRequestBodySchema**](RecordUpdateRequestBodySchema.md)|  | 
 **collection_id** | [**object**](.md)|  | 
 **record_id** | [**object**](.md)|  | 

### Return type

[**RecordUpdateResponseSchema**](RecordUpdateResponseSchema.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

