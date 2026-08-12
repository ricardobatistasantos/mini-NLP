from .deduplicator import (
    Deduplicator,
)

from .models import (
    RetrievalResult,
)

from .reranker import (
    KeywordReranker,
)

from .threshold import (
    ScoreThreshold,
)


class RetrievalPipeline:

    def __init__(
        self,
        hybrid_retriever,
        reranker: KeywordReranker | None = None,
        threshold: ScoreThreshold | None = None,
        deduplicator: Deduplicator | None = None,
    ):

        self.hybrid_retriever = (
            hybrid_retriever
        )

        self.reranker = (
            reranker
            or KeywordReranker()
        )

        self.threshold = (
            threshold
            or ScoreThreshold(
                threshold=0.0
            )
        )

        self.deduplicator = (
            deduplicator
            or Deduplicator()
        )

    def search(
        self,
        query: str,
        top_k: int = 5,
        candidate_k: int = 20,
        filters: dict | None = None,
    ) -> list[RetrievalResult]:

        candidates = (
            self.hybrid_retriever.search(
                query=query,
                top_k=candidate_k,
                filters=filters,
            )
        )

        candidates = (
            self.deduplicator.deduplicate(
                candidates
            )
        )

        candidates = (
            self.reranker.rerank(
                query=query,
                results=candidates,
            )
        )

        candidates = (
            self.threshold.apply(
                candidates
            )
        )

        return candidates[:top_k]