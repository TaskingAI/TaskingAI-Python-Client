import time
import pytest

from taskingai.retrieval import list_collections, create_collection, get_collection, update_collection, delete_collection, list_records, create_text_record, get_record, update_record, delete_record, query_chunks
from test.config import embedding_model_id, sleep_time
from test.common.logger import logger


@pytest.mark.test_sync
class TestCollection:

    collection_list = ['object', 'collection_id',  'name', 'description', 'num_records', 'num_chunks', 'capacity',
                       'embedding_model_id', 'metadata', 'configs', 'created_timestamp', "status"]
    collection_keys = set(collection_list)
    collection_configs = ["metric", "chunk_size", "chunk_overlap"]
    collection_configs_keys = set(collection_configs)

    @pytest.mark.run(order=9)
    def test_create_collection(self):

        # Create a collection.
        name = "test"
        description = "just for test"
        for x in range(2):
            res = create_collection(name=name, description=description, embedding_model_id=embedding_model_id, capacity=1000)
            res_dict = res.to_dict()
            logger.info(res_dict)
            pytest.assume(res_dict.keys() == self.collection_keys)
            pytest.assume(res_dict["configs"].keys() == self.collection_configs_keys)
            pytest.assume(res_dict["name"] == name)
            pytest.assume(res_dict["description"] == description)
            pytest.assume(res_dict["embedding_model_id"] == embedding_model_id)
            pytest.assume(res_dict["capacity"] == 1000)
            pytest.assume(res_dict["status"] == "creating")


    @pytest.mark.run(order=10)
    def test_list_collections(self):

        # List collections.

        nums_limit = 1
        res = list_collections(limit=nums_limit)
        pytest.assume(len(res) == nums_limit)
        after_id = res[-1].collection_id
        after_res = list_collections(limit=nums_limit, after=after_id)
        pytest.assume(len(after_res) == nums_limit)
        twice_nums_list = list_collections(limit=nums_limit * 2)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])
        before_id = after_res[0].collection_id
        before_res = list_collections(limit=nums_limit, before=before_id)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=11)
    def test_get_collection(self, collection_id):

        # Get a collection.

        res = get_collection(collection_id=collection_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.collection_keys)
        pytest.assume(res_dict["configs"].keys() == self.collection_configs_keys)
        pytest.assume(res_dict["status"] == "ready")

    @pytest.mark.run(order=12)
    def test_update_collection(self, collection_id):

        # Update a collection.

        name = "openai"
        description = "test for openai"
        res = update_collection(collection_id=collection_id, name=name, description=description)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.collection_keys)
        pytest.assume(res_dict["configs"].keys() == self.collection_configs_keys)
        pytest.assume(res_dict["name"] == name)
        pytest.assume(res_dict["description"] == description)
        pytest.assume(res_dict["status"] == "ready")

    @pytest.mark.run(order=35)
    def test_delete_collection(self):

        # List collections.

        old_res = list_collections(order="desc", limit=100,  after=None, before=None)
        old_nums = len(old_res)

        for index, collection in enumerate(old_res):
            collection_id = collection.collection_id

            # Delete a collection.

            delete_collection(collection_id=collection_id)

            new_collections = list_collections(order="desc", limit=100,  after=None, before=None)

            # List collections.

            collection_ids = [collection.collection_id for collection in new_collections]
            pytest.assume(collection_id not in collection_ids)
            new_nums = len(new_collections)
            pytest.assume(new_nums == old_nums - 1 - index)


@pytest.mark.test_sync
class TestRecord:

    record_list = ['record_id', 'collection_id', 'num_chunks', 'content', 'metadata', 'type', 'object',
                   'created_timestamp', 'status']
    record_keys = set(record_list)
    record_content = ["text"]
    record_content_keys = set(record_content)
    
    @pytest.mark.run(order=13)
    def test_create_text_record(self, collection_id):

        # Create a text record.

        text = "Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
        for x in range(2):
            res = create_text_record(collection_id=collection_id, text=text)
            res_dict = res.to_dict()
            pytest.assume(res_dict.keys() == self.record_keys)
            pytest.assume(res_dict["content"].keys() == self.record_content_keys)
            pytest.assume(res_dict["content"]["text"] == text)
            pytest.assume(res_dict["status"] == "creating")

    @pytest.mark.run(order=14)
    def test_list_records(self, collection_id):

        # List records.

        nums_limit = 1
        res = list_records(limit=nums_limit, collection_id=collection_id)
        pytest.assume(len(res) == nums_limit)

        after_id = res[-1].record_id
        after_res = list_records(limit=nums_limit, after=after_id, collection_id=collection_id)
        pytest.assume(len(after_res) == nums_limit)

        twice_nums_list = list_records(limit=nums_limit * 2, collection_id=collection_id)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])

        before_id = after_res[0].record_id
        before_res = list_records(limit=nums_limit, before=before_id, collection_id=collection_id)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=15)
    def test_get_record(self, collection_id):

        # list records

        records = list_records(collection_id=collection_id)
        for record in records:
            record_id = record.record_id
            res = get_record(collection_id=collection_id, record_id=record_id)
            logger.info(f'get record response: {res}')
            res_dict = res.to_dict()
            pytest.assume(res_dict.keys() == self.record_keys)
            pytest.assume(res_dict["content"].keys() == self.record_content_keys)
            pytest.assume(res_dict["status"] == "creating" or "ready")

    @pytest.mark.run(order=16)
    def test_update_record(self, collection_id, record_id):

        # Update a record.

        metadata = {"test": "test"}
        res = update_record(collection_id=collection_id, record_id=record_id, metadata=metadata)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.record_keys)
        pytest.assume(res_dict["content"].keys() == self.record_content_keys)
        pytest.assume(res_dict["metadata"] == metadata)


    @pytest.mark.run(order=34)
    def test_delete_record(self, collection_id):

        # List records.

        records = list_records(collection_id=collection_id, order="desc", limit=20,  after=None,
                               before=None)
        old_nums = len(records)
        for index, record in enumerate(records):
            record_id = record.record_id

            # Delete a record.

            delete_record(collection_id=collection_id, record_id=record_id)

            # List records.

            new_records = list_records(collection_id=collection_id, order="desc", limit=20,  after=None,
                                       before=None)
            record_ids = [record.record_id for record in new_records]
            pytest.assume(record_id not in record_ids)
            new_nums = len(new_records)
            pytest.assume(new_nums == old_nums - 1 - index)


@pytest.mark.test_sync
class TestChunk:

    chunk_list = ['chunk_id', 'collection_id', 'record_id',  'object', 'text', 'score']
    chunk_keys = set(chunk_list)

    @pytest.mark.run(order=17)
    def test_query_chunks(self, collection_id):

        # Query chunks.

        query_text = "Machine learning"
        top_k = 2
        res = query_chunks(collection_id=collection_id, query_text=query_text, top_k=top_k)
        pytest.assume(len(res) == top_k)
        for chunk in res:
            chunk_dict = chunk.to_dict()
            pytest.assume(chunk_dict.keys() == self.chunk_keys)
            pytest.assume(query_text in chunk_dict["text"])
            pytest.assume(chunk_dict["score"] >= 0)

