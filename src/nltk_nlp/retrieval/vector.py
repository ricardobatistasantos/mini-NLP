from mini_nlp.embeddings.base import (
    EmbeddingModel,
)

from mini_nlp.vector_store.vector_store import (
    VectorStore,
)

from .models import RetrievalResult


class VectorRetriever:

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

    def search(
        self,
        query: str,
        top_k: int = 5,
        filters: dict | None = None,
    ) -> list[RetrievalResult]:

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
            RetrievalResult(
                id=result.id,
                text=result.text,
                score=result.score,
                vector_score=result.score,
                metadata=result.metadata,
            )
            for result in results
        ]