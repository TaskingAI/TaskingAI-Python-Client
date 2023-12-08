import asyncio
import pytest


@pytest.yield_fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()

from taskingai.assistant import a_list_assistants, a_list_chats, a_list_messages
from taskingai.retrieval import a_list_collections, a_list_records
from taskingai.tool import a_list_functions, a_list_actions

import pytest
import asyncio


@pytest.fixture(scope="function")
async def a_assistant_id():
    res = await a_list_assistants(order='asc')
    assistant_id = res[0].assistant_id
    return assistant_id


@pytest.fixture(scope="function")
async def a_chat_id(a_assistant_id):
    assistant_id = await a_assistant_id
    res = await a_list_chats(assistant_id=str(assistant_id), order='asc')
    chat_id = res[0].chat_id
    return assistant_id, chat_id


@pytest.fixture(scope="function")
async def a_collection_id():
    res = await a_list_collections(order='asc')
    collection_id = res[0].collection_id
    return collection_id


@pytest.fixture(scope="function")
async def a_record_id(a_collection_id):
    collection_id = await a_collection_id
    res = await a_list_records(collection_id=str(collection_id), order='asc')
    record_id = res[0].record_id
    return record_id


@pytest.yield_fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


