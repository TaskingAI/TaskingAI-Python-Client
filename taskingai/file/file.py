from typing import Union

from taskingai.client.models import FileIdData, UploadFilePurpose

from .utils import FileType
from .api import upload_file_api, a_upload_file_api

__all__ = ["upload_file", "a_upload_file"]


def upload_file(
    file: FileType,
    purpose: Union[UploadFilePurpose, str] = UploadFilePurpose.RECORD_FILE,
) -> FileIdData:
    """
    Upload a file.

    :param file: The file bytes or file path.
    :param purpose: The purpose of the file.
    :return: The uploaded file info.
    """
    return upload_file_api(file=file, purpose=purpose)


async def a_upload_file(
    file: FileType,
    purpose: Union[UploadFilePurpose, str] = UploadFilePurpose.RECORD_FILE,
) -> FileIdData:
    """
    Upload a file.

    :param file: The file bytes or file path.
    :param purpose: The purpose of the file.
    :return: The uploaded file info.
    """

    return await a_upload_file_api(file=file, purpose=purpose)
