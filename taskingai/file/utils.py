from io import IOBase
from typing import IO, Union

import aiofiles

from taskingai.client.models import FileIdData

__all__ = [
    "FileType",
    "get_file_response",
    "get_file_response_async",
    "extract_file",
    "extract_file_async",
]


FileType = Union[IO, str]


def get_file_response(response):
    response_json = response.json()
    data = response_json.get("data")
    if data:
        return FileIdData(**data)
    return response_json


async def get_file_response_async(response):
    response_json = await response.json()
    data = response_json.get("data")
    if data:
        return FileIdData(**data)
    return response_json


def extract_file(file: FileType):
    if isinstance(file, str):
        with open(file, "rb") as f:
            file_bytes = f.read()
            file_name = f.name
    elif isinstance(file, IOBase):
        file_bytes = file.read()
        file_name = file.name
    else:
        raise Exception("file type error")
    return file_bytes, file_name


async def extract_file_async(file: FileType):
    if isinstance(file, str):
        async with aiofiles.open(file, "rb") as f:
            file_bytes = await f.read()
            file_name = f.name
    elif isinstance(file, IOBase):
        file_bytes = file.read()
        file_name = file.name
    else:
        raise Exception("file type error")
    return file_bytes, file_name
