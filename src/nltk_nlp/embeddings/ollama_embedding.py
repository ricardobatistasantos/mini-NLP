import requests

from .base import EmbeddingModel


class OllamaEmbedding(EmbeddingModel):

    def __init__(
        self,
        model: str,
        base_url: str = "http://localhost:11434",
    ):

        self.model = model

        self.base_url = base_url.rstrip("/")

    def embed(
        self,
        text: str,
    ) -> list[float]:

        response = requests.post(
            f"{self.base_url}/api/embed",
            json={
                "model": self.model,
                "input": text,
            },
            timeout=60,
        )

        response.raise_for_status()

        data = response.json()

        embeddings = data.get(
            "embeddings"
        )

        if not embeddings:
            raise RuntimeError(
                "Ollama did not return embeddings"
            )

        return embeddings[0]