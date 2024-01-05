from enum import Enum

PARENT_LOGGER_NAME = 'taskingai'
DEFAULT_PARENT_LOGGER_LEVEL = 'ERROR'

class ModuleType(str, Enum):
    ASSISTANT = "assistant"
    TOOL = "tool"
    RETRIEVAL = "retrieval"
    INFERENCE = "inference"





