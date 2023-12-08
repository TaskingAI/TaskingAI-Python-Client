import pytest
import allure

from taskingai.inference import *
from test.config import text_model_id, chat_model_id
from test.common.utils import logger


@allure.epic("test_async_inference")
@allure.feature("test_a_chat_completion")
@pytest.mark.a_sync
class TestChatCompletion:

    @allure.story("test_a_chat_completion")
    @pytest.mark.run(order=4)
    @pytest.mark.asyncio
    async def test_a_chat_completion(self):
        # normal chat completion.
        normal_res = await a_chat_completion(
            model_id=chat_model_id,
            messages=[
                SystemMessage("You are a professional assistant."),
                UserMessage("Hi"),
            ]
        )
        pytest.assume(normal_res.finish_reason == "stop")
        pytest.assume(normal_res.message.content)
        pytest.assume(normal_res.message.role == "assistant")
        pytest.assume(normal_res.message.function_call is None)

        # multi round chat completion.
        multi_round_res = await a_chat_completion(
            model_id=chat_model_id,
            messages=[
                SystemMessage("You are a professional assistant."),
                UserMessage("Hi"),
                AssistantMessage("Hello! How can I assist you today?"),
                UserMessage("Can you tell me a joke?"),
                AssistantMessage(
                    "Sure, here is a joke for you: Why don't scientists trust atoms? Because they make up everything!"),
                UserMessage("That's funny. Can you tell me another one?"),
            ]
        )

        pytest.assume(multi_round_res.finish_reason == "stop")
        pytest.assume(multi_round_res.message.content)
        pytest.assume(multi_round_res.message.role == "assistant")
        pytest.assume(multi_round_res.message.function_call is None)

        # config max tokens chat completion.
        max_tokens_res = await a_chat_completion(
            model_id=chat_model_id,
            messages=[
                SystemMessage("You are a professional assistant."),
                UserMessage("Hi"),
                AssistantMessage("Hello! How can I assist you today?"),
                UserMessage("Can you tell me a joke?"),
                AssistantMessage(
                    "Sure, here is a joke for you: Why don't scientists trust atoms? Because they make up everything!"),
                UserMessage("That's funny. Can you tell me another one?"),
            ],
            configs={
                "max_tokens": 10
            }
        )
        pytest.assume(max_tokens_res.finish_reason == "length")
        pytest.assume(max_tokens_res.message.content)
        pytest.assume(max_tokens_res.message.role == "assistant")
        pytest.assume(max_tokens_res.message.function_call is None)

        # # chat completion with function call.
        # function = await a_function
        # function_res = await a_chat_completion(
        #     model_id=chat_model_id,
        #     messages=[
        #         SystemMessage("You are a professional assistant."),
        #         UserMessage("What is the result of 112 plus 22?"),
        #     ],
        #     functions=[function]
        # )
        # logger.info(function_res)
        # pytest.assume(function_res.finish_reason == "function_call")
        # pytest.assume(function_res.message.content is None)
        # pytest.assume(function_res.message.role == "assistant")
        # pytest.assume(function_res.message.function_call)
        #
        # # add function message.
        # content = "134"
        # function_message_res = await a_chat_completion(
        #     model_id=chat_model_id,
        #     messages=[
        #         SystemMessage("You are a professional assistant."),
        #         UserMessage("What is the result of 112 plus 22?"),
        #         function_res.message,
        #         FunctionMessage(name=function.name, content=content),
        #     ],
        #     functions=[function]
        # )
        # pytest.assume(function_message_res.finish_reason == "stop")
        # pytest.assume(content in function_message_res.message.content)
        # pytest.assume(function_message_res.message.role == "assistant")
        # pytest.assume(function_message_res.message.function_call is None)

        # chat completion with stream.
        stream_res = await a_chat_completion(model_id=chat_model_id,
                                             messages=[
                                                 SystemMessage("You are a professional assistant."),
                                                 UserMessage("count from 1 to 50 and separate numbers by comma."),
                                             ],
                                             stream=True
                                             )
        except_list = [i + 1 for i in range(50)]
        real_list = []
        async for item in stream_res:
            if isinstance(item, ChatCompletionChunk):
                logger.info(f"Message: {item.delta}")
                if item.delta.isdigit():
                    real_list.append(int(item.delta))
            elif isinstance(item, ChatCompletion):
                logger.info(f"Message: {item.finish_reason}")
                pytest.assume(item.finish_reason == "stop")
        pytest.assume(set(except_list) == set(real_list))


@allure.epic("test_async_inference")
@allure.feature("test_a_text_embedding")
@pytest.mark.a_sync
class TestTextEmbedding:

    @allure.story("test_a_text_embedding")
    @pytest.mark.run(order=0)
    @pytest.mark.asyncio
    async def test_a_text_embedding(self):

        # Text embedding with str.
        input_str = "Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
        str_res = await a_text_embedding(model_id=text_model_id, input=input_str)
        pytest.assume(len(str_res) > 0)
        for score in str_res:
            pytest.assume(float(-1) <= score <= float(1))

        # Text embedding with str_list.
        input_list = ["hello", "world"]
        input_list_length = len(input_list)
        list_res = await a_text_embedding(model_id=text_model_id, input=input_list)
        pytest.assume(len(list_res) == input_list_length)
        for str_res in list_res:
            pytest.assume(len(str_res) > 0)
            for score in str_res:
                pytest.assume(float(-1) <= score <= float(1))
