from typing import Union, Dict, BinaryIO
import os

from taskingai.client.models import FileIdData, UploadFilePurpose, UploadFileResponse
from taskingai.client.utils import get_api_client


__all__ = ["upload_file", "a_upload_file"]


def __prepare_files(file: BinaryIO, purpose: Union[UploadFilePurpose, str]) -> Dict:
    """
    Prepare file data for uploading.

    :param file: A file object opened in binary mode.
    :param purpose: The purpose of the upload, either as a string or UploadFilePurpose enum.
    :return: A dictionary formatted for the API call.
    """
    if not hasattr(file, "read"):
        raise ValueError("Unsupported file type: Expected a file-like object with a read method")

    try:
        file_bytes = file.read()
    except Exception as e:
        raise ValueError(f"Error reading file: {e}")

    file_name = os.path.basename(file.name)

    if isinstance(purpose, str):
        try:
            purpose = UploadFilePurpose(purpose)
        except ValueError:
            raise ValueError(f"Invalid purpose value: {purpose}")

    if not isinstance(purpose, UploadFilePurpose):
        raise ValueError("Purpose must be an instance of UploadFilePurpose or a valid string")

    return {
        "file": (file_name, file_bytes, "application/octet-stream"),
        "purpose": (None, str(purpose.value)),
    }


def upload_file(
    file: BinaryIO,
    purpose: Union[UploadFilePurpose, str] = UploadFilePurpose.RECORD_FILE,
) -> FileIdData:
    """
    Upload a file.

    :param file: The file to upload, opened as a binary stream.
    :param purpose: The intended purpose of the uploaded file, influencing handling on the server side.
    :return: The response data containing information about the uploaded file.
    """
    sync_api_client = get_api_client(async_client=False)

    files = __prepare_files(file, purpose)
    header_params = {"Accept": sync_api_client.select_header_accept(["application/json"])}

    # execute the request
    response: UploadFileResponse = sync_api_client.call_api(
        resource_path="/v1/files",
        method="POST",
        header_params=header_params,
        files=files,
        response_type=UploadFileResponse,
        _return_http_data_only=True,
        _preload_content=True,
        collection_formats={},
    )
    return response.data


async def a_upload_file(
    file: BinaryIO,
    purpose: Union[UploadFilePurpose, str] = UploadFilePurpose.RECORD_FILE,
) -> FileIdData:
    """
    Upload a file.

    :param file: The file to upload, opened as a binary stream.
    :param purpose: The intended purpose of the uploaded file, influencing handling on the server side.
    :return: The response data containing information about the uploaded file.
    """
    async_api_client = get_api_client(async_client=True)

    files = __prepare_files(file, purpose)
    header_params = {"Accept": async_api_client.select_header_accept(["application/json"])}

    # execute the request
    response: UploadFileResponse = await async_api_client.call_api(
        resource_path="/v1/files",
        method="POST",
        header_params=header_params,
        files=files,
        response_type=UploadFileResponse,
        _return_http_data_only=True,
        _preload_content=True,
        collection_formats={},
    )
    return response.data
