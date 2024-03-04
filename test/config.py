import os
from dotenv import load_dotenv
import taskingai

load_dotenv()


class Config:

    chat_completion_model_id = os.environ.get("CHAT_COMPLETION_MODEL_ID")
    if not chat_completion_model_id:
        raise ValueError("chat_completion_model_id is not defined")

    text_embedding_model_id = os.environ.get("TEXT_EMBEDDING_MODEL_ID")
    if not chat_completion_model_id:
        raise ValueError("chat_completion_model_id is not defined")

    taskingai_host = os.environ.get("TASKINGAI_HOST")
    if not taskingai_host:
        raise ValueError("taskingai_host is not defined")

    taskingai_apikey = os.environ.get("TASKINGAI_API_KEY")
    if not taskingai_apikey:
        raise ValueError("taskingai_apikey is not defined")

    taskingai.init(api_key=taskingai_apikey, host=taskingai_host)

    sleep_time = 1
