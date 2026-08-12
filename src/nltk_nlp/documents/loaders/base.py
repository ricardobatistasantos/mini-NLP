from abc import ABC, abstractmethod

from ..models import Document


class DocumentLoader(ABC):

    @abstractmethod
    def supports(
        self,
        path: str,
    ) -> bool:
        pass

    @abstractmethod
    def load(
        self,
        path: str,
    ) -> list[Document]:
        pass