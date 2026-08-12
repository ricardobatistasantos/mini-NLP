import hashlib


def calculate_checksum(
    text: str,
) -> str:

    return hashlib.sha256(
        text.encode("utf-8")
    ).hexdigest()


def calculate_file_checksum(
    path: str,
) -> str:

    sha256 = hashlib.sha256()

    with open(
        path,
        "rb",
    ) as file:

        while chunk := file.read(
            1024 * 1024
        ):

            sha256.update(chunk)

    return sha256.hexdigest()