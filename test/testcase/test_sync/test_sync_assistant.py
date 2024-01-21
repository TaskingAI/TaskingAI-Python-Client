import pytest

from taskingai.assistant import *
from taskingai.retrieval import *
from taskingai.tool import *
from taskingai.assistant.memory import AssistantNaiveMemory
from test.config import chat_completion_model_id
from test.common.read_data import data
from test.common.logger import logger
from test.common.utils import list_to_dict
from test.common.utils import assume_assistant
import re


assistant_data = data.load_yaml("test_assistant_data.yml")


@pytest.mark.test_sync
class TestAssistant:
    assistant_list = [
        "assistant_id",
        "created_timestamp",
        "description",
        "metadata",
        "model_id",
        "name",
        "object",
        "retrievals",
        "system_prompt_template",
        "tools",
        "memory",
    ]
    assistant_keys = set(assistant_list)

    @pytest.mark.parametrize("create_assistant_data", assistant_data["test_success_create_assistant"])
    @pytest.mark.run(order=18)
    def test_create_assistant(self, collection_id, action_id, create_assistant_data):
        # Create an assistant.

        assistant_dict = list_to_dict(create_assistant_data)
        assistant_dict.update({"model_id": chat_completion_model_id})
        if (
            "retrievals" in assistant_dict.keys()
            and len(assistant_dict["retrievals"]) > 0
            and assistant_dict["retrievals"][0]["type"] == "collection"
        ):
            assistant_dict["retrievals"][0]["id"] = collection_id
        if (
            "tools" in assistant_dict.keys()
            and len(assistant_dict["tools"]) > 0
            and assistant_dict["tools"][0]["type"] == "action"
        ):
            assistant_dict["tools"][0]["id"] = action_id
        assistant_dict.update({"memory": AssistantNaiveMemory()})
        res = create_assistant(**assistant_dict)
        res_dict = res.to_dict()
        logger.info(f"response_dict:{res_dict}, except_dict:{assistant_dict}")
        pytest.assume(res_dict.keys() == self.assistant_keys)
        assume_assistant(res_dict, assistant_dict)

    @pytest.mark.run(order=19)
    def test_list_assistants(self):
        # List assistants.

        nums_limit = 1
        res = list_assistants(limit=nums_limit)
        pytest.assume(len(res) == nums_limit)

        after_id = res[-1].assistant_id
        after_res = list_assistants(limit=nums_limit, after=after_id)
        pytest.assume(len(after_res) == nums_limit)

        twice_nums_list = list_assistants(limit=nums_limit * 2)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])

        before_id = after_res[0].assistant_id
        before_res = list_assistants(limit=nums_limit, before=before_id)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=20)
    def test_get_assistant(self, assistant_id):
        # Get an assistant.

        res = get_assistant(assistant_id=assistant_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.assistant_keys)

    @pytest.mark.run(order=21)
    def test_update_assistant(self, assistant_id):
        # Update an assistant.

        name = "openai"
        description = "test for openai"
        res = update_assistant(assistant_id=assistant_id, name=name, description=description)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.assistant_keys)
        pytest.assume(res_dict["name"] == name)
        pytest.assume(res_dict["description"] == description)

    @pytest.mark.run(order=33)
    def test_delete_assistant(self):
        # List assistants.

        assistants = list_assistants(limit=100)
        old_nums = len(assistants)
        for i, v in enumerate(assistants):
            assistant_id = v.assistant_id

            # Delete an assistant.

            delete_assistant(assistant_id=str(assistant_id))

            # List assistants.

            new_assistants = list_assistants()
            assistant_ids = [j.assistant_id for j in new_assistants]
            pytest.assume(assistant_id not in assistant_ids)
            new_nums = len(new_assistants)
            pytest.assume(new_nums == old_nums - 1 - i)


@pytest.mark.test_sync
class TestChat:
    chat_list = ["assistant_id", "chat_id", "created_timestamp", "metadata", "object"]
    chat_keys = set(chat_list)

    @pytest.mark.run(order=22)
    def test_create_chat(self, assistant_id):
        for x in range(2):
            # Create a chat.

            res = create_chat(assistant_id=assistant_id)
            res_dict = res.to_dict()
            pytest.assume(res_dict.keys() == self.chat_keys)

    @pytest.mark.run(order=23)
    def test_list_chats(self, assistant_id):
        # List chats.

        nums_limit = 1
        res = list_chats(limit=nums_limit, assistant_id=assistant_id)
        pytest.assume(len(res) == nums_limit)

        after_id = res[-1].chat_id
        after_res = list_chats(limit=nums_limit, after=after_id, assistant_id=assistant_id)
        pytest.assume(len(after_res) == nums_limit)

        twice_nums_list = list_chats(limit=nums_limit * 2, assistant_id=assistant_id)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])

        before_id = after_res[0].chat_id
        before_res = list_chats(limit=nums_limit, before=before_id, assistant_id=assistant_id)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=24)
    def test_get_chat(self, assistant_id, chat_id):
        # Get a chat.

        res = get_chat(assistant_id=assistant_id, chat_id=chat_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.chat_keys)

    @pytest.mark.run(order=25)
    def test_update_chat(self, assistant_id, chat_id):
        # Update a chat.

        metadata = {"test": "test"}
        res = update_chat(assistant_id=assistant_id, chat_id=chat_id, metadata=metadata)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.chat_keys)
        pytest.assume(res_dict["metadata"] == metadata)

    @pytest.mark.run(order=32)
    def test_delete_chat(self, assistant_id):
        # List chats.

        chats = list_chats(assistant_id=assistant_id)
        old_nums = len(chats)
        for index, chat in enumerate(chats):
            chat_id = chat.chat_id

            # Delete a chat.

            delete_chat(assistant_id=assistant_id, chat_id=str(chat_id))

            # List chats.

            new_chats = list_chats(assistant_id=assistant_id)
            chat_ids = [i.chat_id for i in new_chats]
            pytest.assume(chat_id not in chat_ids)
            new_nums = len(new_chats)
            pytest.assume(new_nums == old_nums - 1 - index)


