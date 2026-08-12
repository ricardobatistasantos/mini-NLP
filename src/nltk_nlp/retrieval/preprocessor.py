import re


class RetrievalPreprocessor:

    def process(
        self,
        text: str,
    ) -> list[str]:

        text = text.lower()

        text = re.sub(
            r"[^\w\s]",
            " ",
            text,
        )

        return [
            token
            for token in text.split()
            if token
        ]