class ManualLemmatizer:

    IRREGULAR = {
        "fui": "ir",
        "foi": "ir",
        "foram": "ir",
        "era": "ser",
        "eram": "ser",
        "sou": "ser",
        "é": "ser",
        "são": "ser",
    }

    def lemmatize(self, token: str) -> str:

        token = token.lower()

        if token in self.IRREGULAR:
            return self.IRREGULAR[token]

        if token.endswith("ando"):
            return token[:-4] + "ar"

        if token.endswith("endo"):
            return token[:-4] + "er"

        if token.endswith("indo"):
            return token[:-4] + "ir"

        return token