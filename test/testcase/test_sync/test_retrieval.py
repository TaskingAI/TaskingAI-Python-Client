import time
import allure
import pytest

from taskingai.retrieval import list_collections, create_collection, get_collection, update_collection, delete_collection, list_records, create_text_record, get_record, update_record, delete_record, query_chunks
from test.config import text_model_id, sleep_time
from test.common.utils import logger


@allure.epic("test_sync_retrieval")
@allure.feature("test_collection")
@pytest.mark.sync
class TestCollection:

    collection_list = ['object', 'collection_id',  'name', 'description', 'num_records', 'num_chunks', 'capacity',
                       'embedding_model_id', 'metadata', 'configs', 'created_timestamp', "status"]
    collection_keys = set(collection_list)
    collection_configs = ["metric", "chunk_size", "chunk_overlap"]
    collection_configs_keys = set(collection_configs)

    @allure.story("test_create_collection")
    @pytest.mark.run(order=9)
    @pytest.mark.parametrize("sync_collection_num", (x+1 for x in range(10)))
    def test_create_collection(self, sync_collection_num):
        # List collections.
        old_res = list_collections(limit=100)
        old_nums = len(old_res)
        # Create a collection.
        name = f"test{sync_collection_num}"
        description = "just for test"
        res = create_collection(name=name, description=description, embedding_model_id=text_model_id, capacity=1000)
        res_dict = res.to_dict()
        logger.info(res_dict)
        pytest.assume(res_dict.keys() == self.collection_keys)
        pytest.assume(res_dict["configs"].keys() == self.collection_configs_keys)
        pytest.assume(res_dict["name"] == name)
        pytest.assume(res_dict["description"] == description)
        pytest.assume(res_dict["embedding_model_id"] == text_model_id)
        pytest.assume(res_dict["capacity"] == 1000)
        pytest.assume(res_dict["status"] == "creating")

        # Get a collection.
        time.sleep(sleep_time)
        collection_id = res_dict["collection_id"]
        get_res = get_collection(collection_id=collection_id)
        get_res_dict = get_res.to_dict()
        logger.info(get_res_dict)
        pytest.assume(get_res_dict.keys() == self.collection_keys)
        pytest.assume(get_res_dict["configs"].keys() == self.collection_configs_keys)
        pytest.assume(get_res_dict["name"] == name)
        pytest.assume(get_res_dict["description"] == description)
        pytest.assume(get_res_dict["embedding_model_id"] == text_model_id)
        pytest.assume(get_res_dict["capacity"] == 1000)
        pytest.assume(get_res_dict["status"] == "ready")
        # List collections.
        new_res = list_collections(limit=100)
        new_nums = len(new_res)
        pytest.assume(new_nums == old_nums + 1)

    @allure.story("test_list_collections")
    @pytest.mark.run(order=10)
    def test_list_collections(self,):
        # List collections.
        nums_limit = 4
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

    @allure.story("test_get_collection")
    @pytest.mark.run(order=11)
    def test_get_collection(self, collection_id):
        # Get a collection.
        res = get_collection(collection_id=collection_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.collection_keys)
        pytest.assume(res_dict["configs"].keys() == self.collection_configs_keys)
        pytest.assume(res_dict["status"] == "ready")

    @allure.story("test_update_collection")
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
        # Get a collection.
        time.sleep(sleep_time)
        get_res = get_collection(collection_id=collection_id)
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.collection_keys)
        pytest.assume(get_res_dict["configs"].keys() == self.collection_configs_keys)
        pytest.assume(get_res_dict["name"] == name)
        pytest.assume(get_res_dict["description"] == description)
        pytest.assume(get_res_dict["status"] == "ready")

    @allure.story("test_delete_collection")
    @pytest.mark.run(order=34)
    def test_delete_collection(self):
        # List collections.
        old_res = list_collections(order="desc", limit=100,  after=None, before=None)
        old_nums = len(old_res)

        for index, collection in enumerate(old_res):
            collection_id = collection.collection_id
            # Delete a collection.
            delete_collection(collection_id=collection_id)
            time.sleep(sleep_time)
            new_collections = list_collections(order="desc", limit=100,  after=None, before=None)
            # List collections.
            collection_ids = [collection.collection_id for collection in new_collections]
            pytest.assume(collection_id not in collection_ids)
            new_nums = len(new_collections)
            pytest.assume( new_nums == old_nums - 1 - index)


