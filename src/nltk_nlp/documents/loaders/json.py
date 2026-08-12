import json
from pathlib import Path

from ..checksum import calculate_checksum
from ..ids import generate_document_id
from ..metadata import build_file_metadata
from ..models import Document

from .base import DocumentLoader


class JsonLoader(DocumentLoader):

    def supports(
        self,
        path: str,
    ) -> bool:

        return (
            Path(path).suffix.lower()
            == ".json"
        )

    def load(
        self,
        path: str,
    ) -> list[Document]:

        file_path = Path(path)

        data = json.loads(
            file_path.read_text(
                encoding="utf-8"
            )
        )

        metadata = (
            build_file_metadata(path)
        )

        metadata["source_type"] = "json"

        documents = []

        if isinstance(data, list):

            for index, item in enumerate(
                data
            ):

                text = self._to_text(
                    item
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
                        mime_type=(
                            "application/json"
                        ),
                        metadata={
                            **metadata,
                            "record_index": index,
                        },
                        checksum=calculate_checksum(
                            text
                        ),
                    )
                )

        else:

            text = self._to_text(
                data
            )

            document_id = (
                generate_document_id(
                    str(
                        file_path.resolve()
                    )
                )
            )

            documents.append(
                Document(
                    id=document_id,
                    text=text,
                    source=str(
                        file_path.resolve()
                    ),
                    mime_type=(
                        "application/json"
                    ),
                    metadata=metadata,
                    checksum=calculate_checksum(
                        text
                    ),
                )
            )

        return documents

    def _to_text(
        self,
        data,
    ) -> str:

        if isinstance(data, str):
            return data

        return json.dumps(
            data,
            ensure_ascii=False,
            indent=2,
        )