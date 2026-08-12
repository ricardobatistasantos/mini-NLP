from .index import DocumentIndex
from .ranker import Ranker


class SearchEngine:

    def __init__(
        self,
        index: DocumentIndex,
    ):

        self.index = index

        self.ranker = Ranker()

    def search(
        self,
        query: str,
        top_k: int = 5,
    ):

        tokens = (
            self.index.preprocessor
            .process(query)
        )

        query_vector = (
            self.index.vectorizer
            .model
            .transform(tokens)
        )

        ranked = self.ranker.rank(
            query_vector,
            self.index.get_vectors(),
            self.index.get_documents(),
        )

        return ranked[:top_k]