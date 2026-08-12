import re

from ..ids import generate_chunk_id
from ..models import (
    Document,
    DocumentChunk,
)

from .base import DocumentChunker


class RecursiveChunker(
    DocumentChunker
):

    def __init__(
        self,
        max_chars: int = 1000,
        overlap: int = 100,
    ):

        self.max_chars = max_chars
        self.overlap = overlap

    def chunk(
        self,
        document: Document,
    ) -> list[DocumentChunk]:

        sections = re.split(
            r"\n\s*\n",
            document.text,
        )

        chunks = []

        buffer = ""

        for section in sections:

            section = section.strip()

            if not section:
                continue

            if (
                len(buffer)
                + len(section)
                + 1
                <= self.max_chars
            ):

                buffer = (
                    f"{buffer}\n{section}"
                    if buffer
                    else section
                )

            else:

                if buffer:

                    chunks.append(
                        buffer.strip()
                    )

                buffer = section

        if buffer:

            chunks.append(
                buffer.strip()
            )

        return self._build_chunks(
            document,
            chunks,
        )

    def _build_chunks(
        self,
        document: Document,
        chunks: list[str],
    ) -> list[DocumentChunk]:

        result = []

        search_start = 0

        for position, text in enumerate(
            chunks
        ):

            start_offset = (
                document.text.find(
                    text,
                    search_start,
                )
            )

            if start_offset < 0:
                start_offset = 0

            end_offset = (
                start_offset
                + len(text)
            )

            chunk_id = (
                generate_chunk_id(
                    document.id,
                    position,
                )
            )

            result.append(
                DocumentChunk(
                    id=chunk_id,
                    document_id=document.id,
                    text=text,
                    position=position,
                    metadata={
                        **document.metadata,
                        "source": document.source,
                    },
                    start_offset=start_offset,
                    end_offset=end_offset,
                )
            )

            search_start = end_offset

        return result