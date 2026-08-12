from abc import ABC, abstractmethod

from .models import (
    VectorRecord,
    SearchResult,
)


class VectorStore(ABC):

    @abstractmethod
    def add(
        self,
        record: VectorRecord,
    ) -> None:
        pass

    @abstractmethod
    def add_many(
        self,
        records: list[VectorRecord],
    ) -> None:
        pass

    @abstractmethod
    def get(
        self,
        record_id: str,
    ) -> VectorRecord | None:
        pass

    @abstractmethod
    def delete(
        self,
        record_id: str,
    ) -> bool:
        pass

    @abstractmethod
    def search(
        self,
        query_vector: list[float],
        top_k: int = 5,
        filters: dict | None = None,
    ) -> list[SearchResult]:
        pass

    @abstractmethod
    def count(self) -> int:
        pass

    @abstractmethod
    def clear(self) -> None:
        pass