from .models import RetrievalResult


class Deduplicator:

    def deduplicate(
        self,
        results: list[RetrievalResult],
    ) -> list[RetrievalResult]:

        seen = set()

        unique = []

        for result in results:

            if result.id in seen:
                continue

            seen.add(
                result.id
            )

            unique.append(
                result
            )

        return unique