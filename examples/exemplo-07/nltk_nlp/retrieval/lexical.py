import re


class LexicalTokenizer:

    def tokenize(
        self,
        text: str,
    ) -> list[str]:

        text = text.lower()

        tokens = re.findall(
            r"\b\w+\b",
            text,
            flags=re.UNICODE,
        )

        return tokens