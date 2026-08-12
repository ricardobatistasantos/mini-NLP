from .tf import TermFrequency
from .idf import InverseDocumentFrequency


class TFIDF:

    def __init__(self):

        self.tf = TermFrequency()
        self.idf = InverseDocumentFrequency()

    def fit(
        self,
        documents: list[list[str]],
    ):

        self.documents = documents

        self.idf_values = (
            self.idf.calculate(
                documents
            )
        )

        self.vocabulary = sorted(
            self.idf_values.keys()
        )

        return self

    def transform(
        self,
        document: list[str],
    ) -> list[float]:

        if not hasattr(self, "idf_values"):
            raise RuntimeError(
                "TFIDF precisa ser treinado com fit()"
            )

        tf_values = self.tf.calculate(
            document
        )

        return [
            tf_values.get(term, 0.0)
            * self.idf_values.get(term, 0.0)
            for term in self.vocabulary
        ]

    def fit_transform(
        self,
        documents: list[list[str]],
    ):

        self.fit(documents)

        return [
            self.transform(document)
            for document in documents
        ]