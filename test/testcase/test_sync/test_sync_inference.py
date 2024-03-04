import pytest
from taskingai.inference import *
from test.config import Config
from test.common.logger import logger
from test.common.utils import assume_text_embedding_result


@pytest.mark.test_sync
class TestChatCompletion:

    @pytest.mark.run(order=1)
    def test_chat_completion(self):

        # normal chat completion.

        normal_res = chat_completion(
            model_id=Config.chat_completion_model_id,
            messages=[
                SystemMessage("You are a professional assistant."),
                UserMessage("Hi"),
            ]
        )
        pytest.assume(normal_res.finish_reason == "stop")
        pytest.assume(normal_res.message.content)
        pytest.assume(normal_res.message.role == "assistant")
        pytest.assume(normal_res.message.function_calls is None)

        # multi round chat completion.

        multi_round_res = chat_completion(
            model_id=Config.chat_completion_model_id,
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
        pytest.assume(multi_round_res.message.function_calls is None)

        # config max tokens chat completion.

        max_tokens_res = chat_completion(
            model_id=Config.chat_completion_model_id,
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
        pytest.assume(max_tokens_res.message.function_calls is None)

        # chat completion with stream.

        stream_res = chat_completion(model_id=Config.chat_completion_model_id,
                                     messages=[
                                            SystemMessage("You are a professional assistant."),
                                            UserMessage("count from 1 to 50 and separate numbers by comma."),
                                        ],
                                     stream=True
                                     )
        except_list = [i+1 for i in range(50)]
        real_list = []
        for item in stream_res:
            if isinstance(item, ChatCompletionChunk):
                logger.info(f"Message: {item.delta}")
                if item.delta.isdigit():
                    real_list.append(int(item.delta))
            elif isinstance(item, ChatCompletion):
                logger.info(f"Message: {item.finish_reason}")
                pytest.assume(item.finish_reason == "stop")
        logger.info(f"except_list: {except_list} real_list: {real_list}")
        pytest.assume(set(except_list) == set(real_list))


@pytest.mark.test_sync
class TestTextEmbedding:

    @pytest.mark.run(order=0)
    def test_text_embedding(self):

        # Text embedding with str.

        input_str = "Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
        str_res = text_embedding(model_id=Config.text_embedding_model_id, input=input_str)
        assume_text_embedding_result(str_res)

        # Text embedding with str_list.

        input_list = ["hello", "world"]
        input_list_length = len(input_list)
        list_res = text_embedding(model_id=Config.text_embedding_model_id, input=input_list)
        pytest.assume(len(list_res) == input_list_length)
        for res in list_res:
            assume_text_embedding_result(res)
