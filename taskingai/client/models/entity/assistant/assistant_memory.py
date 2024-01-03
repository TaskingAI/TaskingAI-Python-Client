from enum import Enum
from pydantic import BaseModel, Field
from abc import ABC
from typing import Optional, Dict


class AssistantMemoryType(str, Enum):
    ZERO = "zero"
    NAIVE = "naive"
    MESSAGE_WINDOW = "message_window"


class AssistantMemory(BaseModel, ABC):
    type: AssistantMemoryType = Field(..., description="The type of the memory.")


class AssistantMessageWindowMemory(AssistantMemory):
    type: AssistantMemoryType = Field(AssistantMemoryType.MESSAGE_WINDOW, Literal=AssistantMemoryType.MESSAGE_WINDOW)
    max_messages: int = Field(...)
    max_tokens: int = Field(...)


class AssistantNaiveMemory(AssistantMemory):
    type: AssistantMemoryType = Field(AssistantMemoryType.NAIVE, Literal=AssistantMemoryType.NAIVE)


class AssistantZeroMemory(AssistantMemory):
    type: AssistantMemoryType = Field(AssistantMemoryType.ZERO, Literal=AssistantMemoryType.ZERO)


def build_assistant_memory(memory_dict: Dict) -> Optional[AssistantMemory]:
    # Check if the memory dictionary is provided and has the 'type' key
    if not memory_dict or 'type' not in memory_dict:
        return None

    memory_type = memory_dict['type']

    if memory_type == AssistantMemoryType.ZERO.value:
        # For zero memory, no additional information is needed
        return AssistantZeroMemory()

    elif memory_type == AssistantMemoryType.NAIVE.value:
        # For naive memory, no additional configuration is needed
        return AssistantNaiveMemory()

    elif memory_type == AssistantMemoryType.MESSAGE_WINDOW.value:
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


