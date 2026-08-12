import math


class InverseDocumentFrequency:

    def calculate(
        self,
        documents: list[list[str]],
    ) -> dict[str, float]:

        total_documents = len(documents)

        if total_documents == 0:
            return {}

        vocabulary = set()

        for document in documents:
            vocabulary.update(document)

        idf = {}

        for term in vocabulary:

            document_frequency = sum(
                1
                for document in documents
                if term in document
            )

            idf[term] = math.log(
                total_documents /
                document_frequency
            )

        return idf

    def calculate_term(
        self,
        term: str,
        documents: list[list[str]],
    ) -> float:

        total_documents = len(documents)

        if total_documents == 0:
            return 0.0

        document_frequency = sum(
            1
            for document in documents
            if term in document
        )

        if document_frequency == 0:
            return 0.0

        return math.log(
            total_documents /
            document_frequency
        )