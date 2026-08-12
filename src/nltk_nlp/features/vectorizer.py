from .tfidf import TFIDF


class TFIDFVectorizer:

    def __init__(self):

        self.model = TFIDF()

    def fit(
        self,
        documents: list[list[str]],
    ):

        self.model.fit(
            documents
        )

        return self

    def transform(
        self,
        documents: list[list[str]],
    ):

        return [
            self.model.transform(
                document
            )
            for document in documents
        ]

    def fit_transform(
        self,
        documents: list[list[str]],
    ):

        return self.model.fit_transform(
            documents
        )

    @property
    def vocabulary(self):

        return self.model.vocabulary