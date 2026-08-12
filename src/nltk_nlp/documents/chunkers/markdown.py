import re

from ..ids import generate_chunk_id
from ..models import (
    Document,
    DocumentChunk,
)

from .base import DocumentChunker


class MarkdownChunker(
    DocumentChunker
):

    def chunk(
        self,
        document: Document,
    ) -> list[DocumentChunk]:

        lines = document.text.splitlines()

        sections = []

        current_heading = None
        current_content = []

        for line in lines:

            if re.match(
                r"^#{1,6}\s+",
                line,
            ):

                if current_content:

                    sections.append(
                        (
                            current_heading,
                            "\n".join(
                                current_content
                            ),
                        )
                    )

                current_heading = line.strip()

                current_content = []

            else:

                current_content.append(
                    line
                )

        if current_content:

            sections.append(
                (
                    current_heading,
                    "\n".join(
                        current_content
                    ),
                )
            )

        chunks = []

        for position, (
            heading,
            content,
        ) in enumerate(sections):

            content = content.strip()

            if not content:
                continue

            text = (
                f"{heading}\n{content}"
                if heading
                else content
            )

            chunks.append(
                DocumentChunk(
                    id=generate_chunk_id(
                        document.id,
                        position,
                    ),
                    document_id=document.id,
                    text=text,
                    position=position,
                    metadata={
                        **document.metadata,
                        "heading": heading,
                        "source": document.source,
                    },
                )
            )

        return chunks