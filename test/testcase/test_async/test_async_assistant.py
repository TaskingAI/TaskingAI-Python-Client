import pytest

from taskingai.assistant import *
from taskingai.client.models import ToolRef, ToolType, RetrievalRef, RetrievalType, RetrievalConfig
from taskingai.assistant.memory import AssistantMessageWindowMemory
from test.config import Config
from test.common.logger import logger
from test.common.utils import assume_assistant_result
from test.testcase.test_async import Base


@pytest.mark.test_async
class TestAssistant(Base):
    @pytest.mark.run(order=51)
    @pytest.mark.asyncio
    async def test_a_create_assistant(self):
        # Create an assistant.

        assistant_dict = {
            "model_id": Config.openai_chat_completion_model_id,
            "name": "test",
            "description": "test for assistant",
            "memory": AssistantMessageWindowMemory(max_tokens=2000),
            "system_prompt_template": [
                "You know the meaning of various numbers.",
                "No matter what the user's language is, you will use the {{langugae}} to explain.",
            ],
            "metadata": {"test": "test"},
            "retrievals": [
                RetrievalRef(
                    type=RetrievalType.COLLECTION,
                    id=self.collection_id,
                ),
            ],
            "retrieval_configs": RetrievalConfig(method="memory", top_k=1, max_tokens=5000, score_threshold=0.5),
            "tools": [
                ToolRef(
                    type=ToolType.PLUGIN,
                    id="open_weather/get_hourly_forecast",
                )
            ],
        }
        for i in range(4):
            if i == 0:
                assistant_dict.update({"memory": {"type": "message_window", "max_messages": 50, "max_tokens": 2000}})
                assistant_dict.update({"retrievals": [{"type": "collection", "id": self.collection_id}]})
                assistant_dict.update(
                    {"retrieval_configs": {"method": "memory", "top_k": 2, "max_tokens": 4000, "score_threshold": 0.5}}
                )
                assistant_dict.update({"tools": [{"type": "plugin", "id": "open_weather/get_hourly_forecast"}]})
            res = await a_create_assistant(**assistant_dict)
            res_dict = vars(res)
            logger.info(f"response_dict:{res_dict}, except_dict:{assistant_dict}")
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
        pytest.assume(res_dict["assistant_id"] == self.assistant_id)

    @pytest.mark.run(order=54)
    @pytest.mark.asyncio
    async def test_a_update_assistant(self):
        # Update an assistant.

        update_data_list = [
            {
                "name": "openai",
                "description": "test for openai",
                "memory": AssistantMessageWindowMemory(max_tokens=2000),
                "retrievals": [
                    RetrievalRef(
                        type=RetrievalType.COLLECTION,
                        id=self.collection_id,
                    ),
                ],
                "retrieval_configs": RetrievalConfig(method="memory", top_k=2, max_tokens=4000, score_threshold=0.5),
                "tools": [
                    ToolRef(
                        type=ToolType.PLUGIN,
                        id="open_weather/get_hourly_forecast",
                    )
                ],
            },
            {
                "name": "openai",
                "description": "test for openai",
                "memory": {"type": "message_window", "max_messages": 50, "max_tokens": 2000},
                "retrievals": [{"type": "collection", "id": self.collection_id}],
                "retrieval_configs": {"method": "memory", "top_k": 2, "max_tokens": 4000, "score_threshold": 0.5},
                "tools": [{"type": "plugin", "id": "open_weather/get_hourly_forecast"}],
            },
        ]
        for update_data in update_data_list:
            res = await a_update_assistant(assistant_id=self.assistant_id, **update_data)
            res_dict = vars(res)
            logger.info(f"response_dict:{res_dict}, except_dict:{update_data}")
            assume_assistant_result(update_data, res_dict)

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
    @pytest.mark.run(order=55)
    @pytest.mark.asyncio
    async def test_a_create_chat(self):
        for x in range(2):
            # Create a chat.
            name = f"test_chat{x + 1}"
            res = await a_create_chat(assistant_id=self.assistant_id, name=name)
            res_dict = vars(res)
            pytest.assume(res_dict["name"] == name)
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
        pytest.assume(res_dict["chat_id"] == self.chat_id)
        pytest.assume(res_dict["assistant_id"] == self.assistant_id)

    @pytest.mark.run(order=58)
    @pytest.mark.asyncio
    async def test_a_update_chat(self):
        # Update a chat.

        metadata = {"test": "test"}
        name = "test_update_chat"
        res = await a_update_chat(assistant_id=self.assistant_id, chat_id=self.chat_id, metadata=metadata, name=name)
        res_dict = vars(res)
        pytest.assume(res_dict["metadata"] == metadata)
        pytest.assume(res_dict["name"] == name)

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
    @pytest.mark.run(order=59)
    @pytest.mark.asyncio
    async def test_a_create_message(self):
        for x in range(2):
            # Create a user message.

            text = "hello, what is the weather like in HongKong?"
            res = await a_create_message(assistant_id=self.assistant_id, chat_id=self.chat_id, text=text)
            res_dict = vars(res)
            logger.info(res_dict)
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
        after_res = await a_list_messages(
            limit=nums_limit, after=after_id, assistant_id=self.assistant_id, chat_id=self.chat_id
        )
        pytest.assume(len(after_res) == nums_limit)

        twice_nums_list = await a_list_messages(
            limit=nums_limit * 2, assistant_id=self.assistant_id, chat_id=self.chat_id
        )
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])

        before_id = after_res[0].message_id
        before_res = await a_list_messages(
            limit=nums_limit, before=before_id, assistant_id=self.assistant_id, chat_id=self.chat_id
        )
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=61)
    @pytest.mark.asyncio
    async def test_a_get_message(self):
        # Get a message.

        res = await a_get_message(assistant_id=self.assistant_id, chat_id=self.chat_id, message_id=self.message_id)
        res_dict = vars(res)
        pytest.assume(res_dict["message_id"] == self.message_id)
        pytest.assume(res_dict["assistant_id"] == self.assistant_id)
        pytest.assume(res_dict["chat_id"] == self.chat_id)

    @pytest.mark.run(order=62)
    @pytest.mark.asyncio
    async def test_a_update_message(self):
        # Update a message.

        metadata = {"test": "test"}
        res = await a_update_message(
            assistant_id=self.assistant_id, chat_id=self.chat_id, message_id=self.message_id, metadata=metadata
        )
        res_dict = vars(res)
        pytest.assume(res_dict["metadata"] == metadata)

    @pytest.mark.run(order=63)
    @pytest.mark.asyncio
    async def test_a_generate_message(self):
        # Generate an assistant message.

        res = await a_generate_message(assistant_id=self.assistant_id, chat_id=self.chat_id, system_prompt_variables={})
        res_dict = vars(res)
        pytest.assume(res_dict["role"] == "assistant")
        pytest.assume(res_dict["content"] is not None)
        pytest.assume(res_dict["assistant_id"] == self.assistant_id)
        pytest.assume(res_dict["chat_id"] == self.chat_id)
        pytest.assume(vars(res_dict["content"])["text"] is not None)

    @pytest.mark.run(order=64)
    @pytest.mark.asyncio
    async def test_a_clean_chat_context(self):
        # Generate an assistant message by no stream.

        res = await a_clean_chat_context(assistant_id=self.assistant_id, chat_id=self.chat_id)
        res_dict = vars(res)
        pytest.assume(res_dict["role"] == "system")
        pytest.assume(res_dict["content"] is not None)
        pytest.assume(res_dict["assistant_id"] == self.assistant_id)
        pytest.assume(res_dict["chat_id"] == self.chat_id)
        pytest.assume(vars(res_dict["content"])["text"] == "context_cleaned")

    @pytest.mark.run(order=64)
    @pytest.mark.asyncio
    async def test_a_generate_message_by_stream(self):
        assistant_dict = {
            "model_id": Config.openai_chat_completion_model_id,
            "name": "test",
            "description": "test for assistant",
            "memory": AssistantMessageWindowMemory(max_tokens=2000),
            "system_prompt_template": [
                "You know the meaning of various numbers.",
                "No matter what the user's language is, you will use the {{langugae}} to explain.",
            ],
            "metadata": {"test": "test"},
            "retrievals": [
                RetrievalRef(
                    type=RetrievalType.COLLECTION,
                    id=self.collection_id,
                ),
            ],
            "retrieval_configs": RetrievalConfig(method="memory", top_k=1, max_tokens=5000, score_threshold=0.04),
            "tools": [
                ToolRef(
                    type=ToolType.PLUGIN,
                    id="open_weather/get_hourly_forecast",
                )
            ],
        }
        assistant_res = await a_create_assistant(**assistant_dict)
        assistant_id = assistant_res.assistant_id
        # create chat

        chat_res = await a_create_chat(assistant_id=assistant_id, name="test_chat")
        chat_id = chat_res.chat_id
        logger.info(f"chat_id:{chat_id}")

        # create user message

        user_message = await a_create_message(
            assistant_id=assistant_id,
            chat_id=chat_id,
            text="count from 1 to 10 and separate numbers by comma.",
        )

        # Generate an assistant message by stream.

        stream_res = await a_generate_message(
            assistant_id=assistant_id, chat_id=chat_id, system_prompt_variables={}, stream=True
        )
        except_list = ["MessageChunk", "Message"]
        real_list = []
        async for item in stream_res:
            if isinstance(item, MessageChunk):
                logger.info(f"MessageChunk: {item.delta}")
                pytest.assume(item.delta is not None)
                real_list.append("MessageChunk")
            elif isinstance(item, Message):
                logger.info(f"Message: {item.message_id}")
                pytest.assume(item.content is not None)
                real_list.append("Message")
        logger.info(f"except_list: {except_list} real_list: {real_list}")
        pytest.assume(set(except_list) == set(real_list))

    @pytest.mark.run(order=70)
    @pytest.mark.asyncio
    async def test_a_assistant_by_user_message_retrieval_and_stream(self):
        # Create an assistant.

        assistant_dict = {
            "model_id": Config.openai_chat_completion_model_id,
            "name": "test",
            "description": "test for assistant",
            "memory": AssistantMessageWindowMemory(max_tokens=2000),
            "system_prompt_template": [
                "You know the meaning of various numbers.",
                "No matter what the user's language is, you will use the {{langugae}} to explain.",
            ],
            "metadata": {"test": "test"},
            "retrievals": [
                RetrievalRef(
                    type=RetrievalType.COLLECTION,
                    id=self.collection_id,
                ),
            ],
            "retrieval_configs": {"method": "user_message", "top_k": 1, "max_tokens": 5000, "score_threshold": 0.5},
        }

        assistant_res = await a_create_assistant(**assistant_dict)
        assistant_res_dict = vars(assistant_res)
        logger.info(f"response_dict:{assistant_res_dict}, except_dict:{assistant_dict}")
        assume_assistant_result(assistant_dict, assistant_res_dict)

        chat_res = await a_create_chat(assistant_id=assistant_res.assistant_id, name="test_chat")
        text = "hello, what is the weather like in HongKong?"
        create_message_res = await a_create_message(
            assistant_id=assistant_res.assistant_id, chat_id=chat_res.chat_id, text=text
        )
        generate_message_res = await a_generate_message(
            assistant_id=assistant_res.assistant_id, chat_id=chat_res.chat_id, system_prompt_variables={}, stream=True
        )
        final_content = ""
        async for item in generate_message_res:
            if isinstance(item, MessageChunk):
                logger.info(f"MessageChunk: {item.delta}")
                pytest.assume(item.delta is not None)
                final_content += item.delta
            elif isinstance(item, Message):
                logger.info(f"Message: {item.message_id}")
                pytest.assume(item.content is not None)
        assert final_content is not None

    @pytest.mark.run(order=70)
    @pytest.mark.asyncio
    async def test_a_assistant_by_memory_retrieval_and_stream(self):
        # Create an assistant.

        assistant_dict = {
            "model_id": Config.openai_chat_completion_model_id,
            "name": "test",
            "description": "test for assistant",
            "memory": AssistantMessageWindowMemory(max_tokens=2000),
            "system_prompt_template": [
                "You know the meaning of various numbers.",
                "No matter what the user's language is, you will use the {{langugae}} to explain.",
            ],
            "metadata": {"test": "test"},
            "retrievals": [
                RetrievalRef(
                    type=RetrievalType.COLLECTION,
                    id=self.collection_id,
                ),
            ],
            "retrieval_configs": {"method": "memory", "top_k": 1, "max_tokens": 5000, "score_threshold": 0.5},
        }

        assistant_res = await a_create_assistant(**assistant_dict)
        assistant_res_dict = vars(assistant_res)
        logger.info(f"response_dict:{assistant_res_dict}, except_dict:{assistant_dict}")
        assume_assistant_result(assistant_dict, assistant_res_dict)

        chat_res = await a_create_chat(assistant_id=assistant_res.assistant_id, name="test_chat")
        text = "hello, what is the weather like in HongKong?"
        create_message_res = await a_create_message(
            assistant_id=assistant_res.assistant_id, chat_id=chat_res.chat_id, text=text
        )
        generate_message_res = await a_generate_message(
            assistant_id=assistant_res.assistant_id, chat_id=chat_res.chat_id, system_prompt_variables={}, stream=True
        )
        final_content = ""
        async for item in generate_message_res:
            if isinstance(item, MessageChunk):
                logger.info(f"MessageChunk: {item.delta}")
                pytest.assume(item.delta is not None)
                final_content += item.delta
            elif isinstance(item, Message):
                logger.info(f"Message: {item.message_id}")
                pytest.assume(item.content is not None)
        assert final_content is not None

    @pytest.mark.run(order=70)
    @pytest.mark.asyncio
    async def test_a_assistant_by_function_call_retrieval_and_stream(self):
        # Create an assistant.

        assistant_dict = {
            "model_id": Config.openai_chat_completion_model_id,
            "name": "test",
            "description": "test for assistant",
            "memory": AssistantMessageWindowMemory(max_tokens=2000),
            "system_prompt_template": [
                "You know the meaning of various numbers.",
                "No matter what the user's language is, you will use the {{langugae}} to explain.",
            ],
            "metadata": {"test": "test"},
            "retrievals": [
                RetrievalRef(
                    type=RetrievalType.COLLECTION,
                    id=self.collection_id,
                ),
            ],
            "retrieval_configs": {"method": "function_call", "top_k": 1, "max_tokens": 5000, "score_threshold": 0.5},
        }

        assistant_res = await a_create_assistant(**assistant_dict)
        assistant_res_dict = vars(assistant_res)
        logger.info(f"response_dict:{assistant_res_dict}, except_dict:{assistant_dict}")
        assume_assistant_result(assistant_dict, assistant_res_dict)

        chat_res = await a_create_chat(assistant_id=assistant_res.assistant_id, name="test_chat")
        text = "hello, what is the weather like in HongKong?"
        create_message_res = await a_create_message(
            assistant_id=assistant_res.assistant_id, chat_id=chat_res.chat_id, text=text
        )
        generate_message_res = await a_generate_message(
            assistant_id=assistant_res.assistant_id, chat_id=chat_res.chat_id, system_prompt_variables={}, stream=True
        )
        final_content = ""
        async for item in generate_message_res:
            if isinstance(item, MessageChunk):
                logger.info(f"MessageChunk: {item.delta}")
                pytest.assume(item.delta is not None)
                final_content += item.delta
            elif isinstance(item, Message):
                logger.info(f"Message: {item.message_id}")
                pytest.assume(item.content is not None)
        assert final_content is not None

    @pytest.mark.run(order=70)
    @pytest.mark.asyncio
    async def test_a_assistant_by_not_support_function_call_retrieval_and_stream(self):
        # Create an assistant.

        assistant_dict = {
            "model_id": Config.anthropic_chat_completion_model_id,
            "name": "test",
            "description": "test for assistant",
            "memory": AssistantMessageWindowMemory(max_tokens=2000),
            "system_prompt_template": [
                "You know the meaning of various numbers.",
                "No matter what the user's language is, you will use the {{langugae}} to explain.",
            ],
            "metadata": {"test": "test"},
            "retrievals": [
                RetrievalRef(
                    type=RetrievalType.COLLECTION,
                    id=self.collection_id,
                ),
            ],
            "retrieval_configs": RetrievalConfig(
                method="function_call",
                top_k=1,
                max_tokens=5000,
            ),
        }
        with pytest.raises(Exception) as e:
            assistant_res = await a_create_assistant(**assistant_dict)
        assert "not support function call to use retrieval" in str(e.value)

    @pytest.mark.run(order=70)
    @pytest.mark.asyncio
    async def test_a_assistant_by_all_tool_and_stream(self):
        # Create an assistant.

        assistant_dict = {
            "model_id": Config.openai_chat_completion_model_id,
            "name": "test",
            "description": "test for assistant",
            "memory": AssistantMessageWindowMemory(max_tokens=2000),
            "system_prompt_template": [
                "You know the meaning of various numbers.",
                "No matter what the user's language is, you will use the {{langugae}} to explain.",
            ],
            "metadata": {"test": "test"},
            "tools": [
                ToolRef(
                    type=ToolType.PLUGIN,
                    id="open_weather/get_hourly_forecast",
                )
            ],
        }

        assistant_res = await a_create_assistant(**assistant_dict)
        assistant_res_dict = vars(assistant_res)
        logger.info(f"response_dict:{assistant_res_dict}, except_dict:{assistant_dict}")
        assume_assistant_result(assistant_dict, assistant_res_dict)

        chat_res = await a_create_chat(assistant_id=assistant_res.assistant_id, name="test_chat")
        text = "hello, what is the weather like in HongKong?"
        create_message_res = await a_create_message(
            assistant_id=assistant_res.assistant_id, chat_id=chat_res.chat_id, text=text
        )
        generate_message_res = await a_generate_message(
            assistant_id=assistant_res.assistant_id, chat_id=chat_res.chat_id, system_prompt_variables={}, stream=True
        )
        final_content = ""
        async for item in generate_message_res:
            if isinstance(item, MessageChunk):
                logger.info(f"MessageChunk: {item.delta}")
                pytest.assume(item.delta is not None)
                final_content += item.delta
            elif isinstance(item, Message):
                logger.info(f"Message: {item.message_id}")
                pytest.assume(item.content is not None)
        assert final_content is not None

    @pytest.mark.run(order=70)
    @pytest.mark.asyncio
    async def test_a_assistant_by_not_support_function_call_tool_and_stream(self):
        # Create an assistant.

        assistant_dict = {
            "model_id": Config.anthropic_chat_completion_model_id,
            "name": "test",
            "description": "test for assistant",
            "memory": AssistantMessageWindowMemory(max_tokens=2000),
            "system_prompt_template": [
                "You know the meaning of various numbers.",
                "No matter what the user's language is, you will use the {{langugae}} to explain.",
            ],
            "metadata": {"test": "test"},
            "tools": [
                ToolRef(
                    type=ToolType.PLUGIN,
                    id="open_weather/get_hourly_forecast",
                )
            ],
        }

        assistant_res = await a_create_assistant(**assistant_dict)
        assistant_res_dict = vars(assistant_res)
