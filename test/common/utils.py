from typing import Dict, Any
import asyncio
import random
import string
import pytest

from test.common.logger import logger


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


def get_random_email():
    domain = ["163.com", "126.com", "yeah.net", "vip.163.com", "vip.126.com", "188.com", "vip.188.com", "qq.com",
              "gmail.com", "yahoo.com", "sina.com", "sina.cn", "sohu.com", "sogou.com", "outlook.com", "189.com",
              "wo.cn", "139.com", "ailiyun.com", "icloud.com", "tianya.cn", "renren.com", "tom.com"]
    username_length = random.randint(5, 10)
    username = ''.join(random.choices(string.ascii_lowercase, k=username_length))
    domain_name = random.choice(domain)
    email = username + "@" + domain_name
    return email


def get_password():
    return ''.join(random.choices(string.ascii_letters, k=7))+str(random.randint(0, 9))


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


async def mq_execute_create_collection(n, func,  *args, **kwargs):
    if n == 10:
        logger.info(func+"timeout")
        pytest.assume(False)
    else:
        from test.retrieval_service.collection import get_collection
        res = await get_collection(*args, **kwargs)
        if res.json()["data"]["status"] == "ready" and res.json()["data"]["num_records"] >= 0 and res.json()["data"]["num_chunks"] >= 0:
            return
        else:
            await asyncio.sleep(1)
            logger.info(f"collection status is {res.json()['data']['status']}")
            logger.info(f"collection num_records is {res.json()['data']['num_records']}")
            logger.info(f"collection num_chunks is {res.json()['data']['num_chunks']}")
            await mq_execute_create_collection(n+1, func, *args, **kwargs)


async def mq_execute_delete_collection(n, func,  *args, **kwargs):
    if n == 10:
        logger.info(func + "timeout")
        pytest.assume(False)
    else:
        from test.retrieval_service.collection import get_collection
        res = await get_collection(*args, **kwargs)
        if res.status_code == 404:
            logger.info(f"project[{args[0]}]collection[{args[1]}] is deleted")
            return
        else:
            await asyncio.sleep(1)
            await mq_execute_delete_collection(n+1, func, *args, **kwargs)


async def mq_execute_create_record(n, func, *args, **kwargs):
    if n == 10:
        logger.info(func + "timeout")
        pytest.assume(False)
    else:
        from test.retrieval_service.record import get_record
        res = await get_record(*args, **kwargs)
        if res.json()["data"]["status"] == "ready" and res.json()["data"]["num_chunks"] >= 0:
            logger.info(f"project[{args[0]}]collection[{args[1]}]record[{args[2]}] status is ready")
            return
        elif res.json()["data"]["status"] == "partial" and res.json()["data"]["num_chunks"] >= 0:
            logger.info(f"project[{args[0]}]collection[{args[1]}]record[{args[2]}] is partial")
            return
        else:
            await asyncio.sleep(1)
            logger.info(f"record status is {res.json()['data']['status']}")
            logger.info(f"record num_chunks is {res.json()['data']['num_chunks']}")
            await mq_execute_create_record(n + 1, func, *args, **kwargs)


async def mq_execute_delete_record(n, func, *args, **kwargs):
    if n == 10:
        logger.info(func + "timeout")
        pytest.assume(False)
    else:
        from test.retrieval_service.record import get_record
        res = await get_record(*args, **kwargs)
        if res.status_code == 404:
            logger.info(f"project[{args[0]}]collection[{args[1]}]record[{args[2]}] is deleted")
            return
        else:
            await asyncio.sleep(1)
            await mq_execute_delete_record(n + 1, func, *args, **kwargs)


async def mq_execute_delete_project(n, func, *args, **kwargs):
    if n == 10:
        logger.info(func + "timeout")
        pytest.assume(False)
    else:
        from test.retrieval_service.collection import list_collections
        collections_res = await list_collections(*args, **kwargs)
        if collections_res.status_code == 400:
            return
        else:
            await asyncio.sleep(1)
            await mq_execute_delete_project(n + 1, func, *args, **kwargs)


def get_random():
    return ''.join(random.choices(string.ascii_letters, k=7))+str(random.randint(0, 9))


def get_project_id(i: int):
    return (get_random() for j in range(i))


