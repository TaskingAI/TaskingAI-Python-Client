import pytest
import allure

from taskingai.assistant import *
from test.config import chat_model_id
from test.common.read_data import data
from test.common.logger import logger
from test.common.utils import list_to_dict
from test.common.utils import assume_assistant
from test.testcase.test_async.base import Base

assistant_data = data.load_yaml("test_assistant_data.yml")


@allure.epic("test_bulk_assistant")
@allure.feature("test_assistant")
@pytest.mark.bulk
class TestAssistant:

    assistant_list = ['assistant_id', 'created_timestamp', 'description', 'metadata', 'model_id', 'name', 'object', 'retrievals', 'system_prompt_template', 'tools']
    assistant_keys = set(assistant_list)
    nums = 10

    @allure.story("test_bulk_create_assistant")
    @pytest.mark.run(order=0)
    @pytest.mark.parametrize("num", (x+1 for x in range(nums)))
    @pytest.mark.asyncio
    async def test_bulk_create_assistant(self, num):
        # Create an assistant.
        assistant_dict = {"model_id": chat_model_id,
                          "name": f'{num}',
                          "description": "hello app",
                          "system_prompt_template": "You are a very professional customer service expert speaking {{12312}} language.",
                          "metadata": {}}
        res = await a_create_assistant(**assistant_dict)
        res_dict = res.to_dict()
        logger.info(f'response_dict:{res_dict}, except_dict:{assistant_dict}')
        pytest.assume(res_dict.keys() == self.assistant_keys)
        assume_assistant(res_dict, assistant_dict)
        # Get an assistant.
        get_res = await a_get_assistant(assistant_id=res_dict["assistant_id"])
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.assistant_keys)

    @allure.story("test_bulk_list_assistants")
    @pytest.mark.run(order=1)
    @pytest.mark.asyncio
    async def test_bulk_list_assistants(self):
        # List assistants.
        limit_num = 5
        res = await a_list_assistants(limit=limit_num)

        before_id = res[0].assistant_id
        after_id = res[-1].assistant_id
        before_res = await a_list_assistants(limit=limit_num, before=before_id)
        logger.info('list_assistants_before')
        logger.info(before_res)
        logger.info(len(before_res))
        pytest.assume(len(before_res) == 0)
        # pytest.assume(before_res[0].assistant_id == res[0].assistant_id)
        after_res = await a_list_assistants(limit=limit_num, after=after_id)
        logger.info('list_assistants_after')
        logger.info(after_res)
        pytest.assume(0 <= len(after_res) <= limit_num)
        # limit_twice_res = await a_list_assistants(limit=limit_num*2)
        # logger.info('list_assistants_twice')
        # logger.info(limit_twice_res)
        # pytest.assume(after_res[-1].assistant_id == limit_twice_res[-1].assistant_id)

    @allure.story("test_bulk_delete_assistant")
    @pytest.mark.run(order=10)
    @pytest.mark.asyncio
    async def test_bulk_delete_assistant(self):

        # List assistants.
        while True:
            assistants = await a_list_assistants()
            old_nums = len(assistants)
            if old_nums == 0:
                break
            for i, v in enumerate(assistants):
                assistant_id = v.assistant_id
                # Delete an assistant.
                await a_delete_assistant(assistant_id=str(assistant_id))


@allure.epic("test_bulk_assistant")
@allure.feature("test_chat")
@pytest.mark.bulk
class TestChat:

        chat_list = ['assistant_id', 'chat_id', 'created_timestamp', 'metadata', 'object']
        chat_keys = set(chat_list)
        nums = 100

        @allure.story("test_bulk_create_chat")
        @pytest.mark.run(order=2)
        @pytest.mark.parametrize("num", (x+1 for x in range(nums)))
        @pytest.mark.asyncio
        async def test_bulk_create_chat(self, a_assistant_id, num):
            assistant_id = await a_assistant_id

            res = await a_create_chat(assistant_id=assistant_id)
            res_dict = res.to_dict()
            pytest.assume(res_dict.keys() == self.chat_keys)
            # Get a chat.
            get_res = await a_get_chat(assistant_id=assistant_id, chat_id=res_dict["chat_id"])
            get_res_dict = get_res.to_dict()
            pytest.assume(get_res_dict.keys() == self.chat_keys)

            
        @allure.story("test_bulk_list_chats")
        @pytest.mark.run(order=3)
        @pytest.mark.asyncio
        async def test_bulk_list_chats(self, a_assistant_id):
            assistant_id = await a_assistant_id
            # List chats.
            limit_num = 20
            res = await a_list_chats(limit=limit_num, assistant_id=assistant_id)
            before_id = res[0].chat_id
            after_id = res[-1].chat_id
            before_res = await a_list_chats(limit=limit_num, before=before_id, assistant_id=assistant_id)
            pytest.assume(len(before_res) == 0)
            # pytest.assume(before_res[0].chat_id == res[0].chat_id)
            after_res = await a_list_chats(limit=limit_num, after=after_id, assistant_id=assistant_id)
            pytest.assume(0 <= len(after_res) <= limit_num)
            # limit_twice_res = await a_list_chats(limit=limit_num * 2, assistant_id=assistant_id)
            # pytest.assume(after_res[-1].chat_id == limit_twice_res[-1].chat_id)

        @allure.story("test_bulk_delete_chat")
        @pytest.mark.run(order=9)
        @pytest.mark.asyncio
        async def test_bulk_delete_chat(self, a_assistant_id):
            assistant_id = await a_assistant_id
            while True:
            # List chats.
                chats = await a_list_chats(assistant_id=assistant_id)
                old_nums = len(chats)
                if old_nums == 0:
                    break
                for index, chat in enumerate(chats):
                    chat_id = chat.chat_id
                    # Delete a chat.
                    try:
                        await a_delete_chat(assistant_id=assistant_id, chat_id=str(chat_id))
                    except Exception as e:
                        logger.info(f'error_message{e}')
                    # List chats.
                    new_chats = await a_list_chats(assistant_id=assistant_id)
                    chat_ids = [i.chat_id for i in new_chats]
                    pytest.assume(chat_id not in chat_ids)


