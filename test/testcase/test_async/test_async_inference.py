import pytest

from taskingai.inference import *
from test.config import Config
from test.common.logger import logger
from test.common.utils import assume_text_embedding_result

@pytest.mark.test_async
class TestChatCompletion:

    @pytest.mark.run(order=4)
    @pytest.mark.asyncio
    async def test_a_chat_completion_with_normal(self):

        # normal chat completion.
        normal_chat_completion_data_list = [
            {
                "model_id": Config.openai_chat_completion_model_id,
                "messages": [
                    SystemMessage("You are a professional assistant."),
                    UserMessage("Hi"),
                ],
            },
            {
                "model_id": Config.openai_chat_completion_model_id,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a professional assistant."
                    },
                    {
                        "role": "user",
                        "content": "Hi"
                    }
                ],
            }
        ]
        for normal_chat_completion_data in normal_chat_completion_data_list:
            normal_res = await a_chat_completion(**normal_chat_completion_data)
            pytest.assume(normal_res.finish_reason == "stop")
            pytest.assume(normal_res.message.content is not None)
            pytest.assume(normal_res.message.role == "assistant")
            pytest.assume(normal_res.message.function_calls is None)

    @pytest.mark.run(order=4)
    @pytest.mark.asyncio
    async def test_a_chat_completion_with_multi_round(self):

        # multi round chat completion.
        multi_round_data_list = [
            {
                "model_id": Config.openai_chat_completion_model_id,
                "messages": [
                    SystemMessage("You are a professional assistant."),
                    UserMessage("Hi"),
                    AssistantMessage("Hello! How can I assist you today?"),
                    UserMessage("Can you tell me a joke?"),
                    AssistantMessage(
                        "Sure, here is a joke for you: Why don't scientists trust atoms? Because they make up everything!"),
                    UserMessage("That's funny. Can you tell me another one?"),
                ]
            },
            {
                "model_id": Config.openai_chat_completion_model_id,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a professional assistant."
                    },
                    {
                        "role": "user",
                        "content": "Hi"
                    },
                    {
                        "role": "assistant",
                        "content": "Hello! How can I assist you today?"
                    },
                    {
                        "role": "user",
                        "content": "Can you tell me a joke?"
                    },
                    {
                        "role": "assistant",
                        "content": "Sure, here is a joke for you: Why don't scientists trust atoms? Because they make up everything!"
                    },
                    {
                        "role": "user",
                        "content": "That's funny. Can you tell me another one?"
                    }
                ]
            }
        ]
        for multi_round_data in multi_round_data_list:
            multi_round_res = await a_chat_completion(**multi_round_data)
            pytest.assume(multi_round_res.finish_reason == "stop")
            pytest.assume(multi_round_res.message.content is not None)
            pytest.assume(multi_round_res.message.role == "assistant")
            pytest.assume(multi_round_res.message.function_calls is None)

    @pytest.mark.run(order=4)
    @pytest.mark.asyncio
    async def test_a_chat_completion_with_max_tokens(self):

        # config max tokens chat completion.

        max_tokens_data_list = [
            {
                "model_id": Config.openai_chat_completion_model_id,
                "messages": [
                    SystemMessage("You are a professional assistant."),
                    UserMessage("Hi"),
                    AssistantMessage("Hello! How can I assist you today?"),
                    UserMessage("Can you tell me a joke?"),
                    AssistantMessage(
                        "Sure, here is a joke for you: Why don't scientists trust atoms? Because they make up everything!"),
                    UserMessage("That's funny. Can you tell me another one?"),
                ],
                "configs": {
                    "max_tokens": 10

                }
            },
            {
                "model_id": Config.openai_chat_completion_model_id,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a professional assistant."
                    },
                    {
                        "role": "user",
                        "content": "Hi"
                    },
                    {
                        "role": "assistant",
                        "content": "Hello! How can I assist you today?"
                    },
                    {
                        "role": "user",
                        "content": "Can you tell me a joke?"
                    },
                    {
                        "role": "assistant",
                        "content": "Sure, here is a joke for you: Why don't scientists trust atoms? Because they make up everything!"
                    },
                    {
                        "role": "user",
                        "content": "That's funny. Can you tell me another one?"
                    }
                ],
                "configs": {
                    "max_tokens": 10

                }
            }
        ]
        for max_tokens_data in max_tokens_data_list:
            max_tokens_res = await a_chat_completion(**max_tokens_data)
            pytest.assume(max_tokens_res.finish_reason == "length")
            pytest.assume(max_tokens_res.message.content is not None)
            pytest.assume(max_tokens_res.message.role == "assistant")
            pytest.assume(max_tokens_res.message.function_calls is None)

    @pytest.mark.run(order=4)
    @pytest.mark.asyncio
    async def test_a_chat_completion_with_function_call(self):

        # chat completion with function call.

        function_list = [
            Function(
                name="plus_a_and_b",
                description="Sum up a and b and return the result",
                parameters={
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "integer",
                            "description": "The first number"
                        },
                        "b": {
                            "type": "integer",
                            "description": "The second number"
                        }
                    },
                    "required": ["a", "b"]
                },
            ),

            {
                "name": "plus_a_and_b",
                "description": "Sum up a and b and return the result",
                "parameters": {
                    "type": "object",
                    "properties": {
                        "a": {
                            "type": "integer",
                            "description": "The first number"
                        },
                        "b": {
                            "type": "integer",
                            "description": "The second number"
                        }
                    },
                    "required": ["a", "b"]
                }
            }
        ]
        for function in function_list:


            function_call_res = await a_chat_completion(
                model_id=Config.openai_chat_completion_model_id,
                messages=[
                    UserMessage("What is the result of 112 plus 22?"),
                ],
                functions=[function]
            )
            pytest.assume(function_call_res.finish_reason == "function_calls")
            pytest.assume(function_call_res.message.content is None)
            pytest.assume(function_call_res.message.role == "assistant")
            pytest.assume(function_call_res.message.function_calls is not None)

            # get the function call result
            def plus_a_and_b(a, b):
                return a + b

            arguments = function_call_res.message.function_calls[0].arguments
            function_id = function_call_res.message.function_calls[0].id
            function_call_result = plus_a_and_b(**arguments)

            # chat completion with the function result

            function_message_list = [
                {
                    "role": "function",
                    "id": function_id,
                    "content": str(function_call_result)
                },
                FunctionMessage(id=function_id, content=str(function_call_result))
            ]
            for function_message in function_message_list:
                function_call_result_res = await a_chat_completion(
                    model_id=Config.openai_chat_completion_model_id,
                    messages=[
                        UserMessage("What is the result of 112 plus 22?"),
                        function_call_res.message,
                        function_message
                    ],
                    functions=[function]
                )
                pytest.assume(function_call_result_res.finish_reason == "stop")
                pytest.assume(function_call_result_res.message.content is not None)
                pytest.assume(function_call_result_res.message.role == "assistant")
                pytest.assume(function_call_result_res.message.function_calls is None)

    @pytest.mark.run(order=4)
    @pytest.mark.asyncio
    async def test_a_chat_completion_with_stream(self):

        # chat completion with stream.

        stream_data_list = [
            {
                "model_id": Config.openai_chat_completion_model_id,
                "messages": [
                    SystemMessage("You are a professional assistant."),
                    UserMessage("count from 1 to 10 and separate numbers by comma."),
                ],
                "stream": True
            },
            {
                "model_id": Config.openai_chat_completion_model_id,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a professional assistant."
                    },
                    {
                        "role": "user",
                        "content": "count from 1 to 10 and separate numbers by comma."
                    }
                ],
                "stream": True
            }
        ]
        for stream_data in stream_data_list:
            stream_res = await a_chat_completion(**stream_data)
            except_list = [i + 1 for i in range(10)]
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


@pytest.mark.test_async
class TestTextEmbedding:

    @pytest.mark.run(order=0)
    @pytest.mark.asyncio
    async def test_a_text_embedding_with_str(self):

        # Text embedding with str.

        input_str = "Machine learning is a subfield of artificial intelligence (AI) that involves the development of algorithms that allow computers to learn from and make decisions or predictions based on data."
        str_res = await a_text_embedding(model_id=Config.openai_text_embedding_model_id, input=input_str)
        assume_text_embedding_result(str_res)

    @pytest.mark.run(order=0)
    @pytest.mark.asyncio
    async def test_a_text_embedding_with_str_list(self):

        # Text embedding with str_list.

        input_list = ["hello", "world"]
        input_list_length = len(input_list)
        list_res = await a_text_embedding(model_id=Config.openai_text_embedding_model_id, input=input_list)
        pytest.assume(len(list_res) == input_list_length)
        for res in list_res:
            assume_text_embedding_result(res)
