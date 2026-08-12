from collections import Counter


class BagOfWords:

    def vocabulary(self, documents: list[list[str]]) -> dict[str, int]:
        words = set()

        for document in documents:
            words.update(document)

        return {
            word: index
            for index, word in enumerate(sorted(words))
        }

    def transform(
        self,
        document: list[str],
        vocabulary: dict[str, int],
    ) -> list[int]:

        vector = [0] * len(vocabulary)

        counter = Counter(document)

        for word, count in counter.items():

            if word not in vocabulary:
                continue

            index = vocabulary[word]

            vector[index] = count

        return vector

    def fit_transform(
        self,
        documents: list[list[str]],
    ):

        vocabulary = self.vocabulary(
            documents
        )

        vectors = [
            self.transform(
                document,
                vocabulary
            )
            for document in documents
        ]

        return vocabulary, vectors