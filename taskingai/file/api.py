from typing import Union

import aiohttp
import requests

from taskingai.client.models import UploadFilePurpose

from .utils import (
    FileType,
    extract_file,
    extract_file_async,
    get_file_response,
    get_file_response_async,
)

__all__ = ["upload_file_api", "a_upload_file_api"]


def upload_file_api(
    file: FileType,
    purpose: Union[UploadFilePurpose, str],
    **kwargs,
):
    from ..config import Config
    _url = f"{Config.HOST}/v1/files"
    _header = {"Accept": "application/json", "Authorization": f"Bearer {Config.API_KEY}"}
    _content_type = "application/octet-stream"

    file_bytes, file_name = extract_file(file)

    purpose = purpose if isinstance(purpose, UploadFilePurpose) else UploadFilePurpose(purpose)

    files = {"file": (file_name, file_bytes, _content_type)}
    data = {"purpose": purpose.value}

    response = requests.post(_url, headers=_header, files=files, data=data, **kwargs)
    return get_file_response(response)


async def a_upload_file_api(
    file: FileType,
    purpose: Union[UploadFilePurpose, str],
    **kwargs,
):
    from ..config import Config
    _url = f"{Config.HOST}/v1/files"
    _header = {"Accept": "application/json", "Authorization": f"Bearer {Config.API_KEY}"}
    _content_type = "application/octet-stream"

    file_bytes, file_name = await extract_file_async(file)

    purpose = purpose if isinstance(purpose, UploadFilePurpose) else UploadFilePurpose(purpose)

    data = aiohttp.FormData()
    data.add_field("file", file_bytes, filename=file_name, content_type=_content_type)
    data.add_field("purpose", purpose)
    async with aiohttp.ClientSession(headers=_header) as session, session.post(_url, data=data, **kwargs) as response:
        return await get_file_response_async(response)
