from collections import defaultdict

from .models import RetrievalResult


class ScoreNormalizer:

    @staticmethod
    def min_max(
        results: list[RetrievalResult],
    ) -> list[RetrievalResult]:

        if not results:
            return results

        scores = [
            result.score
            for result in results
        ]

        minimum = min(scores)
        maximum = max(scores)

        if maximum == minimum:

            for result in results:
                result.score = 1.0

            return results

        for result in results:

            result.score = (
                result.score - minimum
            ) / (
                maximum - minimum
            )

        return results


class ReciprocalRankFusion:

    def __init__(
        self,
        k: int = 60,
    ):

        self.k = k

    def fuse(
        self,
        result_lists: list[
            list[RetrievalResult]
        ],
    ) -> list[RetrievalResult]:

        scores = defaultdict(float)

        documents = {}

        for result_list in result_lists:

            for rank, result in enumerate(
                result_list,
                start=1,
            ):

                scores[result.id] += (
                    1
                    / (
                        self.k
                        + rank
                    )
                )

                documents[
                    result.id
                ] = result

        results = []

        for document_id, score in (
            scores.items()
        ):

            result = documents[
                document_id
            ]

            result.score = score

            results.append(
                result
            )

        results.sort(
            key=lambda result: result.score,
            reverse=True,
        )

        return results