@allure.epic("test_bulk_assistant")
@allure.feature("test_message")
@pytest.mark.bulk
class TestMessage:

    message_list = ['object', 'assistant_id', 'chat_id', 'message_id', 'role', 'content', 'metadata', 'created_timestamp']
    message_keys = set(message_list)
    nums = 10
    
    @allure.story("test_bulk_create_user_message")
    @pytest.mark.parametrize("num", (x+1 for x in range(nums)))
    @pytest.mark.run(order=4)
    @pytest.mark.asyncio
    async def test_bulk_create_user_message(self, a_chat_id, num):
        assistant_id, chat_id = await a_chat_id
        # Create a user message.
        chat_res = await a_list_chats(assistant_id=assistant_id)
        chat_id = chat_res[0].chat_id
        text = "hello"
        res = await a_create_user_message(assistant_id=assistant_id, chat_id=chat_id, text=text)
        res_dict = res.to_dict()
        logger.info(res_dict)
        pytest.assume(res_dict.keys() == self.message_keys)
        pytest.assume(res_dict["content"]["text"] == text)
        pytest.assume(res_dict["role"] == "user")
        # Get a message.
        get_res = await a_get_message(assistant_id=assistant_id, chat_id=chat_id,
                                      message_id=res_dict["message_id"])
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.message_keys)


    @allure.story("test_bulk_list_messages")
    @pytest.mark.run(order=5)
    @pytest.mark.asyncio
    async def test_bulk_list_messages(self, a_chat_id):
        assistant_id, chat_id = await a_chat_id

        # List messages.
        limit_num = 5
        res = await a_list_messages(limit=limit_num, assistant_id=assistant_id, chat_id=chat_id)

        before_id = res[0].message_id
        after_id = res[-1].message_id
        before_res = await a_list_messages(limit=limit_num, before=before_id, assistant_id=assistant_id, chat_id=chat_id)
        logger.info('list_messages_before')
        logger.info(before_res)
        pytest.assume(len(before_res) == 0)
        pytest.assume(before_res[0].message_id == res[0].message_id)
        after_res = await a_list_messages(limit=limit_num, after=after_id, assistant_id=assistant_id, chat_id=chat_id)
        logger.info('list_messages_after')
        logger.info(after_res)
        pytest.assume(0 <= len(after_res) <= limit_num)
        # limit_twice_res = await a_list_messages(limit=limit_num * 2, assistant_id=assistant_id, chat_id=chat_id)
        # logger.info(limit_twice_res)
        # logger.info('list_messages_twice')
        # pytest.assume(after_res[-1].message_id == limit_twice_res[-1].message_id)

    @allure.story("test_bulk_generate_assistant_message")
    @pytest.mark.parametrize("num", (x+1 for x in range(2)))
    @pytest.mark.run(order=6)
    @pytest.mark.asyncio
    async def test_bulk_generate_assistant_message(self, a_chat_id, num):
        assistant_id, chat_id = await a_chat_id

        # Generate an assistant message.
        try:
            res = await a_generate_assistant_message(assistant_id=assistant_id, chat_id=chat_id, system_prompt_variables={})
            res_dict = res.to_dict()
            pytest.assume(res_dict.keys() == self.message_keys)
            pytest.assume(res_dict["role"] == "assistant")
            # Get a message.
            get_res = await a_get_message(assistant_id=assistant_id, chat_id=chat_id,
                                          message_id=res_dict["message_id"])
            logger.info('generate assistant message')
            logger.info(get_res)
            get_res_dict = get_res.to_dict()
            pytest.assume(get_res_dict.keys() == self.message_keys)
        except Exception as e:
            logger.info("Generate an assistant message failed.")
            logger.info(e)











