class NGramGenerator:

    def generate(
        self,
        tokens: list[str],
        n: int,
    ) -> list[tuple[str, ...]]:

        if n <= 0:
            raise ValueError("n deve ser maior que zero")

        if n > len(tokens):
            return []

        result = []

        for index in range(len(tokens) - n + 1):

            gram = tuple(
                tokens[index:index + n]
            )

            result.append(gram)

        return result

    def unigram(
        self,
        tokens: list[str],
    ) -> list[tuple[str]]:

        return self.generate(tokens, 1)

    def bigram(
        self,
        tokens: list[str],
    ) -> list[tuple[str, str]]:

        return self.generate(tokens, 2)

    def trigram(
        self,
        tokens: list[str],
    ) -> list[tuple[str, str, str]]:

        return self.generate(tokens, 3)