@pytest.mark.test_sync
class TestMessage:
    message_list = [
        "object",
        "assistant_id",
        "chat_id",
        "message_id",
        "role",
        "content",
        "metadata",
        "created_timestamp",
    ]
    message_keys = set(message_list)

    @pytest.mark.run(order=26)
    def test_create_message(self, assistant_id, chat_id):
        for x in range(2):
            # Create a user message.

            text = "hello"
            res = create_message(assistant_id=assistant_id, chat_id=chat_id, text=text)
            res_dict = res.to_dict()
            logger.info(res_dict)
            pytest.assume(res_dict.keys() == self.message_keys)
            pytest.assume(res_dict["content"]["text"] == text)
            pytest.assume(res_dict["role"] == "user")

    @pytest.mark.run(order=27)
    def test_list_messages(self, assistant_id, chat_id):
        # List messages.

        nums_limit = 1
        res = list_messages(limit=nums_limit, assistant_id=assistant_id, chat_id=chat_id)
        pytest.assume(len(res) == nums_limit)
        after_id = res[-1].message_id
        after_res = list_messages(limit=nums_limit, after=after_id, assistant_id=assistant_id, chat_id=chat_id)
        pytest.assume(len(after_res) == nums_limit)
        twice_nums_list = list_messages(limit=nums_limit * 2, assistant_id=assistant_id, chat_id=chat_id)
        pytest.assume(len(twice_nums_list) == nums_limit * 2)
        pytest.assume(after_res[-1] == twice_nums_list[-1])
        pytest.assume(after_res[0] == twice_nums_list[nums_limit])
        before_id = after_res[0].message_id
        before_res = list_messages(limit=nums_limit, before=before_id, assistant_id=assistant_id, chat_id=chat_id)
        pytest.assume(len(before_res) == nums_limit)
        pytest.assume(before_res[-1] == twice_nums_list[nums_limit - 1])
        pytest.assume(before_res[0] == twice_nums_list[0])

    @pytest.mark.run(order=28)
    def test_get_message(self, assistant_id, chat_id, message_id):
        # Get a message.

        res = get_message(assistant_id=assistant_id, chat_id=chat_id, message_id=message_id)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.message_keys)

    @pytest.mark.run(order=29)
    def test_update_message(self, assistant_id, chat_id, message_id):
        # Update a message.

        metadata = {"test": "test"}
        res = update_message(assistant_id=assistant_id, chat_id=chat_id, message_id=message_id, metadata=metadata)
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.message_keys)
        pytest.assume(res_dict["metadata"] == metadata)

    @pytest.mark.run(order=30)
    def test_generate_message(self, assistant_id, chat_id):
        # Generate an assistant message by no stream.

        res = generate_message(assistant_id=assistant_id, chat_id=chat_id, system_prompt_variables={})
        res_dict = res.to_dict()
        pytest.assume(res_dict.keys() == self.message_keys)
        pytest.assume(res_dict["role"] == "assistant")

    @pytest.mark.run(order=30)
    def test_generate_message_by_stream(self):
        # List assistants.

        assistants = list_assistants()
        assistant_id = assistants[-1].assistant_id
        logger.info(f"assistant_id: {assistant_id}")

        # create chat

        chat_res = create_chat(assistant_id=assistant_id)
        chat_id = chat_res.chat_id
        logger.info(f"chat_id: {chat_id}")

        # create user message

        user_message: Message = create_message(
            assistant_id=assistant_id, chat_id=chat_id, text="count from 1 to 10 and separate numbers by comma."
        )

        # Generate an assistant message by stream.

        stream_res = generate_message(
            assistant_id=assistant_id, chat_id=chat_id, system_prompt_variables={}, stream=True
        )
        except_list = [i + 1 for i in range(10)]
        real_str = ""
        for item in stream_res:
            if isinstance(item, MessageChunk):
                logger.debug(f"MessageChunk: {item.delta}")
                real_str += item.delta

            elif isinstance(item, Message):
                logger.debug(f"Message: {item.message_id}")
                pytest.assume(item.content is not None)

        real_list = [int(num) for num in re.findall(r"\b\d+\b", real_str)]
        logger.debug(f"Message: {real_str}")
        logger.debug(f"except_list: {except_list} real_list: {real_list}")
        pytest.assume(set(except_list) == set(real_list))
