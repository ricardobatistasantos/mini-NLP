import math


def euclidean_distance(
    vector_a: list[float],
    vector_b: list[float],
) -> float:

    if len(vector_a) != len(vector_b):
        raise ValueError(
            "Vectors must have the same dimension"
        )

    return math.sqrt(
        sum(
            (a - b) ** 2
            for a, b in zip(
                vector_a,
                vector_b
            )
        )
    )