@allure.epic("test_sync_retrieval")
@allure.feature("test_record")
@pytest.mark.sync
class TestRecord:

    record_list = ['record_id', 'collection_id', 'num_chunks', 'content', 'metadata', 'type', 'object',
                   'created_timestamp', 'status']
    record_keys = set(record_list)
    record_content = ["text"]
    record_content_keys = set(record_content)
    
    @allure.story("test_create_text_record")
    @pytest.mark.run(order=13)
    @pytest.mark.parametrize("sync_record_num", (x+1 for x in range(10)))
    def test_create_text_record(self, collection_id, sync_record_num):
        # List records.
        old_res = list_records(collection_id=collection_id)
        old_nums = len(old_res)
        # Create a text record.
        text = f"{sync_record_num}Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
        res = create_text_record(collection_id=collection_id, text=text)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.record_keys)
        pytest.assume(res_dict["content"].keys() == self.record_content_keys)
        pytest.assume(res_dict["content"]["text"] == text)
        pytest.assume(res_dict["status"] == "creating")
        # Get a record.  cost too many times, so do it in test_get_record
        # time.sleep(sleep_time*8)
        # record_id = res_dict["record_id"]
        #
        # get_res = get_record(collection_id=collection_id, record_id=record_id)
        # logger.info(f'get record response: {get_res}')
        # get_res_dict = get_res.to_dict()
        # pytest.assume(get_res_dict.keys() == self.record_keys)
        # pytest.assume(get_res_dict["content"].keys() == self.record_content_keys)
        # pytest.assume(get_res_dict["content"]["text"] == text)
        # pytest.assume(get_res_dict["status"] == "ready")
        # List records.
        new_res = list_records(collection_id=collection_id)
        new_nums = len(new_res)
        pytest.assume(new_nums == old_nums + 1)

    @allure.story("test_list_records")
    @pytest.mark.run(order=14)
    def test_list_records(self, collection_id):
        # List records.
        nums_limit = 4
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

    @allure.story("test_get_record")
    @pytest.mark.run(order=15)
    def test_get_record(self, collection_id):
        # list records
        time.sleep(sleep_time*15)
        records = list_records(collection_id=collection_id)
        for record in records:
            record_id = record.record_id
            res = get_record(collection_id=collection_id, record_id=record_id)
            logger.info(f'get record response: {res}')
            res_dict = res.to_dict()
            pytest.assume(res_dict.keys() == self.record_keys)
            pytest.assume(res_dict["content"].keys() == self.record_content_keys)
            pytest.assume(res_dict["status"] == "ready")

    @allure.story("test_update_record")
    @pytest.mark.run(order=16)
    def test_update_record(self, collection_id, record_id):
        # Update a record.
        metadata = {"test": "test"}
        res = update_record(collection_id=collection_id, record_id=record_id, metadata=metadata)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.record_keys)
        pytest.assume(res_dict["content"].keys() == self.record_content_keys)
        pytest.assume(res_dict["metadata"] == metadata)
        # Get a record.
        time.sleep(sleep_time*4)
        get_res = get_record(collection_id=collection_id, record_id=record_id)
        logger.info(f'get record response: {get_res}')
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.record_keys)
        pytest.assume(get_res_dict["content"].keys() == self.record_content_keys)
        pytest.assume(get_res_dict["metadata"] == metadata)
        pytest.assume(get_res_dict["status"] == "ready")

    @allure.story("test_create_record_in_nonexistent_collection")
    @pytest.mark.run(order=17)
    @pytest.mark.abnormal
    def test_create_record_in_nonexistent_collection(self):
        # Create collection.
        name = "test"
        description = "just for test"
        collection_id = "nonexistent_collection_id"
        # Create a record.
        text = "Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
        try:
            res = create_text_record(collection_id=collection_id, text=text)
        except Exception as e:
            logger.info(f'test_create_record_in_creating_collection:{e}')
            pytest.assume(f"Collection not found: {collection_id}" in str(e))

    @allure.story("test_create_record_in_creating_collection")
    @pytest.mark.run(order=17)
    @pytest.mark.abnormal
    def test_create_record_in_creating_collection(self):
        # Create collection.
        name = "test"
        description = "just for test"
        res = create_collection(name=name, description=description, embedding_model_id=text_model_id,
                                        capacity=1000)
        collection_id = res.collection_id
        # Create a record.
        text = "Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
        try:
            res = create_text_record(collection_id=collection_id, text=text)
        except Exception as e:
            logger.info(f'test_create_record_in_creating_collection:{e}')
            pytest.assume(f"Collection {collection_id} is not ready." in str(e))

    @allure.story("test_create_record_in_deleting_collection")
    @pytest.mark.run(order=17)
    @pytest.mark.abnormal
    def test_create_record_in_deleting_collection(self):
        # Create collection.
        name = "test"
        description = "just for test"
        res = create_collection(name=name, description=description, embedding_model_id=text_model_id,
                                        capacity=1000)
        collection_id = res.collection_id
        delete_collection(collection_id=collection_id)
        # Create a record.
        text = "Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
        try:
            res = create_text_record(collection_id=collection_id, text=text)
        except Exception as e:
            logger.info(f'test_create_record_in_creating_collection:{e}')
            pytest.assume(f"Collection not found: {collection_id}" in str(e))

    @allure.story("test_delete_record")
    @pytest.mark.run(order=33)
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


