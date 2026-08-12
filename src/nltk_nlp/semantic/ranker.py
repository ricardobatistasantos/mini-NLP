from mini_nlp.embeddings.similarity import (
    cosine_similarity,
)


class SemanticRanker:

    def rank(
        self,
        query_vector: list[float],
        records,
    ):

        results = []

        for record in records:

            score = cosine_similarity(
                query_vector,
                record.vector,
            )

            results.append({
                "id": record.id,
                "text": record.text,
                "score": score,
                "metadata": record.metadata,
            })

        results.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        return results