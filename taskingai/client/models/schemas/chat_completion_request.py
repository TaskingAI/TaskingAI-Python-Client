# -*- coding: utf-8 -*-

# chat_completion_request.py

"""
This script is automatically generated for TaskingAI python client
Do not modify the file manually

Author: James Yao
Organization: TaskingAI
License: Apache 2.0
"""

from pydantic import BaseModel, Field
from typing import Optional, List, Dict, Union
from ..entities.chat_completion_function_message import ChatCompletionFunctionMessage
from ..entities.chat_completion_system_message import ChatCompletionSystemMessage
from ..entities.chat_completion_user_message import ChatCompletionUserMessage
from ..entities.chat_completion_assistant_message import ChatCompletionAssistantMessage
from ..entities.chat_completion_function import ChatCompletionFunction

__all__ = ["ChatCompletionRequest"]


class ChatCompletionRequest(BaseModel):
    model_id: str = Field(..., min_length=8, max_length=8)
    configs: Optional[Dict] = Field(None)
    stream: bool = Field(False)
    messages: List[
        Union[
            ChatCompletionFunctionMessage,
            ChatCompletionAssistantMessage,
            ChatCompletionUserMessage,
            ChatCompletionSystemMessage,
        ]
    ] = Field(...)
    function_call: Optional[str] = Field(None)
    functions: Optional[List[ChatCompletionFunction]] = Field(None)
