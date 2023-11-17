# Record

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | **object** | The object type, which is always &#x60;Retrieval.Record&#x60;. | 
**record_id** | **object** | The record ID. | 
**collection_id** | **object** | The collection ID. | 
**type** | **object** | The record type, which is always &#x60;text&#x60; or &#x60;file&#x60;. | 
**num_chunks** | **object** | The number of chunks in the record. | 
**text** | **object** | The record text. It&#x27;s only valid when the record type is &#x60;text&#x60;. | 
**metadata** | **object** | The record metadata. It can store up to 16 key-value pairs where each key&#x27;s length is less than 64 and value&#x27;s length is less than 512. | 
**created_timestamp** | **object** | The timestamp when the record was created. | 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

