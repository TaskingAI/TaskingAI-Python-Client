import aiohttp
from typing import List, Dict
from test.common.utils import ResponseWrapper
from test.config import Config

AUTH_BASE_URL = Config.SPACE_SERVICE_URL + "/v1/auth"


async def login(data: Dict):
    # data = {email: str, password: str}
    async with aiohttp.ClientSession() as session:
        response = await session.post(AUTH_BASE_URL + "/login", json=data)
        return ResponseWrapper(response.status, await response.json())

BASE_URL = Config.PROJECT_SERVICE_URL


# For GET /{space_id}/projects/list
async def list_projects(token: str, space_id: str, data: Dict):
    # data = {"offset": int, "limit": int}
    headers = {"Authorization": "Bearer " + token}
    async with aiohttp.ClientSession(headers=headers) as session:
        request_url = f"{BASE_URL}/v1/{space_id}/projects/list"
        response = await session.get(request_url, params=data)
        return ResponseWrapper(response.status, await response.json())