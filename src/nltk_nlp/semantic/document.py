from dataclasses import dataclass, field


@dataclass
class SemanticDocument:

    id: str

    text: str

    metadata: dict = field(
        default_factory=dict
    )