import asyncio
import pytest

from taskingai.assistant import *
from test.config import chat_model_id, sleep_time, text_model_id
from test.common.read_data import data
from test.common.logger import logger
from test.common.utils import list_to_dict
from test.common.utils import assume_assistant
from test.testcase.test_async.base import Base
from taskingai.tool import *
from taskingai.retrieval import *

assistant_data = data.load_yaml("test_assistant_data.yml")


@pytest.mark.test_async
class TestAssistant(Base):

    assistant_list = ['assistant_id', 'created_timestamp', 'description', 'metadata', 'model_id', 'name', 'object',
                      'retrievals', 'system_prompt_template', 'tools', "memory"]
    assistant_keys = set(assistant_list)

    @pytest.mark.parametrize("a_create_assistant_data", assistant_data["test_success_create_assistant"])
    @pytest.mark.run(order=18)
    @pytest.mark.asyncio
    async def test_a_create_assistant(self, a_create_assistant_data):

        # List assistants.
        old_res = await a_list_assistants(limit=100)
        old_nums = len(old_res)

        # Create an assistant.

        assistant_dict = list_to_dict(a_create_assistant_data)
        assistant_dict.update({"model_id": chat_model_id})
        if ("retrievals" in assistant_dict.keys() and len(assistant_dict["retrievals"]) > 0 and
                assistant_dict["retrievals"][0]["type"] == "collection"):
            assistant_dict["retrievals"][0]["id"] = Base.collection_id
        if ("tools" in assistant_dict.keys() and len(assistant_dict["tools"]) > 0 and assistant_dict["tools"][0]["type"]
                == "action"):
            logger.info(f'a_create_assistant_action_id:{Base.action_id}')
            assistant_dict["tools"][0]["id"] = Base.action_id
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

        new_res = await a_list_assistants(limit=100)
        new_nums = len(new_res)
        logger.info(f'old_nums:{old_nums}, new_nums:{new_nums}')
        pytest.assume(new_nums == old_nums + 1)

    @pytest.mark.run(order=19)
    @pytest.mark.asyncio
    async def test_a_list_assistants(self):

        # List assistants.

        nums_limit = 2
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

    @pytest.mark.run(order=20)
    @pytest.mark.asyncio
    async def test_a_get_assistant(self, a_assistant_id):

        # Get an assistant.

        if not Base.assistant_id:
            Base.assistant_id = await a_assistant_id
        res = await a_get_assistant(assistant_id=self.assistant_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.assistant_keys)

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

    @pytest.mark.run(order=32)
    @pytest.mark.asyncio
    async def test_a_delete_assistant(self):

        # List assistants.

        assistants = await a_list_assistants(limit=100)
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
            pytest.assume(new_nums == old_nums - 1 - i)

@pytest.mark.test_async
class TestChat(Base):

        chat_list = ['assistant_id', 'chat_id', 'created_timestamp', 'metadata', 'object']
        chat_keys = set(chat_list)

        @pytest.mark.run(order=22)
        @pytest.mark.asyncio
        async def test_a_create_chat(self):

            # List chats.

            old_res = await a_list_chats(assistant_id=self.assistant_id)
            old_nums = len(old_res)

            for x in range(4):

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
                pytest.assume(new_nums == old_nums + 1 + x)

        @pytest.mark.run(order=23)
        @pytest.mark.asyncio
        async def test_a_list_chats(self):

            # List chats.

            nums_limit = 2
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

        @pytest.mark.run(order=24)
        @pytest.mark.asyncio
        async def test_a_get_chat(self, a_chat_id):

            # Get a chat.

            if not Base.chat_id:
                Base.assistant_id, Base.chat_id = await a_chat_id
            res = await a_get_chat(assistant_id=self.assistant_id, chat_id=self.chat_id)
            res_dict = res.to_dict()
            pytest.assume(res_dict.keys() == self.chat_keys)

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
                pytest.assume(new_nums == old_nums - 1 - index)


