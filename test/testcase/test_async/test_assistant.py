import pytest
import allure

from taskingai.assistant import *
from test.config import chat_model_id
from test.common.read_data import data
from test.common.logger import logger, logger_info, logger_success_info, logger_error_info, logger_info_base
from test.common.utils import list_to_dict
from test.common.utils import assume, assume_success, assume_error, assume_collection, assume_count, assume_assistant
from test.testcase.test_async.base import Base


assistant_data = data.load_yaml("test_assistant_data.yml")


@allure.epic("test_assistant")
@allure.feature("test_assistant")
@pytest.mark.a_sync
class TestAssistant(Base):

    assistant_list = ['assistant_id', 'created_timestamp', 'description', 'metadata', 'model_id', 'name', 'object', 'retrievals', 'system_prompt_template', 'tools']
    assistant_keys = set(assistant_list)

    @allure.story("test_a_create_assistant")
    @pytest.mark.parametrize("a_create_assistant_data", assistant_data["test_success_create_assistant"])
    @pytest.mark.run(order=18)
    @pytest.mark.asyncio
    async def test_a_create_assistant(self, a_create_assistant_data):
        # List assistants.
        old_res = await a_list_assistants()
        old_nums = len(old_res)
        # Create an assistant.
        assistant_dict = list_to_dict(a_create_assistant_data)
        assistant_dict.update({"model_id": chat_model_id})
        if "retrievals" in assistant_dict.keys() and len(assistant_dict["retrievals"]) > 0 and assistant_dict["retrievals"][0]["type"] == "collection":
            assistant_dict["retrievals"][0]["id"] = self.collection_id
        if "tools" in assistant_dict.keys() and len(assistant_dict["tools"]) > 0 and assistant_dict["tools"][0]["type"] == "function":
            assistant_dict["tools"][0]["id"] = self.function_id
        if "tools" in assistant_dict.keys() and len(assistant_dict["tools"]) > 0 and assistant_dict["tools"][0]["type"] == "action":
            assistant_dict["tools"][0]["id"] = self.action_id
        res = await a_create_assistant(**assistant_dict)
        res_dict = res.to_dict()
        logger.info(f'response_dict:{res_dict}, except_dict:{assistant_dict}')
        pytest.assume(res_dict.keys() == self.assistant_keys)
        assume_assistant(res_dict, assistant_dict)
        # Get an assistant.
        get_res = await a_get_assistant(assistant_id=res_dict["assistant_id"])
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.assistant_keys)
        # List assistants.
        new_res = await a_list_assistants()
        new_nums = len(new_res)
        logger.info(f'old_nums:{old_nums}, new_nums:{new_nums}')
        pytest.assume(new_nums == old_nums + 1)

    # @allure.story("test_correct_model_id_a_create_assistant")
    # @pytest.mark.parametrize("a_create_assistant_data", assistant_data["test_correct_model_id_a_create_assistant"])
    # @pytest.mark.run(order=1)
    # def test_correct_model_id_a_create_assistant(self, a_create_assistant_data):
    #     # Create an assistant
    #     assistant_dict = list_to_dict(a_create_assistant_data)
    #     assistant_dict.update({"model_id": chat_model_id})
    #     try:
    #         res = a_create_assistant(**assistant_dict)
    #     except Exception as e:
    #         logger.error(e)

    @allure.story("test_a_list_assistants")
    @pytest.mark.run(order=19)
    @pytest.mark.asyncio
    async def test_a_list_assistants(self):
        # List assistants.
        res = await a_list_assistants()
        assert len(res) >= 0

    @allure.story("test_a_get_assistant")
    @pytest.mark.run(order=20)
    @pytest.mark.asyncio
    async def test_a_get_assistant(self, a_assistant_id):
        # Get an assistant.
        if not Base.assistant_id:
            Base.assistant_id = await a_assistant_id
        res = await a_get_assistant(assistant_id=self.assistant_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.assistant_keys)

    @allure.story("test_a_update_assistant")
    @pytest.mark.run(order=21)
    @pytest.mark.asyncio
    async def test_a_update_assistant(self):
        # Update an assistant.
        name = "openai"
        description = "test for openai"
        res = await a_update_assistant(assistant_id=self.assistant_id, name=name, description=description)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.assistant_keys)
        pytest.assume(res_dict["name"] == name)
        pytest.assume(res_dict["description"] == description)
        # Get an assistant.
        get_res = await a_get_assistant(assistant_id=self.assistant_id)
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.assistant_keys)
        pytest.assume(get_res_dict["name"] == name)
        pytest.assume(get_res_dict["description"] == description)

    @allure.story("test_a_delete_assistant")
    @pytest.mark.run(order=32)
    @pytest.mark.asyncio
    async def test_a_delete_assistant(self):

        # List assistants.
        assistants = await a_list_assistants()
        old_nums = len(assistants)
        for i, v in enumerate(assistants):
            assistant_id = v.assistant_id
            # Delete an assistant.
            await a_delete_assistant(assistant_id=str(assistant_id))
            # List assistants.
            new_assistants = await a_list_assistants()
            assistant_ids = [j.assistant_id for j in new_assistants]
            pytest.assume(assistant_id not in assistant_ids)
            new_nums = len(new_assistants)
            assert new_nums == old_nums - 1 - i


