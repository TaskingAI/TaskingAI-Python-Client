from enum import Enum
from pydantic import BaseModel, Field
from abc import ABC
from typing import Optional, Dict


class AssistantMemoryType(str, Enum):
    zero = "zero"
    naive = "naive"
    message_window = "message_window"


class AssistantMemory(BaseModel, ABC):
    type: AssistantMemoryType = Field(..., description="The type of the memory.")


class AssistantMessageWindowMemory(AssistantMemory):
    type: AssistantMemoryType = Field(AssistantMemoryType.message_window, Literal=AssistantMemoryType.message_window)
    max_messages: int = Field(...)
    max_tokens: int = Field(...)


class AssistantNaiveMemory(AssistantMemory):
    type: AssistantMemoryType = Field(AssistantMemoryType.naive, Literal=AssistantMemoryType.naive)


class AssistantZeroMemory(AssistantMemory):
    type: AssistantMemoryType = Field(AssistantMemoryType.zero, Literal=AssistantMemoryType.zero)


def build_assistant_memory(memory_dict: Dict) -> Optional[AssistantMemory]:
    # Check if the memory dictionary is provided and has the 'type' key
    if not memory_dict or 'type' not in memory_dict:
        return None

    memory_type = memory_dict['type']

    if memory_type == AssistantMemoryType.zero.value:
        # For zero memory, no additional information is needed
        return AssistantZeroMemory()

    elif memory_type == AssistantMemoryType.naive.value:
        # For naive memory, no additional configuration is needed
        return AssistantNaiveMemory()

    elif memory_type == AssistantMemoryType.message_window.value:
        # For message window memory, additional configuration is needed
        max_messages = memory_dict.get('max_messages')
        max_tokens = memory_dict.get('max_tokens')

        # Validate that required fields are present
        if max_messages is None or max_tokens is None:
            return None

        return AssistantMessageWindowMemory(max_messages=max_messages, max_tokens=max_tokens)

    else:
        # If the memory type is unknown, return None
        return None


