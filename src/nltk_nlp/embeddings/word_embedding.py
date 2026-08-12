class WordEmbedding:

    def __init__(
        self,
        vectors: dict[str, list[float]],
    ):
        self.vectors = vectors

    def get(
        self,
        word: str,
    ) -> list[float] | None:

        return self.vectors.get(
            word.lower()
        )