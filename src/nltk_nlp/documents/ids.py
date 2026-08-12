import hashlib


def generate_document_id(
    source: str,
) -> str:

    return hashlib.sha256(
        source.encode("utf-8")
    ).hexdigest()[:32]


def generate_chunk_id(
    document_id: str,
    position: int,
) -> str:

    value = (
        f"{document_id}:{position}"
    )

    return hashlib.sha256(
        value.encode("utf-8")
    ).hexdigest()[:32]