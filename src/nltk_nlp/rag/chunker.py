from .models import (
    Document,
    Chunk,
)


class TextChunker:

    def __init__(
        self,
        chunk_size: int = 100,
        overlap: int = 20,
    ):

        if chunk_size <= 0:
            raise ValueError(
                "chunk_size must be greater than zero"
            )

        if overlap < 0:
            raise ValueError(
                "overlap cannot be negative"
            )

        if overlap >= chunk_size:
            raise ValueError(
                "overlap must be smaller than chunk_size"
            )

        self.chunk_size = chunk_size
        self.overlap = overlap

    def split(
        self,
        document: Document,
    ) -> list[Chunk]:

        words = document.text.split()

        if not words:
            return []

        chunks = []

        start = 0
        position = 0

        step = (
            self.chunk_size
            - self.overlap
        )

        while start < len(words):

            end = start + self.chunk_size

            chunk_words = words[
                start:end
            ]

            text = " ".join(
                chunk_words
            )

            chunk = Chunk(
                id=(
                    f"{document.id}"
                    f"-chunk-{position}"
                ),
                document_id=document.id,
                text=text,
                position=position,
                metadata={
                    **document.metadata,
                    "chunk_position": position,
                },
            )

            chunks.append(chunk)

            start += step
            position += 1

        return chunks