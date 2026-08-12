from pathlib import Path

from ..checksum import calculate_checksum
from ..ids import generate_document_id
from ..metadata import build_file_metadata
from ..models import Document

from .base import DocumentLoader


class MarkdownLoader(DocumentLoader):

    def supports(
        self,
        path: str,
    ) -> bool:

        return Path(path).suffix.lower() in {
            ".md",
            ".markdown",
        }

    def load(
        self,
        path: str,
    ) -> list[Document]:

        file_path = Path(path)

        text = file_path.read_text(
            encoding="utf-8"
        )

        document_id = (
            generate_document_id(
                str(file_path.resolve())
            )
        )

        metadata = (
            build_file_metadata(path)
        )

        metadata["source_type"] = "markdown"

        return [
            Document(
                id=document_id,
                text=text,
                source=str(
                    file_path.resolve()
                ),
                mime_type="text/markdown",
                metadata=metadata,
                checksum=calculate_checksum(
                    text
                ),
            )
        ]