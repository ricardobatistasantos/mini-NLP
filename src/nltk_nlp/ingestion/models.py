from dataclasses import dataclass, field
from enum import Enum


class IngestionStatus(str, Enum):

    SUCCESS = "success"

    SKIPPED = "skipped"

    FAILED = "failed"


@dataclass
class IngestionResult:

    document_id: str

    source: str

    status: IngestionStatus

    chunks: int = 0

    error: str | None = None

    metadata: dict = field(
        default_factory=dict
    )