@allure.epic("test_assistant")
@allure.feature("test_chat")
@pytest.mark.a_sync
class TestChat(Base):

        chat_list = ['assistant_id', 'chat_id', 'created_timestamp', 'metadata', 'object']
        chat_keys = set(chat_list)

        @allure.story("test_a_create_chat")
        @pytest.mark.run(order=22)
        @pytest.mark.asyncio
        async def test_a_create_chat(self):
            # List chats.
            old_res = await a_list_chats(assistant_id=self.assistant_id)
            old_nums = len(old_res)
            # Create a chat.
            res = await a_create_chat(assistant_id=self.assistant_id)
            res_dict = res.to_dict()
            pytest.assume(res_dict.keys() == self.chat_keys)
            # Get a chat.
            get_res = await a_get_chat(assistant_id=self.assistant_id, chat_id=res_dict["chat_id"])
            get_res_dict = get_res.to_dict()
            pytest.assume(get_res_dict.keys() == self.chat_keys)
            # List chats.
            new_res = await a_list_chats(assistant_id=self.assistant_id)
            new_nums = len(new_res)
            assert new_nums == old_nums + 1

        @allure.story("test_a_list_chats")
        @pytest.mark.run(order=23)
        @pytest.mark.asyncio
        async def test_a_list_chats(self):
            # List chats.
            res = await a_list_chats(assistant_id=self.assistant_id)
            assert len(res) >= 0

        @allure.story("test_a_get_chat")
        @pytest.mark.run(order=24)
        @pytest.mark.asyncio
        async def test_a_get_chat(self, a_chat_id):
            # Get a chat.
            if not Base.chat_id:
                Base.assistant_id, Base.chat_id = await a_chat_id
            res = await a_get_chat(assistant_id=self.assistant_id, chat_id=self.chat_id)
            res_dict = res.to_dict()
            pytest.assume(res_dict.keys() == self.chat_keys)

        @allure.story("test_a_update_chat")
        @pytest.mark.run(order=25)
        @pytest.mark.asyncio
        async def test_a_update_chat(self):
            # Update a chat.
            metadata = {"test": "test"}
            res = await a_update_chat(assistant_id=self.assistant_id, chat_id=self.chat_id, metadata=metadata)
            res_dict = res.to_dict()
            pytest.assume(res_dict.keys() == self.chat_keys)
            pytest.assume(res_dict["metadata"] == metadata)
            # Get a chat.
            get_res = await a_get_chat(assistant_id=self.assistant_id, chat_id=self.chat_id)
            get_res_dict = get_res.to_dict()
            pytest.assume(get_res_dict.keys() == self.chat_keys)
            pytest.assume(get_res_dict["metadata"] == metadata)

        @allure.story("test_a_delete_chat")
        @pytest.mark.run(order=31)
        @pytest.mark.asyncio
        async def test_a_delete_chat(self):
            # List chats.
            chats = await a_list_chats(assistant_id=self.assistant_id)
            old_nums = len(chats)
            for index, chat in enumerate(chats):
                chat_id = chat.chat_id
                # Delete a chat.
                await a_delete_chat(assistant_id=self.assistant_id, chat_id=str(chat_id))
                # List chats.
                new_chats = await a_list_chats(assistant_id=self.assistant_id)
                chat_ids = [i.chat_id for i in new_chats]
                pytest.assume(chat_id not in chat_ids)
                new_nums = len(new_chats)
                assert new_nums == old_nums - 1 - index


