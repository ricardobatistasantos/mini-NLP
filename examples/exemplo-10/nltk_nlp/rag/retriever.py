from nltk_nlp.embeddings.base import (
    EmbeddingModel,
)

from nltk_nlp.vector_store.vector_store import (
    VectorStore,
)

from .models import RetrievedChunk


class Retriever:

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

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        filters: dict | None = None,
    ) -> list[RetrievedChunk]:

        query_vector = (
            self.embedding_model.embed(
                query
            )
        )

        results = (
            self.vector_store.search(
                query_vector=query_vector,
                top_k=top_k,
                filters=filters,
            )
        )

        return [
            RetrievedChunk(
                id=result.id,
                document_id=result.metadata.get(
                    "document_id",
                    "",
                ),
                text=result.text,
                score=result.score,
                position=result.metadata.get(
                    "position",
                    0,
                ),
                metadata=result.metadata,
            )
            for result in results
        ]