@allure.epic("test_sync_retrieval")
@allure.feature("test_chunk")
@pytest.mark.sync
class TestChunk:

    chunk_list = ['chunk_id', 'collection_id', 'record_id',  'object', 'text', 'score']
    chunk_keys = set(chunk_list)

    @allure.story("test_query_chunks")
    @pytest.mark.run(order=17)
    def test_query_chunks(self, collection_id):
        # Query chunks.
        query_text = "Machine learning"
        top_k = 5
        res = query_chunks(collection_id=collection_id, query_text=query_text, top_k=top_k)
        pytest.assume(len(res) == top_k)
        for chunk in res:
            chunk_dict = chunk.to_dict()
            pytest.assume(chunk_dict.keys() == self.chunk_keys)
            pytest.assume(query_text in chunk_dict["text"])
            pytest.assume(chunk_dict["score"] >= 0)

    @allure.story("test_query_chunks_in_creating_collection")
    @pytest.mark.run(order=17)
    @pytest.mark.abnormal
    def test_query_chunks_in_creating_collection(self):
        # Create collection.
        name = "test"
        description = "just for test"
        res = create_collection(name=name, description=description, embedding_model_id=text_model_id,
                                        capacity=1000)
        collection_id = res.collection_id
        # Query chunks
        query_text = "Machine learning"
        top_k = 1
        try:
            res = query_chunks(collection_id=collection_id, query_text=query_text, top_k=top_k)
        except Exception as e:
            logger.info(f'test_query_chunks_in_creating_collection:{res}')
            pytest.assume(f"Collection {collection_id} is not ready." in str(e))

    @allure.story("test_query_chunks_in_deleting_collection")
    @pytest.mark.run(order=17)
    @pytest.mark.abnormal
    def test_query_chunks_in_deleting_collection(self):
        # Create collection.
        name = "test"
        description = "just for test"
        collection_res = create_collection(name=name, description=description, embedding_model_id=text_model_id,
                                                   capacity=1000)
        collection_id = collection_res.collection_id
        # delete collection
        delete_collection(collection_id=collection_id)
        # Query chunks
        query_text = "Machine learning"
        top_k = 1
        try:
            res = query_chunks(collection_id=collection_id, query_text=query_text, top_k=top_k)
        except Exception as e:
            logger.info(f'test_query_chunks_in_deleting_collection:{e}')
            pytest.assume("Collections not found" in str(e))

    @allure.story("test_query_chunks_in_nonexistent_collection")
    @pytest.mark.run(order=17)
    @pytest.mark.abnormal
    def test_query_chunks_in_nonexistent_collection(self):
        # Query chunks
        query_text = "Machine learning"
        top_k = 1
        try:
            res = query_chunks(collection_id="nonexistent_collection_id", query_text=query_text, top_k=top_k)
        except Exception as e:
            logger.info(f'test_query_chunks_in_nonexistent_collection:{e}')
            pytest.assume('Collections not found' in str(e))
