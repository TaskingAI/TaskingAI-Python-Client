from typing import Dict, Any
import random
import string
import pytest


class ResponseWrapper:
    def __init__(self, status: int, json_data: Dict):
        self.status_code = status
        self._json_data = json_data

    def json(self):
        return self._json_data


def list_to_dict(data: list):
    d = {}
    for i in data:
        if isinstance(i, dict):
            for k, v in i.items():
                d[k] = v
        else:
            d.update(i)
    return d


def assume(res, except_dict: Dict[str, Any]):
    pytest.assume(res.status_code == int(except_dict["except_http_code"]))
    pytest.assume(res.json()["status"] == except_dict["except_status"])


def assume_success(res, except_dict: Dict[str, Any]):
    assume(res, except_dict)
    pytest.assume(res.json()["data"]["status"] == except_dict["except_data_status"])


def assume_error(res, except_dict: Dict[str, Any]):
    assume(res, except_dict)
    pytest.assume(res.json()["error"]["code"] == except_dict["except_error_code"])


def assume_count(res, except_dict: Dict[str, Any]):
    assume(res, except_dict)
    pytest.assume(res.json()["total_count"] >= 0)
    pytest.assume(res.json()["fetched_count"] >= 0)
    pytest.assume(len(res.json()["data"]) == res.json()["fetched_count"])


def assume_assistant(res, assistant_dict: Dict[str, Any]):
    for key, value in assistant_dict.items():
        if key == "error":
            pass
        elif key == 'system_prompt_template' and isinstance(value, str):
            pytest.assume(res[key] == [assistant_dict[key]])
        elif key in ["memory", "tool", "retrievals"]:
            pass
        else:
            pytest.assume(res[key] == assistant_dict[key])


def assume_collection(res, collection_dict: Dict[str, Any]):
    for key, value in collection_dict.items():
        if key == "configs":
            for k, v in value.items():
                pytest.assume(res.json()["data"][key][k] == collection_dict[key][k])
        elif key == "error":
            pass
        else:
            pytest.assume(res.json()["data"][key] == collection_dict[key])


def assume_record(res, record_dict: Dict[str, Any]):
    for key, value in record_dict.items():
        if key == "type":
            pytest.assume(res.json()["data"][key] == record_dict[key])
        elif key == "error":
            pass
        elif key == "text":
            pytest.assume(res.json()["data"]["content"][key] == record_dict[key])


def assume_chunk(res, chunk_dict: Dict[str, Any]):
    for key, value in chunk_dict.items():
        if key == "error":
            pass
        else:
            pytest.assume(len(res.json()["data"]) == res.json()["fetched_count"] == chunk_dict["top_k"])


def get_random():
    return ''.join(random.choices(string.ascii_letters, k=7))+str(random.randint(0, 9))


def get_project_id(i: int):
    return (get_random() for j in range(i))


def assume_text_embedding_result(result: list):
    pytest.assume(len(result) > 0)
    pytest.assume(all(isinstance(value, float) for value in result))


def assume_collection_result(create_dict: dict, res_dict: dict):
    for key in create_dict:
        pytest.assume(res_dict[key] == create_dict[key])
    pytest.assume(res_dict["status"] == "ready")


def assume_record_result(create_record_data: dict, res_dict: dict):
    for key, value in create_record_data.items():
        if key in ["text_splitter"]:
            continue
        elif key in ["url"]:
            assert create_record_data[key] in res_dict.get("content")
        elif key == "file_id":
            assert create_record_data[key] in res_dict.get("content")
            assert int(res_dict.get("content").split('\"file_size\":')[-1].strip("}").strip()) > 0
        else:
            pytest.assume(res_dict[key] == create_record_data[key])

    pytest.assume(res_dict["status"] == "creating")


def assume_chunk_result(chunk_dict: dict, res: dict):
    for key, value in chunk_dict.items():
        pytest.assume(res[key] == chunk_dict[key])


def assume_query_chunk_result(query_text, chunk_dict: dict):
    pytest.assume(query_text in chunk_dict["content"])
    pytest.assume(isinstance(chunk_dict["score"], float))


def assume_assistant_result(assistant_dict: dict, res: dict):
    for key, value in assistant_dict.items():
        if key == 'system_prompt_template' and isinstance(value, str):
            pytest.assume(res[key] == [assistant_dict[key]])
        elif key in ['retrieval_configs']:
            continue
            # if isinstance(value, dict):
            #     pytest.assume(vars(res[key]) == assistant_dict[key])
            # else:
            #     pytest.assume(res[key] == assistant_dict[key])
        elif key in ["memory", "tools", "retrievals"]:
            continue
        else:
            pytest.assume(res[key] == assistant_dict[key])


def assume_chat_result(chat_dict: dict, res: dict):
    for key, value in chat_dict.items():
        pytest.assume(res[key] == chat_dict[key])


def assume_message_result(message_dict: dict, res: dict):
    for key, value in message_dict.items():
        pytest.assume(res[key] == message_dict[key])

