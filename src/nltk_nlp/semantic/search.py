from mini_nlp.embeddings.base import (
    EmbeddingModel,
)

from .index import SemanticIndex
from .ranker import SemanticRanker


class SemanticSearch:

    def __init__(
        self,
        index: SemanticIndex,
        embedding_model: EmbeddingModel,
    ):

        self.index = index

        self.embedding_model = (
            embedding_model
        )

        self.ranker = SemanticRanker()

    def search(
        self,
        query: str,
        top_k: int = 5,
    ):

        query_vector = (
            self.embedding_model.embed(
                query
            )
        )

        results = self.ranker.rank(
            query_vector,
            self.index.get_all(),
        )

        return results[:top_k]