from .cosine import cosine_similarity
from .euclidean import euclidean_distance
from .manhattan import manhattan_distance


class Similarity:

    @staticmethod
    def cosine(
        vector_a: list[float],
        vector_b: list[float],
    ) -> float:

        return cosine_similarity(
            vector_a,
            vector_b
        )

    @staticmethod
    def euclidean(
        vector_a: list[float],
        vector_b: list[float],
    ) -> float:

        return euclidean_distance(
            vector_a,
            vector_b
        )

    @staticmethod
    def manhattan(
        vector_a: list[float],
        vector_b: list[float],
    ) -> float:

        return manhattan_distance(
            vector_a,
            vector_b
        )