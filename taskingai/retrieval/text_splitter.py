from taskingai.client.models import TextSplitter, TextSplitterType

__all__ = [
    "TextSplitter",
    "TextSplitterType",
    "TokenTextSplitter",
]


class TokenTextSplitter(TextSplitter):
    def __init__(self, chunk_size: int, chunk_overlap: int):
        super().__init__(
            type=TextSplitterType.TOKEN,
            chunk_size=chunk_size,
            chunk_overlap=chunk_overlap,
        )
