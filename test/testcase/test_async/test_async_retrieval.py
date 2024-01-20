import pytest

from taskingai.retrieval import *
from test.config import embedding_model_id
from test.common.logger import logger
from test.testcase.test_async.base import Base


@pytest.mark.test_async
class TestCollection(Base):
    collection_list = [
        "object",
        "collection_id",
        "name",
        "description",
        "num_records",
        "num_chunks",
        "capacity",
        "embedding_model_id",
        "metadata",
        "created_timestamp",
        "status",
    ]
    collection_keys = set(collection_list)
    collection_configs = ["metric", "chunk_size", "chunk_overlap"]
    collection_configs_keys = set(collection_configs)

    @pytest.mark.run(order=9)
    @pytest.mark.asyncio
    async def test_a_create_collection(self):
        for x in range(2):
            # Create a collection.

            name = f"test{x}"
            description = "just for test"
            res = await a_create_collection(
                name=name, description=description, embedding_model_id=embedding_model_id, capacity=1000
            )
            res_dict = res.to_dict()
            logger.info(res_dict)
            pytest.assume(res_dict.keys() == self.collection_keys)
            pytest.assume(res_dict["name"] == name)
            pytest.assume(res_dict["description"] == description)
            pytest.assume(res_dict["embedding_model_id"] == embedding_model_id)
            pytest.assume(res_dict["capacity"] == 1000)
            pytest.assume(res_dict["status"] == "creating")

    @pytest.mark.run(order=10)
    @pytest.mark.asyncio
    async def test_a_list_collections(self):
        # List collections.

        nums_limit = 1
        res = await a_list_collections(limit=nums_limit)
        pytest.assume(len(res) == nums_limit)
        after_id = res[-1].collection_id
        after_res = await a_list_collections(limit=nums_limit, after=after_id)
        pytest.assume(len(after_res) == nums_limit)
        twice_nums_list = await a_list_collections(limit=nums_limit * 2)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])
        before_id = after_res[0].collection_id
        before_res = await a_list_collections(limit=nums_limit, before=before_id)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

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
        pytest.assume(res_dict["status"] == "ready" or "creating")

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

    @pytest.mark.run(order=35)
    @pytest.mark.asyncio
    async def test_a_delete_collection(self):
        # List collections.
        old_res = await a_list_collections(order="desc", limit=100, after=None, before=None)

        for index, collection in enumerate(old_res):
            collection_id = collection.collection_id
            # Delete a collection.
            await a_delete_collection(collection_id=collection_id)

            new_collections = await a_list_collections(order="desc", limit=100, after=None, before=None)
            # List collections.
            collection_ids = [c.collection_id for c in new_collections]
            pytest.assume(collection_id not in collection_ids)


@pytest.mark.test_async
class TestRecord(Base):
    record_list = [
        "record_id",
        "collection_id",
        "num_chunks",
        "content",
        "metadata",
        "type",
        "object",
        "created_timestamp",
        "status",
    ]
    record_keys = set(record_list)
    record_content = ["text"]
    record_content_keys = set(record_content)

    @pytest.mark.run(order=13)
    @pytest.mark.asyncio
    async def test_a_create_record(self):
        for x in range(2):
            # Create a text record.

            text = f"{x}Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
            res = await a_create_record(
                collection_id=self.collection_id,
                content=text,
                text_splitter=TokenTextSplitter(chunk_size=200, chunk_overlap=20),
            )
            res_dict = res.to_dict()
            pytest.assume(res_dict.keys() == self.record_keys)
            pytest.assume(res_dict["content"].keys() == self.record_content_keys)
            pytest.assume(res_dict["content"]["text"] == text)
            pytest.assume(res_dict["status"] == "creating")

    @pytest.mark.run(order=14)
    @pytest.mark.asyncio
    async def test_a_list_records(self, a_record_id):
        # List records.

        if not Base.record_id:
            Base.record_id = await a_record_id
        nums_limit = 1
        res = await a_list_records(limit=nums_limit, collection_id=self.collection_id)
        pytest.assume(len(res) == nums_limit)

        after_id = res[-1].record_id
        after_res = await a_list_records(limit=nums_limit, after=after_id, collection_id=self.collection_id)
        pytest.assume(len(after_res) == nums_limit)

        twice_nums_list = await a_list_records(limit=nums_limit * 2, collection_id=self.collection_id)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])

        before_id = after_res[0].record_id
        before_res = await a_list_records(limit=nums_limit, before=before_id, collection_id=self.collection_id)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=15)
    @pytest.mark.asyncio
    async def test_a_get_record(self):
        # Get a record.

        res = await a_get_record(collection_id=self.collection_id, record_id=self.record_id)
        logger.info(f"a_get_record:{res}")
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.record_keys)
        pytest.assume(res_dict["content"].keys() == self.record_content_keys)
        pytest.assume(res_dict["status"] == "ready" or "creating")

    @pytest.mark.run(order=16)
    @pytest.mark.asyncio
    async def test_a_update_record(self):
        # Update a record.

        metadata = {"test": "test"}
        res = await a_update_record(collection_id=self.collection_id, record_id=self.record_id, metadata=metadata)
        logger.info(f"a_update_record:{res}")
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.record_keys)
        pytest.assume(res_dict["content"].keys() == self.record_content_keys)
        pytest.assume(res_dict["metadata"] == metadata)

    @pytest.mark.run(order=34)
    @pytest.mark.asyncio
    async def test_a_delete_record(self):
        # List records.

        records = await a_list_records(
            collection_id=self.collection_id, order="desc", limit=20, after=None, before=None
        )
        old_nums = len(records)
        for index, record in enumerate(records):
            record_id = record.record_id

            # Delete a record.

            await a_delete_record(collection_id=self.collection_id, record_id=record_id)

            # List records.

            new_records = await a_list_records(
                collection_id=self.collection_id, order="desc", limit=20, after=None, before=None
            )
            record_ids = [record.record_id for record in new_records]
            pytest.assume(record_id not in record_ids)
            new_nums = len(new_records)
            pytest.assume(new_nums == old_nums - 1 - index)


@pytest.mark.test_async
class TestChunk(Base):
    chunk_list = ["chunk_id", "collection_id", "record_id", "object", "text", "score"]
    chunk_keys = set(chunk_list)

    @pytest.mark.run(order=17)
    @pytest.mark.asyncio
    async def test_a_query_chunks(self):
        # Query chunks.

        query_text = "Machine learning"
        top_k = 2
        res = await a_query_chunks(collection_id=self.collection_id, query_text=query_text, top_k=top_k)
        pytest.assume(len(res) == top_k)
        for chunk in res:
            chunk_dict = chunk.to_dict()
            pytest.assume(chunk_dict.keys() == self.chunk_keys)
            pytest.assume(query_text in chunk_dict["text"])
            pytest.assume(chunk_dict["score"] >= 0)
