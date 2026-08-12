from ..ids import generate_chunk_id
from ..models import (
    Document,
    DocumentChunk,
)

from .base import DocumentChunker


class ParagraphChunker(
    DocumentChunker
):

    def chunk(
        self,
        document: Document,
    ) -> list[DocumentChunk]:

        paragraphs = [
            paragraph.strip()
            for paragraph in document.text.split(
                "\n\n"
            )
            if paragraph.strip()
        ]

        chunks = []

        search_start = 0

        for position, paragraph in enumerate(
            paragraphs
        ):

            start_offset = (
                document.text.find(
                    paragraph,
                    search_start,
                )
            )

            end_offset = (
                start_offset
                + len(paragraph)
            )

            chunk_id = (
                generate_chunk_id(
                    document.id,
                    position,
                )
            )

            chunks.append(
                DocumentChunk(
                    id=chunk_id,
                    document_id=document.id,
                    text=paragraph,
                    position=position,
                    metadata={
                        **document.metadata,
                        "source": document.source,
                        "document_version": (
                            document.version
                        ),
                    },
                    start_offset=start_offset,
                    end_offset=end_offset,
                )
            )

            search_start = end_offset

        return chunks