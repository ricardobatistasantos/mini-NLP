from mini_nlp.embeddings.base import (
    EmbeddingModel,
)

from .vector_store import VectorStore


class VectorSearch:

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
    ):

        query_vector = (
            self.embedding_model.embed(
                query
            )
        )

        return self.vector_store.search(
            query_vector=query_vector,
            top_k=top_k,
            filters=filters,
        )