from taskingai.client.models import (
    AssistantMemory,
    AssistantMemoryType,
)

__all__ = [
    "AssistantMemory",
    "AssistantMemoryType",
    "AssistantNaiveMemory",
    "AssistantZeroMemory",
    "AssistantMessageWindowMemory",
]


class AssistantNaiveMemory(AssistantMemory):
    def __init__(self):
        super().__init__(type=AssistantMemoryType.NAIVE)


class AssistantZeroMemory(AssistantMemory):
    def __init__(self):
        super().__init__(type=AssistantMemoryType.ZERO)


class AssistantMessageWindowMemory(AssistantMemory):
    def __init__(self, max_messages: int, max_tokens: int):
        super().__init__(type=AssistantMemoryType.MESSAGE_WINDOW, max_messages=max_messages, max_tokens=max_tokens)
