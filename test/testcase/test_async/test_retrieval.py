import time
import asyncio
import allure
import pytest

from taskingai.retrieval import a_list_collections, a_create_collection, a_get_collection, a_update_collection, a_delete_collection, a_list_records, a_create_text_record, a_get_record, a_update_record, a_delete_record, a_query_chunks
from test.config import text_model_id
from test.common.utils import logger
from test.testcase.test_async.base import Base

@allure.epic("test_retrieval")
@allure.feature("test_collection")
@pytest.mark.a_sync
class TestCollection(Base):

    collection_list = ['object', 'collection_id',  'name', 'description', 'num_records', 'num_chunks', 'capacity',
                       'embedding_model_id', 'metadata', 'configs', 'created_timestamp', "status"]
    collection_keys = set(collection_list)
    collection_configs = ["metric", "chunk_size", "chunk_overlap"]
    collection_configs_keys = set(collection_configs)

    @allure.story("test_a_create_collection")
    @pytest.mark.run(order=9)
    @pytest.mark.asyncio
    async def test_a_create_collection(self):
        # List collections.
        old_res = await a_list_collections()
        old_nums = len(old_res)
        # Create a collection.
        name = "test"
        description = "just for test"
        res = await a_create_collection(name=name, description=description, embedding_model_id=text_model_id, capacity=1000)
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
        await asyncio.sleep(1)
        collection_id = res_dict["collection_id"]
        get_res = await a_get_collection(collection_id=collection_id)
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
        new_res = await a_list_collections()
        new_nums = len(new_res)
        assert new_nums == old_nums + 1

    @allure.story("test_a_list_collections")
    @pytest.mark.run(order=10)
    @pytest.mark.asyncio
    async def test_a_list_collections(self,):
        # List collections.
        res = await a_list_collections(order="desc", limit=20, offset=None, after=None, before=None)
        assert len(res) >= 0

    @allure.story("test_a_get_collection")
    @pytest.mark.run(order=11)
    @pytest.mark.asyncio
    async def test_a_get_collection(self, a_collection_id):
        # Get a collection.
        if not Base.collection_id:
            Base.collection_id = await a_collection_id
        res = await a_get_collection(collection_id=self.collection_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.collection_keys)
        pytest.assume(res_dict["configs"].keys() == self.collection_configs_keys)
        pytest.assume(res_dict["status"] == "ready")

    @allure.story("test_a_update_collection")
    @pytest.mark.run(order=12)
    @pytest.mark.asyncio
    async def test_a_update_collection(self):
        # Update a collection.
        name = "openai"
        description = "test for openai"
        res = await a_update_collection(collection_id=self.collection_id, name=name, description=description)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.collection_keys)
        pytest.assume(res_dict["configs"].keys() == self.collection_configs_keys)
        pytest.assume(res_dict["name"] == name)
        pytest.assume(res_dict["description"] == description)
        pytest.assume(res_dict["status"] == "ready")
        # Get a collection.
        get_res = await a_get_collection(collection_id=self.collection_id)
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.collection_keys)
        pytest.assume(get_res_dict["configs"].keys() == self.collection_configs_keys)
        pytest.assume(get_res_dict["name"] == name)
        pytest.assume(get_res_dict["description"] == description)
        pytest.assume(get_res_dict["status"] == "ready")

    @allure.story("test_a_delete_collection")
    @pytest.mark.run(order=34)
    @pytest.mark.asyncio
    async def test_a_delete_collection(self):
        # List collections.
        old_res = await a_list_collections(order="desc", limit=20, offset=None, after=None, before=None)
        old_nums = len(old_res)

        for index, collection in enumerate(old_res):
            collection_id = collection.collection_id
            # Delete a collection.
            await a_delete_collection(collection_id=collection_id)
            new_collections = await a_list_collections(order="desc", limit=20, offset=None, after=None, before=None)
            # List collections.
            collection_ids = [c.collection_id for c in new_collections]
            pytest.assume(collection_id not in collection_ids)
            new_nums = len(new_collections)
            assert new_nums == old_nums - 1 - index


