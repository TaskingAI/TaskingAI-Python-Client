import os


class Config:

    chat_completion_model_id = os.environ.get("CHAT_COMPLETION_MODEL_ID")
    if not chat_completion_model_id:
        raise ValueError("chat_completion_model_id is not defined")

    text_embedding_model_id = os.environ.get("TEXT_EMBEDDING_MODEL_ID")
    if not chat_completion_model_id:
        raise ValueError("chat_completion_model_id is not defined")

    sleep_time = 1


