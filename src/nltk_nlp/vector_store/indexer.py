from mini_nlp.embeddings.base import (
    EmbeddingModel,
)

from .models import VectorRecord
from .vector_store import VectorStore


class VectorIndexer:

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

    def index(
        self,
        id: str,
        text: str,
        metadata: dict | None = None,
    ) -> VectorRecord:

        vector = (
            self.embedding_model.embed(
                text
            )
        )

        record = VectorRecord(
            id=id,
            vector=vector,
            text=text,
            metadata=metadata or {},
        )

        self.vector_store.add(
            record
        )

        return record

    def index_many(
        self,
        documents: list[dict],
    ):

        records = []

        for document in documents:

            record = VectorRecord(
                id=document["id"],
                vector=(
                    self.embedding_model
                    .embed(
                        document["text"]
                    )
                ),
                text=document["text"],
                metadata=document.get(
                    "metadata",
                    {},
                ),
            )

            records.append(
                record
            )

        self.vector_store.add_many(
            records
        )

        return records