from pathlib import Path

from .models import Document


class DocumentLoader:

    def load_text(
        self,
        text: str,
        document_id: str,
        metadata: dict | None = None,
    ) -> Document:

        return Document(
            id=document_id,
            text=text,
            metadata=metadata or {},
        )

    def load_file(
        self,
        path: str,
        document_id: str | None = None,
        metadata: dict | None = None,
    ) -> Document:

        file_path = Path(path)

        text = file_path.read_text(
            encoding="utf-8"
        )

        return Document(
            id=(
                document_id
                or file_path.stem
            ),
            text=text,
            metadata=metadata or {},
        )