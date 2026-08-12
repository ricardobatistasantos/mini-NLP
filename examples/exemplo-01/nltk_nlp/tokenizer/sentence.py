import re

class SentenceTokenizer:

    ENDINGS = ".!?"

    def tokenize(self, text: str) -> list[str]:
        sentences = []

        current = []

        for char in text:

            current.append(char)

            if char in self.ENDINGS:

                sentence = "".join(current).strip()

                if sentence:
                    sentences.append(sentence)

                current = []

        remaining = "".join(current).strip()

        if remaining:
            sentences.append(remaining)

        return sentences