def manhattan_distance(
    vector_a: list[float],
    vector_b: list[float],
) -> float:

    if len(vector_a) != len(vector_b):
        raise ValueError(
            "Vectors must have the same dimension"
        )

    return sum(
        abs(a - b)
        for a, b in zip(
            vector_a,
            vector_b
        )
    )