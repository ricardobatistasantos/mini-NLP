from abc import ABC, abstractmethod

from ..models import (
    Document,
    DocumentChunk,
)


class DocumentChunker(ABC):

    @abstractmethod
    def chunk(
        self,
        document: Document,
    ) -> list[DocumentChunk]:
        pass