from dataclasses import dataclass, field
from typing import Any


@dataclass
class VectorRecord:

    id: str

    vector: list[float]

    text: str

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


@dataclass
class SearchResult:

    id: str

    score: float

    text: str

    metadata: dict[str, Any]