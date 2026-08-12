from mini_nlp.documents.models import (
    Document,
)

from mini_nlp.documents.chunkers.base import (
    DocumentChunker,
)

from mini_nlp.embeddings.base import (
    EmbeddingModel,
)

from mini_nlp.vector_store.models import (
    VectorRecord,
)

from mini_nlp.vector_store.vector_store import (
    VectorStore,
)


class DocumentProcessor:

    def __init__(
        self,
        chunker: DocumentChunker,
        embedding_model: EmbeddingModel,
        vector_store: VectorStore,
    ):

        self.chunker = chunker

        self.embedding_model = (
            embedding_model
        )

        self.vector_store = (
            vector_store
        )

    def process(
        self,
        document: Document,
    ):

        chunks = self.chunker.chunk(
            document
        )

        records = []

        for chunk in chunks:

            vector = (
                self.embedding_model.embed(
                    chunk.text
                )
            )

            records.append(
                VectorRecord(
                    id=chunk.id,
                    vector=vector,
                    text=chunk.text,
                    metadata={
                        **chunk.metadata,
                        "document_id": (
                            document.id
                        ),
                        "checksum": (
                            document.checksum
                        ),
                        "chunk_position": (
                            chunk.position
                        ),
                    },
                )
            )

        self.vector_store.add_many(
            records
        )

        return chunks