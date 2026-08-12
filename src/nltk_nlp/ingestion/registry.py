from dataclasses import dataclass


@dataclass
class DocumentState:

    document_id: str

    checksum: str

    version: int


class DocumentRegistry:

    def __init__(self):

        self.documents: dict[
            str,
            DocumentState,
        ] = {}

    def get(
        self,
        document_id: str,
    ) -> DocumentState | None:

        return self.documents.get(
            document_id
        )

    def register(
        self,
        document_id: str,
        checksum: str,
        version: int,
    ) -> None:

        self.documents[
            document_id
        ] = DocumentState(
            document_id=document_id,
            checksum=checksum,
            version=version,
        )

    def has_changed(
        self,
        document_id: str,
        checksum: str,
    ) -> bool:

        state = self.get(
            document_id
        )

        if state is None:
            return True

        return (
            state.checksum
            != checksum
        )

    def remove(
        self,
        document_id: str,
    ) -> None:

        self.documents.pop(
            document_id,
            None,
        )