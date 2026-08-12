from .document import Document
from .preprocessor import RetrievalPreprocessor
from ..features.vectorizer import TFIDFVectorizer


class DocumentIndex:

    def __init__(self):

        self.documents: list[Document] = []

        self.preprocessor = (
            RetrievalPreprocessor()
        )

        self.vectorizer = (
            TFIDFVectorizer()
        )

        self.vectors = []

    def add(
        self,
        document: Document,
    ):

        self.documents.append(
            document
        )

    def build(self):

        tokenized_documents = [
            self.preprocessor.process(
                document.text
            )
            for document
            in self.documents
        ]

        self.vectors = (
            self.vectorizer
            .fit_transform(
                tokenized_documents
            )
        )

    def get_documents(self):

        return self.documents

    def get_vectors(self):

        return self.vectors