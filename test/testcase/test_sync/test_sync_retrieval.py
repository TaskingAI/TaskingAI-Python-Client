import pytest

from taskingai.retrieval import Record, TokenTextSplitter
from taskingai.retrieval import list_collections, create_collection, get_collection, update_collection, delete_collection, list_records, create_record, get_record, update_record, delete_record, query_chunks, create_chunk, update_chunk, get_chunk, delete_chunk, list_chunks
from test.config import Config
from test.common.logger import logger
from test.common.utils import assume_collection_result, assume_record_result, assume_chunk_result, assume_query_chunk_result


@pytest.mark.test_sync
class TestCollection:

    collection_list = ["collection_id",
                        "name",
                        "description",
                        "num_records",
                        "num_chunks",
                        "capacity",
                        "embedding_model_id",
                        "metadata",
                        "updated_timestamp",
                        "created_timestamp",
                        "status"]
    collection_keys = set(collection_list)

    @pytest.mark.run(order=21)
    def test_create_collection(self):

        # Create a collection.
        create_dict = {
            "capacity": 1000,
            "embedding_model_id": Config.text_embedding_model_id,
            "name": "test",
            "description": "description",
            "metadata": {
                "key1": "value1",
                "key2": "value2"
            }
        }
        for x in range(2):
            res = create_collection(**create_dict)
            res_dict = vars(res)
            logger.info(res_dict)
            pytest.assume(res_dict.keys() == self.collection_keys)
            assume_collection_result(create_dict, res_dict)

    @pytest.mark.run(order=22)
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

    @pytest.mark.run(order=23)
    def test_get_collection(self, collection_id):

        # Get a collection.

        res = get_collection(collection_id=collection_id)
        res_dict = vars(res)
        pytest.assume(res_dict.keys() == self.collection_keys)
        pytest.assume(res_dict["status"] == "ready")
        pytest.assume(res_dict["collection_id"] == collection_id)

    @pytest.mark.run(order=24)
    def test_update_collection(self, collection_id):

        # Update a collection.

        update_collection_data = {
            "collection_id": collection_id,
            "name": "test_update",
            "description": "description_update",
            "metadata": {
                "key1": "value1",
                "key2": "value2"
            }
        }
        res = update_collection(**update_collection_data)
        res_dict = vars(res)
        pytest.assume(res_dict.keys() == self.collection_keys)
        assume_collection_result(update_collection_data, res_dict)

    @pytest.mark.run(order=80)
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

    record_list = ["record_id",
                    "collection_id",
                    "num_chunks",
                    "content",
                    "metadata",
                    "type",
                    "title",
                    "updated_timestamp",
                    "created_timestamp",
                    "status"]
    record_keys = set(record_list)
    
    @pytest.mark.run(order=31)
    def test_create_record(self, collection_id):

        # Create a text record.
        text_splitter = TokenTextSplitter(chunk_size=200, chunk_overlap=20)
        text = "Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
        create_record_data = {
            "collection_id": collection_id,
            "content": text,
            "text_splitter": text_splitter,
            "metadata": {
                "key1": "value1",
                "key2": "value2"
            }
        }
        for x in range(2):
            res = create_record(**create_record_data)
            res_dict = vars(res)
            pytest.assume(res_dict.keys() == self.record_keys)
            assume_record_result(create_record_data, res_dict)

    @pytest.mark.run(order=32)
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

    @pytest.mark.run(order=33)
    def test_get_record(self, collection_id):

        # list records

        records = list_records(collection_id=collection_id)
        for record in records:
            record_id = record.record_id
            res = get_record(collection_id=collection_id, record_id=record_id)
            logger.info(f'get record response: {res}')
            res_dict = vars(res)
            pytest.assume(res_dict["collection_id"] == collection_id)
            pytest.assume(res_dict["record_id"] == record_id)
            pytest.assume(res_dict.keys() == self.record_keys)
            pytest.assume(res_dict["status"] == "ready")

    @pytest.mark.run(order=34)
    def test_update_record(self, collection_id, record_id):

        # Update a record.

        update_record_data = {
            "collection_id": collection_id,
            "record_id": record_id,
            "content": "TaskingAI is an AI-native application development platform that unifies modules like Model, Retrieval, Assistant, and Tool into one seamless ecosystem, streamlining the creation and deployment of applications for developers.",
            "text_splitter": TokenTextSplitter(chunk_size=200, chunk_overlap=20),
            "metadata": {"test": "test"}
        }
        res = update_record(**update_record_data)
        res_dict = vars(res)
        pytest.assume(res_dict.keys() == self.record_keys)
        assume_record_result(update_record_data, res_dict)

    @pytest.mark.run(order=79)
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

    chunk_list = ["chunk_id", "record_id", "collection_id", "content", "metadata", "num_tokens", "score", "updated_timestamp","created_timestamp"]
    chunk_keys = set(chunk_list)

    @pytest.mark.run(order=41)
    def test_query_chunks(self, collection_id):

        # Query chunks.

        query_text = "Machine learning"
        top_k = 1
        res = query_chunks(collection_id=collection_id, query_text=query_text, top_k=top_k)
        pytest.assume(len(res) == top_k)
        for chunk in res:
            chunk_dict = vars(chunk)
            assume_query_chunk_result(query_text, chunk_dict)
            pytest.assume(chunk_dict.keys() == self.chunk_keys)

    @pytest.mark.run(order=42)
    def test_create_chunk(self, collection_id):

        # Create a chunk.
        create_chunk_data = {
            "collection_id": collection_id,
            "content": "Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."}
        res = create_chunk(**create_chunk_data)
        res_dict = vars(res)
        pytest.assume(res_dict.keys() == self.chunk_keys)
        assume_chunk_result(create_chunk_data, res_dict)

    @pytest.mark.run(order=43)
    def test_list_chunks(self, collection_id):

        # List chunks.

        nums_limit = 1
        res = list_chunks(limit=nums_limit, collection_id=collection_id)
        pytest.assume(len(res) == nums_limit)

        after_id = res[-1].chunk_id
        after_res = list_chunks(limit=nums_limit, after=after_id, collection_id=collection_id)
        pytest.assume(len(after_res) == nums_limit)

        twice_nums_list = list_chunks(limit=nums_limit * 2, collection_id=collection_id)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])

        before_id = after_res[0].chunk_id
        before_res = list_chunks(limit=nums_limit, before=before_id, collection_id=collection_id)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=44)
    def test_get_chunk(self, collection_id):

        # list chunks

        chunks = list_chunks(collection_id=collection_id)
        for chunk in chunks:
            chunk_id = chunk.chunk_id
            res = get_chunk(collection_id=collection_id, chunk_id=chunk_id)
            logger.info(f'get chunk response: {res}')
            res_dict = vars(res)
            pytest.assume(res_dict["collection_id"] == collection_id)
            pytest.assume(res_dict["chunk_id"] == chunk_id)
            pytest.assume(res_dict.keys() == self.chunk_keys)

    @pytest.mark.run(order=45)
    def test_update_chunk(self, collection_id, chunk_id):

        # Update a chunk.

        update_chunk_data = {
            "collection_id": collection_id,
            "chunk_id": chunk_id,
            "content": "Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data.",
            "metadata": {"test": "test"}
        }
        res = update_chunk(**update_chunk_data)
        res_dict = vars(res)
        pytest.assume(res_dict.keys() == self.chunk_keys)
        assume_chunk_result(update_chunk_data, res_dict)

    @pytest.mark.run(order=46)
    def test_delete_chunk(self, collection_id):

        # List chunks.

        chunks = list_chunks(collection_id=collection_id)
        old_nums = len(chunks)
        for index, chunk in enumerate(chunks):
            chunk_id = chunk.chunk_id

            # Delete a chunk.

            delete_chunk(collection_id=collection_id, chunk_id=chunk_id)

            # List chunks.

            new_chunks = list_chunks(collection_id=collection_id)
            chunk_ids = [chunk.chunk_id for chunk in new_chunks]
            pytest.assume(chunk_id not in chunk_ids)
            new_nums = len(new_chunks)
            pytest.assume(new_nums == old_nums - 1 - index)
