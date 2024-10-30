from taskingai.client.models import (
    AssistantMemory,
    AssistantMemoryType,
)

__all__ = [
    "AssistantMemory",
    "AssistantMemoryType",
    "AssistantMessageWindowMemory",
]


class AssistantMessageWindowMemory(AssistantMemory):
    def __init__(self, max_tokens: int):
        super().__init__(type=AssistantMemoryType.MESSAGE_WINDOW, max_tokens=max_tokens)
