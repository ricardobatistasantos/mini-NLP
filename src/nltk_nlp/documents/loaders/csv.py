import csv
from pathlib import Path

from ..checksum import calculate_checksum
from ..ids import generate_document_id
from ..metadata import build_file_metadata
from ..models import Document

from .base import DocumentLoader


class CsvLoader(DocumentLoader):

    def supports(
        self,
        path: str,
    ) -> bool:

        return (
            Path(path).suffix.lower()
            == ".csv"
        )

    def load(
        self,
        path: str,
    ) -> list[Document]:

        file_path = Path(path)

        documents = []

        metadata = (
            build_file_metadata(path)
        )

        metadata["source_type"] = "csv"

        with file_path.open(
            "r",
            encoding="utf-8",
            newline="",
        ) as file:

            reader = csv.DictReader(
                file
            )

            for index, row in enumerate(
                reader
            ):

                text = self._row_to_text(
                    row
                )

                document_id = (
                    generate_document_id(
                        f"{file_path.resolve()}:{index}"
                    )
                )

                documents.append(
                    Document(
                        id=document_id,
                        text=text,
                        source=str(
                            file_path.resolve()
                        ),
                        mime_type="text/csv",
                        metadata={
                            **metadata,
                            "row_index": index,
                        },
                        checksum=calculate_checksum(
                            text
                        ),
                    )
                )

        return documents

    def _row_to_text(
        self,
        row: dict,
    ) -> str:

        parts = []

        for key, value in row.items():

            parts.append(
                f"{key}: {value}"
            )

        return "\n".join(parts)