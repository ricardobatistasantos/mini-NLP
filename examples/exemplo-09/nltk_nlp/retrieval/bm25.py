import math
from collections import Counter

from .lexical import LexicalTokenizer
from .models import (
    RetrievalDocument,
    RetrievalResult,
)


class BM25:

    def __init__(
        self,
        documents: list[RetrievalDocument],
        k1: float = 1.5,
        b: float = 0.75,
    ):

        self.documents = documents

        self.k1 = k1
        self.b = b

        self.tokenizer = (
            LexicalTokenizer()
        )

        self.tokenized_documents = [
            self.tokenizer.tokenize(
                document.text
            )
            for document in documents
        ]

        self.document_lengths = [
            len(tokens)
            for tokens in self.tokenized_documents
        ]

        self.avg_document_length = (
            sum(self.document_lengths)
            / len(self.document_lengths)
            if self.document_lengths
            else 0
        )

        self.document_frequency = (
            self._calculate_document_frequency()
        )

    def _calculate_document_frequency(
        self,
    ) -> dict[str, int]:

        frequencies = {}

        for tokens in self.tokenized_documents:

            unique_tokens = set(tokens)

            for token in unique_tokens:

                frequencies[token] = (
                    frequencies.get(
                        token,
                        0,
                    )
                    + 1
                )

        return frequencies

    def _idf(
        self,
        token: str,
    ) -> float:

        total_documents = len(
            self.documents
        )

        document_frequency = (
            self.document_frequency.get(
                token,
                0,
            )
        )

        if document_frequency == 0:
            return 0.0

        return math.log(
            1
            + (
                total_documents
                - document_frequency
                + 0.5
            )
            / (
                document_frequency
                + 0.5
            )
        )

    def search(
        self,
        query: str,
        top_k: int = 5,
    ) -> list[RetrievalResult]:

        query_tokens = (
            self.tokenizer.tokenize(
                query
            )
        )

        results = []

        for index, document in enumerate(
            self.documents
        ):

            document_tokens = (
                self.tokenized_documents[
                    index
                ]
            )

            term_frequency = Counter(
                document_tokens
            )

            document_length = (
                self.document_lengths[
                    index
                ]
            )

            score = 0.0

            for token in query_tokens:

                if token not in term_frequency:
                    continue

                tf = term_frequency[token]

                idf = self._idf(token)

                numerator = (
                    tf
                    * (self.k1 + 1)
                )

                denominator = (
                    tf
                    + self.k1
                    * (
                        1
                        - self.b
                        + self.b
                        * (
                            document_length
                            / self.avg_document_length
                        )
                    )
                )

                score += (
                    idf
                    * numerator
                    / denominator
                )

            results.append(
                RetrievalResult(
                    id=document.id,
                    text=document.text,
                    score=score,
                    lexical_score=score,
                    metadata=document.metadata,
                )
            )

        results.sort(
            key=lambda item: item.score,
            reverse=True,
        )

        return results[:top_k]