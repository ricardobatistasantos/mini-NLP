from dataclasses import dataclass, field
from typing import Any


@dataclass
class RetrievalDocument:

    id: str

    text: str

    metadata: dict[str, Any] = field(
        default_factory=dict
    )


@dataclass
class RetrievalResult:

    id: str

    text: str

    score: float

    metadata: dict[str, Any] = field(
        default_factory=dict
    )

    lexical_score: float = 0.0

    vector_score: float = 0.0

    rerank_score: float = 0.0