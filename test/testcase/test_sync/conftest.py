import pytest

from taskingai.retrieval import list_collections, list_records
from taskingai.assistant import list_assistants, list_chats, list_messages
from taskingai.tool import list_actions


@pytest.fixture(scope="session")
def assistant_id():
    res = list_assistants()
    assistant_id = res[0].assistant_id
    return assistant_id


@pytest.fixture(scope="session")
def chat_id(assistant_id):
    res = list_chats(str(assistant_id))
    chat_id = res[0].chat_id
    return chat_id


@pytest.fixture(scope="session")
def message_id(assistant_id, chat_id):
    res = list_messages(str(assistant_id), str(chat_id))
    message_id = res[0].message_id
    return message_id


@pytest.fixture(scope="session")
def collection_id():
    res = list_collections()
    collection_id = res[0].collection_id
    return collection_id


@pytest.fixture(scope="session")
def record_id(collection_id):
    res = list_records(str(collection_id))
    record_id = res[0].record_id
    return record_id


@pytest.fixture(scope="session")
def action_id():
    res = list_actions()
    action_id = res[-1].action_id
    return action_id



