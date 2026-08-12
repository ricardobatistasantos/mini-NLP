import re


class ManualNER:

    MONEY_PATTERN = re.compile(
        r"R\$\s?\d+(?:\.\d{3})*(?:,\d{2})?"
    )

    def extract(
        self,
        text: str,
    ) -> list[dict]:

        entities = []

        # Dinheiro
        for match in self.MONEY_PATTERN.finditer(text):

            entities.append({
                "text": match.group(),
                "type": "MONEY",
                "start": match.start(),
                "end": match.end(),
            })

        return entities