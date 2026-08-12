from dataclasses import dataclass, field
from typing import Any


@dataclass
class Document:

    id: str

    text: str

    source: str

    mime_type: str

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    checksum: str | None = None

    version: int = 1


@dataclass
class DocumentChunk:

    id: str

    document_id: str

    text: str

    position: int

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    start_offset: int = 0

    end_offset: int = 0