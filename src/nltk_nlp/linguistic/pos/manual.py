class ManualPOSTagger:

    VERBS = {
        "sou",
        "é",
        "são",
        "estou",
        "está",
        "estão",
        "quero",
        "quer",
        "comprar",
        "compro",
        "comprou",
        "pagar",
        "pagou",
        "estudar",
        "estuda",
    }

    ARTICLES = {
        "o",
        "a",
        "os",
        "as",
        "um",
        "uma",
        "uns",
        "umas",
    }

    PRONOUNS = {
        "eu",
        "tu",
        "ele",
        "ela",
        "nós",
        "vocês",
        "eles",
        "elas",
    }

    def tag(
        self,
        tokens: list[str],
    ) -> list[tuple[str, str]]:

        result = []

        for token in tokens:

            word = token.lower()

            if word in self.VERBS:
                tag = "VERB"

            elif word in self.ARTICLES:
                tag = "DET"

            elif word in self.PRONOUNS:
                tag = "PRON"

            elif word[0].isupper():
                tag = "PROPN"

            else:
                tag = "NOUN"

            result.append((token, tag))

        return result