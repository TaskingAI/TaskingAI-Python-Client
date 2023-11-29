from enum import Enum

PARENT_LOGGER_NAME = 'taskingai'
DEFAULT_PARENT_LOGGER_LEVEL = 'ERROR'

class ModuleType(str, Enum):
    assistant = "assistant"
    tool = "tool"
    retrieval = "retrieval"
    inference = "inference"





