from collections import Counter


class TermFrequency:

    def calculate(
        self,
        document: list[str],
    ) -> dict[str, float]:

        if not document:
            return {}

        counter = Counter(document)

        total = len(document)

        return {
            word: count / total
            for word, count in counter.items()
        }

    def calculate_for_term(
        self,
        term: str,
        document: list[str],
    ) -> float:

        if not document:
            return 0.0

        count = document.count(term)

        return count / len(document)