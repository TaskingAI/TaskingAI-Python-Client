import pytest

from taskingai.assistant import *
from taskingai.client.models import ToolRef, ToolType, RetrievalRef, RetrievalType
from taskingai.assistant.memory import AssistantNaiveMemory
from test.config import Config
from test.common.read_data import data
from test.common.logger import logger
from test.common.utils import list_to_dict
from test.common.utils import assume_assistant_result, assume_chat_result, assume_message_result
from test.testcase.test_async import Base


@pytest.mark.test_async
class TestAssistant(Base):

    assistant_list = ['assistant_id', 'updated_timestamp','created_timestamp', 'description', 'metadata', 'model_id', 'name', 'retrievals', 'retrieval_configs', 'system_prompt_template', 'tools',"memory"]
    assistant_keys = set(assistant_list)

    @pytest.mark.run(order=51)
    @pytest.mark.asyncio
    async def test_a_create_assistant(self):

        # Create an assistant.

        assistant_dict = {
            "model_id": Config.chat_completion_model_id,
            "name": "test",
            "description": "test for assistant",
            "memory": AssistantNaiveMemory(),
            "system_prompt_template": ["You know the meaning of various numbers.",
                                       "No matter what the user's language is, you will use the {{langugae}} to explain."],
            "metadata": {"test": "test"},
            "retrievals": [
                RetrievalRef(
                    type=RetrievalType.COLLECTION,
                    id=self.collection_id,
                ),
            ],
            "tools": [
                ToolRef(
                    type=ToolType.ACTION,
                    id=self.action_id,
                ),
                ToolRef(
                    type=ToolType.PLUGIN,
                    id="open_weather/get_hourly_forecast",
                )
            ]
        }
        for i in range(4):
            res = await a_create_assistant(**assistant_dict)
            res_dict = vars(res)
            logger.info(f'response_dict:{res_dict}, except_dict:{assistant_dict}')
            pytest.assume(res_dict.keys() == self.assistant_keys)
            assume_assistant_result(assistant_dict, res_dict)
            Base.assistant_id = res.assistant_id

    @pytest.mark.run(order=52)
    @pytest.mark.asyncio
    async def test_a_list_assistants(self):

        # List assistants.

        nums_limit = 1
        res = await a_list_assistants(limit=nums_limit)
        pytest.assume(len(res) == nums_limit)

        after_id = res[-1].assistant_id
        after_res = await a_list_assistants(limit=nums_limit, after=after_id)
        pytest.assume(len(after_res) == nums_limit)

        twice_nums_list = await a_list_assistants(limit=nums_limit * 2)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])

        before_id = after_res[0].assistant_id
        before_res = await a_list_assistants(limit=nums_limit, before=before_id)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=53)
    @pytest.mark.asyncio
    async def test_a_get_assistant(self):

        # Get an assistant.

        res = await a_get_assistant(assistant_id=self.assistant_id)
        res_dict = vars(res)
        pytest.assume(res_dict.keys() == self.assistant_keys)

    @pytest.mark.run(order=54)
    @pytest.mark.asyncio
    async def test_a_update_assistant(self):

        # Update an assistant.

        name = "openai"
        description = "test for openai"
        res = await a_update_assistant(assistant_id=self.assistant_id, name=name, description=description)
        res_dict = vars(res)
        pytest.assume(res_dict.keys() == self.assistant_keys)
        pytest.assume(res_dict["name"] == name)
        pytest.assume(res_dict["description"] == description)

    @pytest.mark.run(order=66)
    @pytest.mark.asyncio
    async def test_a_delete_assistant(self):

        # List assistants.

        assistants = await a_list_assistants(limit=100)
        old_nums = len(assistants)
        for index, v in enumerate(assistants):
            assistant_id = v.assistant_id

            # Delete an assistant.

            await a_delete_assistant(assistant_id=str(assistant_id))

            # List assistants.
            if index == old_nums - 1:
                new_assistants = await a_list_assistants()
                new_nums = len(new_assistants)
                pytest.assume(new_nums == 0)


@pytest.mark.test_async
class TestChat(Base):

        chat_list = ['assistant_id', 'chat_id', 'created_timestamp', 'updated_timestamp', 'metadata']
        chat_keys = set(chat_list)

        @pytest.mark.run(order=55)
        @pytest.mark.asyncio
        async def test_a_create_chat(self):

            for x in range(2):

                # Create a chat.

                res = await a_create_chat(assistant_id=self.assistant_id)
                res_dict = vars(res)
                pytest.assume(res_dict.keys() == self.chat_keys)
                Base.chat_id = res.chat_id

        @pytest.mark.run(order=56)
        @pytest.mark.asyncio
        async def test_a_list_chats(self):

            # List chats.

            nums_limit = 1
            res = await a_list_chats(limit=nums_limit, assistant_id=self.assistant_id)
            pytest.assume(len(res) == nums_limit)

            after_id = res[-1].chat_id
            after_res = await a_list_chats(limit=nums_limit, after=after_id, assistant_id=self.assistant_id)
            pytest.assume(len(after_res) == nums_limit)

            twice_nums_list = await a_list_chats(limit=nums_limit * 2, assistant_id=self.assistant_id)
            pytest.assume(len(twice_nums_list) == nums_limit * 2)
            pytest.assume(after_res[-1] == twice_nums_list[-1])
            pytest.assume(after_res[0] == twice_nums_list[nums_limit])

            before_id = after_res[0].chat_id
            before_res = await a_list_chats(limit=nums_limit, before=before_id, assistant_id=self.assistant_id)
            pytest.assume(len(before_res) == nums_limit)
            pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
            pytest.assume(before_res[0] == twice_nums_list[0])

        @pytest.mark.run(order=57)
        @pytest.mark.asyncio
        async def test_a_get_chat(self):

            # Get a chat.
            res = await a_get_chat(assistant_id=self.assistant_id, chat_id=self.chat_id)
            res_dict = vars(res)
            pytest.assume(res_dict.keys() == self.chat_keys)

        @pytest.mark.run(order=58)
        @pytest.mark.asyncio
        async def test_a_update_chat(self):

            # Update a chat.

            metadata = {"test": "test"}
            res = await a_update_chat(assistant_id=self.assistant_id, chat_id=self.chat_id, metadata=metadata)
            res_dict = vars(res)
            pytest.assume(res_dict.keys() == self.chat_keys)
            pytest.assume(res_dict["metadata"] == metadata)

        @pytest.mark.run(order=65)
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
                if index == old_nums - 1:
                    new_chats = await a_list_chats(assistant_id=self.assistant_id)
                    new_nums = len(new_chats)
                    pytest.assume(new_nums == 0)