@allure.epic("test_retrieval")
@allure.feature("test_record")
@pytest.mark.a_sync
class TestRecord(Base):

    record_list = ['record_id', 'collection_id', 'num_chunks', 'content', 'metadata', 'type', 'object',
                   'created_timestamp', 'status']
    record_keys = set(record_list)
    record_content = ["text"]
    record_content_keys = set(record_content)
    
    @allure.story("test_a_create_text_record")
    @pytest.mark.run(order=13)
    @pytest.mark.asyncio
    async def test_a_create_text_record(self):
        # List records.
        old_res = await a_list_records(collection_id=self.collection_id)
        old_nums = len(old_res)
        # Create a text record.
        text = "Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
        res = await a_create_text_record(collection_id=self.collection_id, text=text)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.record_keys)
        pytest.assume(res_dict["content"].keys() == self.record_content_keys)
        pytest.assume(res_dict["content"]["text"] == text)
        pytest.assume(res_dict["status"] == "creating")
        # Get a record.
        await asyncio.sleep(2)
        record_id = res_dict["record_id"]
        get_res = await a_get_record(collection_id=self.collection_id, record_id=record_id)
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.record_keys)
        pytest.assume(get_res_dict["content"].keys() == self.record_content_keys)
        pytest.assume(get_res_dict["content"]["text"] == text)
        pytest.assume(get_res_dict["status"] == "ready")
        # List records.
        new_res = await a_list_records(collection_id=self.collection_id)
        new_nums = len(new_res)
        assert new_nums == old_nums + 1

    @allure.story("test_a_list_records")
    @pytest.mark.run(order=14)
    @pytest.mark.asyncio
    async def test_a_list_records(self, a_record_id):
        # List records.
        if not Base.record_id:
            Base.record_id = await a_record_id
        res = await a_list_records(collection_id=self.collection_id, order="desc", limit=20, offset=None, after=None, before=None)
        assert len(res) >= 0

    @allure.story("test_a_get_record")
    @pytest.mark.run(order=15)
    @pytest.mark.asyncio
    async def test_a_get_record(self):
        # Get a record.
        res = await a_get_record(collection_id=self.collection_id, record_id=self.record_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.record_keys)
        pytest.assume(res_dict["content"].keys() == self.record_content_keys)
        pytest.assume(res_dict["status"] == "ready")

    @allure.story("test_a_update_record")
    @pytest.mark.run(order=16)
    @pytest.mark.asyncio
    async def test_a_update_record(self):
        # Update a record.
        metadata = {"test": "test"}
        res = await a_update_record(collection_id=self.collection_id, record_id=self.record_id, metadata=metadata)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.record_keys)
        pytest.assume(res_dict["content"].keys() == self.record_content_keys)
        pytest.assume(res_dict["metadata"] == metadata)
        # Get a record.
        get_res = await a_get_record(collection_id=self.collection_id, record_id=self.record_id)
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.record_keys)
        pytest.assume(get_res_dict["content"].keys() == self.record_content_keys)
        pytest.assume(get_res_dict["metadata"] == metadata)
        pytest.assume(get_res_dict["status"] == "ready")

    @allure.story("test_a_delete_record")
    @pytest.mark.run(order=33)
    @pytest.mark.asyncio
    async def test_a_delete_record(self):
        # List records.
        records = await a_list_records(collection_id=self.collection_id, order="desc", limit=20, offset=None, after=None,
                               before=None)
        old_nums = len(records)
        for index, record in enumerate(records):
            record_id = record.record_id
            # Delete a record.
            await a_delete_record(collection_id=self.collection_id, record_id=record_id)
            # List records.
            new_records = await a_list_records(collection_id=self.collection_id, order="desc", limit=20, offset=None, after=None,
                                       before=None)
            record_ids = [record.record_id for record in new_records]
            pytest.assume(record_id not in record_ids)
            new_nums = len(new_records)
            assert new_nums == old_nums - 1 - index


@allure.epic("test_retrieval")
@allure.feature("test_chunk")
@pytest.mark.a_sync
class TestChunk(Base):

    chunk_list = ['chunk_id', 'collection_id', 'record_id',  'object', 'text', 'score']
    chunk_keys = set(chunk_list)

    @allure.story("test_a_query_chunks")
    @pytest.mark.run(order=17)
    @pytest.mark.asyncio
    async def test_a_query_chunks(self):
        # List chunks.
        query_text = "Machine learning"
        top_k = 5
        text = "Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
        for i in range(top_k):
            await a_create_text_record(collection_id=self.collection_id, text=text)
        res = await a_query_chunks(collection_id=self.collection_id, query_text=query_text, top_k=top_k)
        pytest.assume(len(res) == top_k)
        for chunk in res:
            chunk_dict = chunk.to_dict()
            pytest.assume(chunk_dict.keys() == self.chunk_keys)
            pytest.assume(query_text in chunk_dict["text"])
            pytest.assume(chunk_dict["score"] >= 0)


