from mini_nlp.embeddings.base import (
    EmbeddingModel,
)

from mini_nlp.vector_store.models import (
    VectorRecord,
)

from mini_nlp.vector_store.vector_store import (
    VectorStore,
)

from .models import Chunk


class RAGIndexer:

    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_store: VectorStore,
    ):

        self.embedding_model = (
            embedding_model
        )

        self.vector_store = (
            vector_store
        )

    def index_chunk(
        self,
        chunk: Chunk,
    ) -> VectorRecord:

        vector = (
            self.embedding_model.embed(
                chunk.text
            )
        )

        record = VectorRecord(
            id=chunk.id,
            vector=vector,
            text=chunk.text,
            metadata={
                **chunk.metadata,
                "document_id": chunk.document_id,
                "position": chunk.position,
            },
        )

        self.vector_store.add(
            record
        )

        return record

    def index_chunks(
        self,
        chunks: list[Chunk],
    ):

        records = []

        for chunk in chunks:

            records.append(
                self.index_chunk(chunk)
            )

        return records