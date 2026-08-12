from pathlib import Path


def build_file_metadata(
    path: str,
) -> dict:

    file_path = Path(path)

    return {
        "filename": file_path.name,
        "extension": file_path.suffix.lower(),
        "directory": str(
            file_path.parent
        ),
        "size": file_path.stat().st_size,
    }