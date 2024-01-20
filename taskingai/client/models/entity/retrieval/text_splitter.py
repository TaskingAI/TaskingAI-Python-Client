from enum import Enum
from .._base import TaskingaiBaseModel
from pydantic import Field, model_validator
from typing import Optional, Dict, Any

__all__ = [
    "TextSplitter",
    "TextSplitterType",
    "TokenTextSplitter",
    "build_text_splitter",
]


class TextSplitterType(str, Enum):
    """TextSplitterType enum."""

    TOKEN = "token"


class TextSplitter(TaskingaiBaseModel):
    type: TextSplitterType = Field(...)


class TokenTextSplitter(TextSplitter):
    type: TextSplitterType = Field(TextSplitterType.TOKEN, Literal=TextSplitterType.TOKEN)
    chunk_size: int = Field(...)
    chunk_overlap: int = Field(...)

    # check chunk_overlap <= chunk_size/2
    @model_validator(mode="after")
    def validate_chunk_overlap(cls, data: Any):
        if data.chunk_overlap > data.chunk_size / 2:
            raise ValueError("chunk_overlap must be less than or equal to chunk_size/2")
        return data


def build_text_splitter(data: Dict) -> Optional[TextSplitter]:
    if not isinstance(data, Dict):
        raise ValueError("Text splitter input data must be a valid dictionary")

    splitter_type = data.get("type")
    if splitter_type is None:
        return None

    # Depending on the type of splitter, initialize the appropriate splitter instance
    if splitter_type == TextSplitterType.TOKEN.value:
        chunk_size = data.get("chunk_size")
        chunk_overlap = data.get("chunk_overlap")
        return TokenTextSplitter(chunk_size=chunk_size, chunk_overlap=chunk_overlap)

    else:
        # If the splitter_type is unknown, return None
        return None
