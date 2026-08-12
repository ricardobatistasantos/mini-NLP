from typing import Any


class MetadataFilter:

    def matches(
        self,
        metadata: dict[str, Any],
        filters: dict[str, Any] | None,
    ) -> bool:

        if not filters:
            return True

        for key, expected_value in filters.items():

            if key not in metadata:
                return False

            if metadata[key] != expected_value:
                return False

        return True