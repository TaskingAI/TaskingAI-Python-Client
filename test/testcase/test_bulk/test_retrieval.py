import asyncio
import allure
import pytest

from taskingai.retrieval import a_list_collections, a_create_collection, a_get_collection, a_update_collection, \
    a_delete_collection, a_list_records, a_create_text_record, a_get_record, a_update_record, a_delete_record, \
    a_query_chunks
from test.config import text_model_id
from test.common.utils import logger
from test.testcase.test_async.base import Base


@allure.epic("test_bulk_retrieval")
@allure.feature("test_collection")
@pytest.mark.bulk
class TestCollection(Base):
    collection_list = ['object', 'collection_id', 'name', 'description', 'num_records', 'num_chunks', 'capacity',
                       'embedding_model_id', 'metadata', 'configs', 'created_timestamp', "status"]
    collection_keys = set(collection_list)
    collection_configs = ["metric", "chunk_size", "chunk_overlap"]
    collection_configs_keys = set(collection_configs)
    nums = 100

    @allure.story("test_bulk_create_collection")
    @pytest.mark.parametrize("num", (x + 1 for x in range(nums)))
    @pytest.mark.run(order=0)
    @pytest.mark.asyncio
    async def test_bulk_create_collection(self, num):
        # Create a collection.
        name = f"test{num}"
        description = "just for test"
        res = await a_create_collection(name=name, description=description, embedding_model_id=text_model_id,
                                        capacity=1000)
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

    @allure.story("test_bulk_list_collections")
    @pytest.mark.run(order=1)
    @pytest.mark.asyncio
    async def test_bulk_list_collections(self):
        # List collections.
        limit_num = 20
        res = await a_list_collections(limit=limit_num)
        before_id = res[0].collection_id
        after_id = res[-1].collection_id
        before_res = await a_list_collections(limit=limit_num, before=before_id)
        pytest.assume(len(before_res) == 0)
        after_res = await a_list_collections(limit=limit_num, after=after_id)
        pytest.assume(0 <= len(after_res) <= limit_num)


    @allure.story("test_bulk_delete_collection")
    @pytest.mark.run(order=34)
    @pytest.mark.asyncio
    async def test_bulk_delete_collection(self):
        while True:
            # List collections.
            old_res = await a_list_collections()
            old_nums = len(old_res)
            if old_nums == 0:
                break

            for index, collection in enumerate(old_res):
                collection_id = collection.collection_id
                # Delete a collection.
                await a_delete_collection(collection_id=collection_id)
                await asyncio.sleep(1)
                new_collections = await a_list_collections()
                # List collections.
                collection_ids = [c.collection_id for c in new_collections]
                logger.info(f'collection: {collection_id}, collection_ids: {collection_ids}')
                pytest.assume(collection_id not in collection_ids)


@allure.epic("test_bulk_retrieval")
@allure.feature("test_record")
@pytest.mark.bulk
class TestRecord(Base):
    record_list = ['record_id', 'collection_id', 'num_chunks', 'content', 'metadata', 'type', 'object',
                   'created_timestamp', 'status']
    record_keys = set(record_list)
    record_content = ["text"]
    record_content_keys = set(record_content)
    nums = 100

    @allure.story("test_bulk_create_text_record")
    @pytest.mark.parametrize("num", (x + 1 for x in range(nums)))
    @pytest.mark.run(order=2)
    @pytest.mark.asyncio
    async def test_bulk_create_text_record(self, a_collection_id, num):
        collection_id = await a_collection_id
        # Create a text record.
        text = f"{num}Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
        res = await a_create_text_record(collection_id=collection_id, text=text)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.record_keys)
        pytest.assume(res_dict["content"].keys() == self.record_content_keys)
        pytest.assume(res_dict["content"]["text"] == text)
        pytest.assume(res_dict["status"] == "creating")
        # Get a record.
        await asyncio.sleep(3)
        record_id = res_dict["record_id"]
        get_res = await a_get_record(collection_id=collection_id, record_id=record_id)
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.record_keys)
        pytest.assume(get_res_dict["content"].keys() == self.record_content_keys)
        pytest.assume(get_res_dict["content"]["text"] == text)
        logger.info(get_res_dict["status"])
        pytest.assume(get_res_dict["status"] == "ready")


        
    @allure.story("test_bulk_list_records")
    @pytest.mark.run(order=3)
    @pytest.mark.asyncio
    async def test_bulk_list_records(self, a_collection_id):
        collection_id = await a_collection_id
        # List records.

        limit_num = 20
        res = await a_list_records(limit=limit_num, collection_id=collection_id)

        before_id = res[0].record_id
        after_id = res[-1].record_id
        before_res = await a_list_records(limit=limit_num, before=before_id, collection_id=collection_id)
        pytest.assume(len(before_res) == 0)
        pytest.assume(before_res[0].record_id == res[0].record_id)
        after_res = await a_list_records(limit=limit_num, after=after_id, collection_id=collection_id)
        pytest.assume(0 <= len(after_res) <= limit_num)

    @allure.story("test_bulk_delete_record")
    @pytest.mark.run(order=33)
    @pytest.mark.asyncio
    async def test_bulk_delete_record(self, a_collection_id):
        collection_id = await a_collection_id
        while True:
            # List records.
            records = await a_list_records(collection_id=collection_id)
            old_nums = len(records)
            if old_nums == 0:
                break
            for index, record in enumerate(records):
                record_id = record.record_id
                # Delete a record.
                await a_delete_record(collection_id=collection_id, record_id=record_id)
                # List records.
                await asyncio.sleep(1)
                new_records = await a_list_records(collection_id=collection_id)
                record_ids = [record.record_id for record in new_records]
                logger.info(f'record: {record_id}, record_ids: {record_ids}')
                pytest.assume(record_id not in record_ids)


