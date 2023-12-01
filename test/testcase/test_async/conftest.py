from taskingai.assistant import a_list_assistants, a_list_chats, a_list_messages
from taskingai.retrieval import a_list_collections, a_list_records
from taskingai.tool import a_list_functions, a_list_actions

import pytest
import asyncio


@pytest.fixture(scope="function")
async def a_assistant_id():
    res = await a_list_assistants()
    assistant_id = res[0].assistant_id
    return assistant_id


@pytest.fixture(scope="function")
async def a_chat_id(a_assistant_id):
    assistant_id = await a_assistant_id
    res = await a_list_chats(str(assistant_id))
    chat_id = res[0].chat_id
    return assistant_id, chat_id


@pytest.fixture(scope="function")
async def a_message_id(a_chat_id):
    assistant_id, chat_id = await a_chat_id
    res = await a_list_messages(str(assistant_id), str(chat_id))
    message_id = res[0].message_id
    return message_id


@pytest.fixture(scope="function")
async def a_collection_id():
    res = await a_list_collections()
    collection_id = res[0].collection_id
    return collection_id


@pytest.fixture(scope="function")
async def a_record_id(a_collection_id):
    collection_id = await a_collection_id
    res = await a_list_records(str(collection_id))
    record_id = res[0].record_id
    return record_id


@pytest.fixture(scope="function")
async def a_function_id():
    res = await a_list_functions()
    function_id = res[0].function_id
    return function_id


@pytest.fixture(scope="function")
async def a_function():
    res = await a_list_functions()
    function = res[0]
    return function


@pytest.fixture(scope="function")
async def a_action_id():
    res = await a_list_actions()
    action_id = res[0].action_id
    return action_id


@pytest.yield_fixture(scope="session")
def event_loop(request):
    """Create an instance of the default event loop for each test case."""
    loop = asyncio.get_event_loop_policy().new_event_loop()
    yield loop
    loop.close()


