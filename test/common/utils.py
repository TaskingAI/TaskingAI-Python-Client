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
