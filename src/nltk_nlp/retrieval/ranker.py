from ..similarity.cosine import cosine_similarity


class Ranker:

    def rank(
        self,
        query_vector: list[float],
        document_vectors: list[list[float]],
        documents,
    ):

        results = []

        for document, vector in zip(
            documents,
            document_vectors
        ):

            score = cosine_similarity(
                query_vector,
                vector
            )

            results.append({
                "document": document,
                "score": score,
            })

        results.sort(
            key=lambda item: item["score"],
            reverse=True,
        )

        return results