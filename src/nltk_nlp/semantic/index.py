from mini_nlp.embeddings.base import (
    EmbeddingModel,
)

from mini_nlp.embeddings.store import (
    EmbeddingRecord,
)

from .document import SemanticDocument


class SemanticIndex:

    def __init__(
        self,
        embedding_model: EmbeddingModel,
    ):

        self.embedding_model = (
            embedding_model
        )

        self.records: list[
            EmbeddingRecord
        ] = []

    def add(
        self,
        document: SemanticDocument,
    ):

        vector = (
            self.embedding_model.embed(
                document.text
            )
        )

        record = EmbeddingRecord(
            id=document.id,
            text=document.text,
            vector=vector,
            metadata=document.metadata,
        )

        self.records.append(
            record
        )

    def add_many(
        self,
        documents: list[
            SemanticDocument
        ],
    ):

        for document in documents:
            self.add(document)

    def get_all(self):

        return self.records