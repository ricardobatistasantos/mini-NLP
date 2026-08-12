from dataclasses import dataclass, field


@dataclass
class Entity:
    text: str
    type: str
    start: int | None = None
    end: int | None = None


@dataclass
class NLPResult:

    original_text: str

    sentences: list[str] = field(
        default_factory=list
    )

    tokens: list[str] = field(
        default_factory=list
    )

    normalized_tokens: list[str] = field(
        default_factory=list
    )

    stems: list[str] = field(
        default_factory=list
    )

    lemmas: list[str] = field(
        default_factory=list
    )

    pos_tags: list[tuple[str, str]] = field(
        default_factory=list
    )

    entities: list[Entity] = field(
        default_factory=list
    )

    unigrams: list[tuple[str, ...]] = field(
        default_factory=list
    )

    bigrams: list[tuple[str, ...]] = field(
        default_factory=list
    )

    trigrams: list[tuple[str, ...]] = field(
        default_factory=list
    )