import requests

from .generator import Generator


class OllamaGenerator(Generator):

    def __init__(
        self,
        model: str,
        base_url: str = "http://localhost:11434",
    ):

        self.model = model

        self.base_url = (
            base_url.rstrip("/")
        )

    def generate(
        self,
        prompt: str,
    ) -> str:

        response = requests.post(
            f"{self.base_url}/api/generate",
            json={
                "model": self.model,
                "prompt": prompt,
                "stream": False,
            },
            timeout=120,
        )

        response.raise_for_status()

        data = response.json()

        return data.get(
            "response",
            "",
        )