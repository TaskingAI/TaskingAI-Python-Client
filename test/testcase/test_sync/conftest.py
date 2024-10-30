import pytest
#
# from taskingai.retrieval import list_collections, list_records, list_chunks
from taskingai.assistant import list_assistants, list_chats, list_messages
# from taskingai.tool import list_actions
#
#
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
