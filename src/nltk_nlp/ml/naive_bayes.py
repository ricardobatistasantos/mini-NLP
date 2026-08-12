import math
from collections import Counter


class NaiveBayes:

    def __init__(self):
        self.classes = set()
        self.class_counts = Counter()
        self.word_counts = {}
        self.total_words = {}
        self.vocabulary = set()

    def fit(
        self,
        documents: list[list[str]],
        labels: list[str],
    ) -> None:

        for document, label in zip(documents, labels):

            self.classes.add(label)

            self.class_counts[label] += 1

            if label not in self.word_counts:
                self.word_counts[label] = Counter()

            for token in document:

                self.word_counts[label][token] += 1
                self.vocabulary.add(token)

                self.total_words[label] = (
                    self.total_words.get(label, 0) + 1
                )

    def predict(
        self,
        document: list[str],
    ) -> str:

        scores = {}

        total_documents = sum(
            self.class_counts.values()
        )

        for label in self.classes:

            score = math.log(
                self.class_counts[label]
                / total_documents
            )

            vocabulary_size = len(self.vocabulary)

            for token in document:

                word_count = (
                    self.word_counts[label][token]
                )

                total_words = self.total_words[label]

                probability = (
                    word_count + 1
                ) / (
                    total_words + vocabulary_size
                )

                score += math.log(probability)

            scores[label] = score

        return max(
            scores,
            key=scores.get,
        )