@allure.epic("test_assistant")
@allure.feature("test_message")
@pytest.mark.a_sync
class TestMessage(Base):

    message_list = ['object', 'assistant_id', 'chat_id', 'message_id', 'role', 'content', 'metadata', 'created_timestamp']
    message_keys = set(message_list)

    @allure.story("test_a_create_user_message")
    @pytest.mark.run(order=26)
    @pytest.mark.asyncio
    async def test_a_create_user_message(self):
        # List messages.
        old_res = await a_list_messages(assistant_id=self.assistant_id, chat_id=self.chat_id)
        old_nums = len(old_res)
        # Create a user message.
        text = "hello"
        res = await a_create_user_message(assistant_id=self.assistant_id, chat_id=self.chat_id, text=text)
        res_dict = res.to_dict()
        logger.info(res_dict)
        pytest.assume(res_dict.keys() == self.message_keys)
        pytest.assume(res_dict["content"]["text"] == text)
        pytest.assume(res_dict["role"] == "user")
        # Get a message.
        get_res = await a_get_message(assistant_id=self.assistant_id, chat_id=self.chat_id, message_id=res_dict["message_id"])
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.message_keys)
        # List messages.
        new_res = await a_list_messages(assistant_id=self.assistant_id, chat_id=self.chat_id)
        new_nums = len(new_res)
        assert new_nums == old_nums + 1

    @allure.story("test_a_list_messages")
    @pytest.mark.run(order=27)
    @pytest.mark.asyncio
    async def test_a_list_messages(self):
        # List messages.
        res = await a_list_messages(assistant_id=self.assistant_id, chat_id=self.chat_id)
        assert len(res) >= 0

    @allure.story("test_a_get_message")
    @pytest.mark.run(order=28)
    @pytest.mark.asyncio
    async def test_a_get_message(self, a_message_id):
        # Get a message.
        if not Base.message_id:
            Base.message_id = await a_message_id
        res = await a_get_message(assistant_id=self.assistant_id, chat_id=self.chat_id, message_id=self.message_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.message_keys)

    @allure.story("test_a_update_message")
    @pytest.mark.run(order=29)
    @pytest.mark.asyncio
    async def test_a_update_message(self):
        # Update a message.
        metadata = {"test": "test"}
        res = await a_update_message(assistant_id=self.assistant_id, chat_id=self.chat_id, message_id=self.message_id, metadata=metadata)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.message_keys)
        pytest.assume(res_dict["metadata"] == metadata)
        # Get a message.
        get_res = await a_get_message(assistant_id=self.assistant_id, chat_id=self.chat_id, message_id=self.message_id)
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.message_keys)
        pytest.assume(get_res_dict["metadata"] == metadata)

    @allure.story("test_a_generate_assistant_message")
    @pytest.mark.run(order=30)
    @pytest.mark.asyncio
    async def test_a_generate_assistant_message(self):
        # List messages.
        messages = await a_list_messages(assistant_id=self.assistant_id, chat_id=self.chat_id)
        old_nums = len(messages)
        # Generate an assistant message.
        res = await a_generate_assistant_message(assistant_id=self.assistant_id, chat_id=self.chat_id, system_prompt_variables={})
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.message_keys)
        pytest.assume(res_dict["role"] == "assistant")
        # Get a message.
        get_res = await a_get_message(assistant_id=self.assistant_id, chat_id=self.chat_id, message_id=res_dict["message_id"])
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.message_keys)
        # List messages.
        new_res = await a_list_messages(assistant_id=self.assistant_id, chat_id=self.chat_id)
        new_nums = len(new_res)
        assert new_nums == old_nums + 1

    @allure.story("test_generate_assistant_message_by_stream")
    @pytest.mark.run(order=30)
    async def test_generate_assistant_message_by_stream(self):
        # List assistants.
        # assistants = await a_list_assistants()
        # assistant_id = assistants[-1].assistant_id

        logger.info(f'assistant_id:{self.assistant_id}')
        # create chat
        chat_res = await a_create_chat(assistant_id=self.assistant_id)
        chat_id = chat_res.chat_id
        logger.info(f'chat_id:{chat_id}')
        # create user message
        user_message = await a_create_user_message(
            assistant_id=self.assistant_id,
            chat_id=chat_id,
            text="count from 1 to 100 and separate numbers by comma.",
        )
        # Generate an assistant message by stream.
        stream_res = await a_generate_assistant_message(assistant_id=self.assistant_id, chat_id=chat_id, system_prompt_variables={},
                                                stream=True, debug=True)
        except_list = [i + 1 for i in range(100)]
        real_list = []
        real_str = ''
        async for item in stream_res:
            if isinstance(item, MessageChunk):
                logger.info(f"MessageChunk: {item.delta}")
                if item.delta.isdigit():
                    real_list.append(int(item.delta))
                real_str += item.delta

            elif isinstance(item, Message):
                logger.info(f"Message: {item.message_id}")
                pytest.assume(item.content is not None)
        logger.info(f"Message: {real_str}")
        logger.info(f"except_list: {except_list} real_list: {real_list}")
        pytest.assume(except_list == real_list)



