from .models import RetrievedChunk


class RetrievalAdapter:

    def __init__(
        self,
        retrieval_pipeline,
    ):

        self.retrieval_pipeline = (
            retrieval_pipeline
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 5,
        filters: dict | None = None,
    ):

        results = (
            self.retrieval_pipeline.search(
                query=query,
                top_k=top_k,
                filters=filters,
            )
        )

        return [
            RetrievedChunk(
                id=result.id,
                document_id=result.metadata.get(
                    "document_id",
                    "",
                ),
                text=result.text,
                score=result.score,
                position=result.metadata.get(
                    "position",
                    0,
                ),
                metadata=result.metadata,
            )
            for result in results
        ]