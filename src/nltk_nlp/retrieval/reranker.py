from collections import Counter

from .lexical import LexicalTokenizer
from .models import RetrievalResult


class KeywordReranker:

    def __init__(self):

        self.tokenizer = (
            LexicalTokenizer()
        )

    def score(
        self,
        query: str,
        text: str,
    ) -> float:

        query_tokens = set(
            self.tokenizer.tokenize(
                query
            )
        )

        document_tokens = (
            self.tokenizer.tokenize(
                text
            )
        )

        if not query_tokens:
            return 0.0

        frequencies = Counter(
            document_tokens
        )

        matched = 0

        for token in query_tokens:

            if frequencies[token] > 0:
                matched += 1

        return (
            matched
            / len(query_tokens)
        )

    def rerank(
        self,
        query: str,
        results: list[RetrievalResult],
    ) -> list[RetrievalResult]:

        for result in results:

            result.rerank_score = (
                self.score(
                    query=query,
                    text=result.text,
                )
            )

        results.sort(
            key=lambda result: (
                result.rerank_score,
                result.score,
            ),
            reverse=True,
        )

        return results