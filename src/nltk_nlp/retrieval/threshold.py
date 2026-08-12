from .models import RetrievalResult


class ScoreThreshold:

    def __init__(
        self,
        threshold: float = 0.0,
    ):

        self.threshold = threshold

    def apply(
        self,
        results: list[RetrievalResult],
    ) -> list[RetrievalResult]:

        return [
            result
            for result in results
            if result.score >= self.threshold
        ]