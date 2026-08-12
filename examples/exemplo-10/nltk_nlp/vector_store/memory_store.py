from .vector_store import VectorStore
from .models import (
    VectorRecord,
    SearchResult,
)
from .distance import cosine_similarity
from .filters import MetadataFilter


class MemoryVectorStore(VectorStore):

    def __init__(self):

        self.records: dict[
            str,
            VectorRecord
        ] = {}

        self.metadata_filter = (
            MetadataFilter()
        )

    def add(
        self,
        record: VectorRecord,
    ) -> None:

        self.records[
            record.id
        ] = record

    def add_many(
        self,
        records: list[VectorRecord],
    ) -> None:

        for record in records:
            self.add(record)

    def get(
        self,
        record_id: str,
    ) -> VectorRecord | None:

        return self.records.get(
            record_id
        )

    def delete(
        self,
        record_id: str,
    ) -> bool:

        if record_id not in self.records:
            return False

        del self.records[
            record_id
        ]

        return True

    def search(
        self,
        query_vector: list[float],
        top_k: int = 5,
        filters: dict | None = None,
    ) -> list[SearchResult]:

        results = []

        for record in self.records.values():

            if not self.metadata_filter.matches(
                record.metadata,
                filters,
            ):
                continue

            score = cosine_similarity(
                query_vector,
                record.vector,
            )

            results.append(
                SearchResult(
                    id=record.id,
                    score=score,
                    text=record.text,
                    metadata=record.metadata,
                )
            )

        results.sort(
            key=lambda result: result.score,
            reverse=True,
        )

        return results[:top_k]

    def count(self) -> int:

        return len(self.records)

    def clear(self) -> None:

        self.records.clear()