@pytest.mark.test_async
class TestMessage(Base):

    message_list = ['object', 'assistant_id', 'chat_id', 'message_id', 'role', 'content', 'metadata',
                    'created_timestamp']
    message_keys = set(message_list)

    @pytest.mark.run(order=26)
    @pytest.mark.asyncio
    async def test_a_create_user_message(self):

        # List messages.

        old_res = await a_list_messages(assistant_id=self.assistant_id, chat_id=self.chat_id)
        old_nums = len(old_res)

        for x in range(4):

            # Create a user message.

            text = f"hello test{x}"
            res = await a_create_user_message(assistant_id=self.assistant_id, chat_id=self.chat_id, text=text)
            res_dict = res.to_dict()
            logger.info(res_dict)
            pytest.assume(res_dict.keys() == self.message_keys)
            pytest.assume(res_dict["content"]["text"] == text)
            pytest.assume(res_dict["role"] == "user")

            # Get a message.

            get_res = await a_get_message(assistant_id=self.assistant_id, chat_id=self.chat_id,
                                          message_id=res_dict["message_id"])
            get_res_dict = get_res.to_dict()
            pytest.assume(get_res_dict.keys() == self.message_keys)

            # List messages.

            new_res = await a_list_messages(assistant_id=self.assistant_id, chat_id=self.chat_id)
            new_nums = len(new_res)
            pytest.assume(new_nums == old_nums + 1 + x)

    @pytest.mark.run(order=27)
    @pytest.mark.asyncio
    async def test_a_list_messages(self):

        # List messages.

        nums_limit = 2
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

    @pytest.mark.run(order=28)
    @pytest.mark.asyncio
    async def test_a_get_message(self, a_message_id):

        # Get a message.

        if not Base.message_id:
            Base.message_id = await a_message_id
        res = await a_get_message(assistant_id=self.assistant_id, chat_id=self.chat_id, message_id=self.message_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.message_keys)

    @pytest.mark.run(order=29)
    @pytest.mark.asyncio
    async def test_a_update_message(self):

        # Update a message.

        metadata = {"test": "test"}
        res = await a_update_message(assistant_id=self.assistant_id, chat_id=self.chat_id, message_id=self.message_id,
                                     metadata=metadata)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.message_keys)
        pytest.assume(res_dict["metadata"] == metadata)

        # Get a message.

        get_res = await a_get_message(assistant_id=self.assistant_id, chat_id=self.chat_id, message_id=self.message_id)
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.message_keys)
        pytest.assume(get_res_dict["metadata"] == metadata)

    @pytest.mark.run(order=30)
    @pytest.mark.asyncio
    async def test_a_generate_assistant_message(self):

        # List messages.

        messages = await a_list_messages(assistant_id=self.assistant_id, chat_id=self.chat_id)
        old_nums = len(messages)

        # Generate an assistant message.

        res = await a_generate_assistant_message(assistant_id=self.assistant_id, chat_id=self.chat_id,
                                                 system_prompt_variables={})
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.message_keys)
        pytest.assume(res_dict["role"] == "assistant")

        # Get a message.

        get_res = await a_get_message(assistant_id=self.assistant_id, chat_id=self.chat_id,
                                      message_id=res_dict["message_id"])
        get_res_dict = get_res.to_dict()
        pytest.assume(get_res_dict.keys() == self.message_keys)
        # List messages.

        new_res = await a_list_messages(assistant_id=self.assistant_id, chat_id=self.chat_id)
        new_nums = len(new_res)
        pytest.assume(new_nums == old_nums + 1)

    @pytest.mark.run(order=30)
    @pytest.mark.asyncio
    async def test_a_generate_assistant_message_by_stream(self):

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

        stream_res = await a_generate_assistant_message(assistant_id=self.assistant_id, chat_id=chat_id,
                                                        system_prompt_variables={}, stream=True, debug=True)
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

    @pytest.mark.run(order=30)
    @pytest.mark.asyncio
    @pytest.mark.test_abnormal
    async def test_a_generate_assistant_message_in_user_message_not_created(self):

        # create chat

        chat_res = await a_create_chat(assistant_id=self.assistant_id)
        chat_id = chat_res.chat_id
        logger.info(f'chat_id:{chat_id}')

        # Generate an assistant message.

        try:
            res = await a_generate_assistant_message(assistant_id=self.assistant_id, chat_id=chat_id,
                                                     system_prompt_variables={})
        except Exception as e:
            logger.info(f'test_a_generate_assistant_message_in_user_message_not_created{e}')
            pytest.assume("There is no user message in the chat context." in str(e))

    @pytest.mark.run(order=30)
    @pytest.mark.asyncio
    @pytest.mark.test_abnormal
    async def test_a_create_user_message_in_generating_assistant_message(self):

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

        await a_generate_assistant_message(assistant_id=self.assistant_id, chat_id=chat_id,
                                                        system_prompt_variables={},
                                                        stream=True, debug=True)

        # create user message

        try:
            user_message = await a_create_user_message(
                assistant_id=self.assistant_id,
                chat_id=chat_id,
                text="count from 100 to 200 and separate numbers by comma.",
            )
        except Exception as e:
            logger.info(f'test_a_create_user_message_in_generating_assistant_message{user_message}')
            pytest.assume("Chat is locked by another generation process. Please try again later." in str(e))

    @pytest.mark.run(order=30)
    @pytest.mark.asyncio
    @pytest.mark.test_abnormal
    async def test_a_generate_assistant_message_in_generating_assistant_message(self):

        # create chat

        chat_res = await a_create_chat(assistant_id=self.assistant_id)
        chat_id = chat_res.chat_id
        logger.info(f'chat_id:{chat_id}')

        # create user message

        await a_create_user_message(
            assistant_id=self.assistant_id,
            chat_id=chat_id,
            text="count from 1 to 100 and separate numbers by comma.",
        )

        # Generate an assistant message by stream.

        stream_res = await a_generate_assistant_message(assistant_id=self.assistant_id, chat_id=chat_id,
                                                        system_prompt_variables={},
                                                        stream=True, debug=True)

        # Generate an assistant message by stream.

        try:
            stream_res = await a_generate_assistant_message(assistant_id=self.assistant_id, chat_id=chat_id,
                                                            system_prompt_variables={},
                                                            stream=True, debug=True)
        except Exception as e:
            logger.info(f'test_a_generate_assistant_message_in_generating_assistant_message{stream_res}')
            pytest.assume("Chat is locked by another generation process. Please try again later." in str(e))

    @pytest.mark.run(order=30)
    @pytest.mark.asyncio
    @pytest.mark.test_abnormal
    async def test_a_generate_assistant_message_in_generated_assistant_message(self):

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

        res = await a_generate_assistant_message(assistant_id=self.assistant_id, chat_id=chat_id,
                                                 system_prompt_variables={})

        # Generate an assistant message by stream.

        try:
            stream_res = await a_generate_assistant_message(assistant_id=self.assistant_id, chat_id=chat_id,
                                                            system_prompt_variables={},
                                                            stream=True, debug=True)
        except Exception as e:
            logger.info(f'test_a_generate_assistant_message_in_generated_assistant_message{e}')
            pytest.assume("Cannot generate another assistant message after an assistant message." in str(e))

    @pytest.mark.run(order=30)
    @pytest.mark.asyncio
    @pytest.mark.test_abnormal
    async def test_a_generate_assistant_message_in_action_deleted_assistant(self):

        # create action

        schema = {
            "openapi": "3.1.0",
            "info": {
                "title": "Get weather data",
                "description": "Retrieves current weather data for a location.",
                "version": "v1.0.0"
            },
            "servers": [
                {
                    "url": "https://weather.example.com"
                }
            ],
            "paths": {
                "/location": {
                    "get": {
                        "description": "Get temperature for a specific location",
                        "operationId": "GetCurrentWeather",
                        "parameters": [
                            {
                                "name": "location",
                                "in": "query",
                                "description": "The city and state to retrieve the weather for",
                                "required": True,
                                "schema": {
                                    "type": "string"
                                }
                            }
                        ],
                        "deprecated": False
                    },
                    "post": {
                        "description": "UPDATE temperature for a specific location",
                        "operationId": "UpdateCurrentWeather",
                        "requestBody": {
                            "required": True,
                            "content": {
                                "application/json": {
                                    "schema": {
                                        "$ref": "#/componeents/schemas/ActionCreateRequest"
                                    }
                                }
                            }
                        },
                        "deprecated": False
                    }
                }
            },
            "components": {
                "schemas": {}
            },
            "security": []
        }
        action_res = await a_bulk_create_actions(schema=schema)
        action_id = action_res[0].action_id

        # create an assistant

        assistant_res = await a_create_assistant(name="test", description="test", model_id=chat_model_id, tools=[{"type": "action", "id": action_id}])
        assistant_id = assistant_res.assistant_id

        # create a chat

        chat_res = await a_create_chat(assistant_id=assistant_id)
        chat_id = chat_res.chat_id

        # create user message

        user_message = await a_create_user_message(
            assistant_id=assistant_id,
            chat_id=chat_id,
            text="count from 1 to 100 and separate numbers by comma.",
        )

        # delete action

        await a_delete_action(action_id=action_id)
        await asyncio.sleep(sleep_time)

        # Generate an assistant message by stream.

        try:
            res = await a_generate_assistant_message(assistant_id=assistant_id, chat_id=chat_id,
                                                     system_prompt_variables={})
        except Exception as e:
            logger.info(f'test_a_generate_assistant_message_in_action_deleted_assistant{e}')
            pytest.assume("Some tools are not found" in str(e))

    @pytest.mark.run(order=30)
    @pytest.mark.asyncio
    @pytest.mark.test_abnormal
    async def test_a_generate_assistant_message_in_collection_deleted_assistant(self):

        # create collection

        collection_res = await a_create_collection(name="test", description="test", embedding_model_id=text_model_id, capacity=1000)
        collection_id = collection_res.collection_id

        # create an assistant

        assistant_res = await a_create_assistant(name="test", description="test", model_id=chat_model_id, retrievals=[{"type": "collection", "id": collection_id}])
        assistant_id = assistant_res.assistant_id

        # create chat

        chat_res = await a_create_chat(assistant_id=assistant_id)
        chat_id = chat_res.chat_id

        # create user message

        user_message = await a_create_user_message(
            assistant_id=assistant_id,
            chat_id=chat_id,
            text="count from 1 to 1000 and separate numbers by comma.",
        )

        # delete collection

        await a_delete_collection(collection_id)
        await asyncio.sleep(sleep_time)

        # Generate an assistant message by stream.

        try:
            res = await a_generate_assistant_message(assistant_id=assistant_id, chat_id=chat_id,
                                                     system_prompt_variables={})
        except Exception as e:
            logger.info(f'test_a_generate_assistant_message_in_collection_deleted_assistant{e}')
            pytest.assume(f"Collections not found" in str(e))
