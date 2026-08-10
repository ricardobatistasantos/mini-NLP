from dataclasses import dataclass, field

@dataclass
class NLPResult:
    original_text: str
    tokens: list[str] = field(default_factory=list)
    normalized_tokens: list[str] = field(default_factory=list)
    stems: list[str] = field(default_factory=list)