import hashlib
import math

from .base import EmbeddingModel


class HashEmbedding(EmbeddingModel):

    def __init__(
        self,
        dimensions: int = 128,
    ):

        if dimensions <= 0:
            raise ValueError(
                "dimensions must be greater than zero"
            )

        self.dimensions = dimensions

    def _hash_token(
        self,
        token: str,
    ) -> int:

        digest = hashlib.sha256(
            token.encode("utf-8")
        ).digest()

        return int.from_bytes(
            digest[:8],
            byteorder="big",
        )

    def embed(
        self,
        text: str,
    ) -> list[float]:

        tokens = text.lower().split()

        vector = [
            0.0
            for _ in range(self.dimensions)
        ]

        if not tokens:
            return vector

        for token in tokens:

            index = (
                self._hash_token(token)
                % self.dimensions
            )

            vector[index] += 1.0

        return self._normalize(
            vector
        )

    def _normalize(
        self,
        vector: list[float],
    ) -> list[float]:

        magnitude = math.sqrt(
            sum(
                value ** 2
                for value in vector
            )
        )

        if magnitude == 0:
            return vector

        return [
            value / magnitude
            for value in vector
        ]