@pytest.mark.test_async
class TestMessage(Base):

    message_list = ['assistant_id', 'chat_id', 'message_id', 'role', 'content', 'metadata', 'created_timestamp','updated_timestamp']
    message_keys = set(message_list)

    @pytest.mark.run(order=59)
    @pytest.mark.asyncio
    async def test_a_create_message(self):

        for x in range(2):

            # Create a user message.

            text = "hello, what is the weather like in HongKong?"
            res = await a_create_message(assistant_id=self.assistant_id, chat_id=self.chat_id, text=text)
            res_dict = vars(res)
            logger.info(res_dict)
            pytest.assume(res_dict.keys() == self.message_keys)
            pytest.assume(vars(res_dict["content"])["text"] == text)
            pytest.assume(res_dict["role"] == "user")
            Base.message_id = res.message_id

    @pytest.mark.run(order=60)
    @pytest.mark.asyncio
    async def test_a_list_messages(self):

        # List messages.

        nums_limit = 1
        res = await a_list_messages(limit=nums_limit, assistant_id=self.assistant_id, chat_id=self.chat_id)
        pytest.assume(len(res) == nums_limit)

        after_id = res[-1].message_id
        after_res = await a_list_messages(limit=nums_limit, after=after_id, assistant_id=self.assistant_id,
                                          chat_id=self.chat_id)
        pytest.assume(len(after_res) == nums_limit)

        twice_nums_list = await a_list_messages(limit=nums_limit * 2, assistant_id=self.assistant_id,
                                                chat_id=self.chat_id)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])

        before_id = after_res[0].message_id
        before_res = await a_list_messages(limit=nums_limit, before=before_id, assistant_id=self.assistant_id,
                                           chat_id=self.chat_id)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=61)
    @pytest.mark.asyncio
    async def test_a_get_message(self):

        # Get a message.

        res = await a_get_message(assistant_id=self.assistant_id, chat_id=self.chat_id, message_id=self.message_id)
        res_dict = vars(res)
        pytest.assume(res_dict.keys() == self.message_keys)

    @pytest.mark.run(order=62)
    @pytest.mark.asyncio
    async def test_a_update_message(self):

        # Update a message.

        metadata = {"test": "test"}
        res = await a_update_message(assistant_id=self.assistant_id, chat_id=self.chat_id, message_id=self.message_id,
                                     metadata=metadata)
        res_dict = vars(res)
        pytest.assume(res_dict.keys() == self.message_keys)
        pytest.assume(res_dict["metadata"] == metadata)

    @pytest.mark.run(order=63)
    @pytest.mark.asyncio
    async def test_a_generate_message(self):

        # Generate an assistant message.

        res = await a_generate_message(assistant_id=self.assistant_id, chat_id=self.chat_id,
                                       system_prompt_variables={})
        res_dict = vars(res)
        pytest.assume(res_dict.keys() == self.message_keys)
        pytest.assume(res_dict["role"] == "assistant")
        pytest.assume(res_dict["content"] is not None)
        pytest.assume(res_dict["assistant_id"] == self.assistant_id)
        pytest.assume(res_dict["chat_id"] == self.chat_id)
        pytest.assume(vars(res_dict["content"])["text"] is not None)

    @pytest.mark.run(order=64)
    @pytest.mark.asyncio
    async def test_a_generate_message_by_stream(self):

        assistant_dict = {
            "model_id": Config.chat_completion_model_id,
            "name": "test",
            "description": "test for assistant",
            "memory": AssistantNaiveMemory(),
        }
        assistant_res = await a_create_assistant(**assistant_dict)
        assistant_id = assistant_res.assistant_id
        # create chat

        chat_res = await a_create_chat(assistant_id=assistant_id)
        chat_id = chat_res.chat_id
        logger.info(f'chat_id:{chat_id}')

        # create user message

        user_message = await a_create_message(
            assistant_id=assistant_id,
            chat_id=chat_id,
            text="count from 1 to 100 and separate numbers by comma.",
        )

        # Generate an assistant message by stream.

        stream_res = await a_generate_message(assistant_id=assistant_id, chat_id=chat_id,
                                              system_prompt_variables={}, stream=True)
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
        pytest.assume(set(except_list) == set(real_list))
