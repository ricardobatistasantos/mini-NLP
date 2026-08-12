from .bm25 import BM25
from .fusion import ReciprocalRankFusion
from .models import (
    RetrievalDocument,
    RetrievalResult,
)
from .vector import VectorRetriever


class HybridRetriever:

    def __init__(
        self,
        lexical_retriever: BM25,
        vector_retriever: VectorRetriever,
        fusion: ReciprocalRankFusion | None = None,
    ):

        self.lexical_retriever = (
            lexical_retriever
        )

        self.vector_retriever = (
            vector_retriever
        )

        self.fusion = (
            fusion
            or ReciprocalRankFusion()
        )

    def search(
        self,
        query: str,
        top_k: int = 5,
        filters: dict | None = None,
    ) -> list[RetrievalResult]:

        lexical_results = (
            self.lexical_retriever.search(
                query=query,
                top_k=top_k,
            )
        )

        vector_results = (
            self.vector_retriever.search(
                query=query,
                top_k=top_k,
                filters=filters,
            )
        )

        return self.fusion.fuse(
            [
                lexical_results,
                vector_results,
            ]
        )[:top_k]