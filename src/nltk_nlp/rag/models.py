from dataclasses import dataclass, field
from typing import Any


@dataclass
class Document:

    id: str

    text: str

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


@dataclass
class Chunk:

    id: str

    document_id: str

    text: str

    position: int

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


@dataclass
class RetrievedChunk:

    id: str

    document_id: str

    text: str

    score: float

    position: int

    metadata: dict[str, Any] = field(
        default_factory=dict
    )