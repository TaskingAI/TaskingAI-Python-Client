from enum import Enum

PARENT_LOGGER_NAME = 'taskingai'
DEFAULT_PARENT_LOGGER_LEVEL = 'ERROR'

REQUEST_ID: str = "request_id"
CLIENT_VERSION_HEADER = 'X-TaskingAI-Client-Version'


class AssistantToolType(str, Enum):
    action = "action"
    function = "function"


class AssistantRetrievalType(str, Enum):
    collection = "collection"


