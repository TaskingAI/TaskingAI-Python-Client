import pytest
import asyncio

from taskingai.retrieval import list_collections, list_records, a_list_collections, a_list_records
from taskingai.assistant import list_assistants, list_chats, list_messages, a_list_assistants, a_list_chats, a_list_messages
from taskingai.tool import list_functions, list_actions, a_list_functions, a_list_actions


#
# def pytest_pytest.assume(repr_compare(config, op, left, right):
#     left_name, right_name = inspect.stack()[7].code_context[0].lstrip().lstrip("pytest.assume").rstrip("").split(op)
#     # pytest_output = pytest.assume(repr_compare(config, op, left, right)
#     logger.info("except_res：{}， real_res： {} ".format(left_name, left))
#     print("except_res：{}， real_res： {} ".format(left_name, left))

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


# @pytest.fixture(scope="session")
# def function_id():
#     res = list_functions()
#     function_id = res[0].function_id
#     return function_id
#
#
# @pytest.fixture(scope="session")
# def function():
#     res = list_functions()
#     function = res[0]
#     return function


@pytest.fixture(scope="session")
def action_id():
    res = list_actions()
    action_id = res[-1].action_id
    return action_id






# @pytest.fixture()
# async def bulk_create_project():
#     projects = get_project_id(10000)
#     create_collection_dict = {"embedding_model_id": "Hfg845kh", "embedding_size": 100}
#     for i in projects:
#         res = await create_collection(i, create_collection_dict)
#     return projects
