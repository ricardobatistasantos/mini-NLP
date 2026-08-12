import json
from pathlib import Path

from .memory_store import MemoryVectorStore
from .models import VectorRecord


class JsonVectorStore(
    MemoryVectorStore
):

    def __init__(
        self,
        path: str = "data/vectors.json",
    ):

        super().__init__()

        self.path = Path(path)

        self._ensure_directory()

        self.load()

    def _ensure_directory(self):

        self.path.parent.mkdir(
            parents=True,
            exist_ok=True,
        )

    def add(
        self,
        record: VectorRecord,
    ) -> None:

        super().add(record)

        self.save()

    def add_many(
        self,
        records: list[VectorRecord],
    ) -> None:

        for record in records:

            self.records[
                record.id
            ] = record

        self.save()

    def delete(
        self,
        record_id: str,
    ) -> bool:

        deleted = super().delete(
            record_id
        )

        if deleted:
            self.save()

        return deleted

    def clear(self) -> None:

        super().clear()

        self.save()

    def save(self):

        data = []

        for record in self.records.values():

            data.append({
                "id": record.id,
                "vector": record.vector,
                "text": record.text,
                "metadata": record.metadata,
            })

        with self.path.open(
            "w",
            encoding="utf-8",
        ) as file:

            json.dump(
                data,
                file,
                ensure_ascii=False,
                indent=2,
            )

    def load(self):

        if not self.path.exists():
            return

        with self.path.open(
            "r",
            encoding="utf-8",
        ) as file:

            data = json.load(file)

        self.records.clear()

        for item in data:

            record = VectorRecord(
                id=item["id"],
                vector=item["vector"],
                text=item["text"],
                metadata=item.get(
                    "metadata",
                    {},
                ),
            )

            self.records[
                record.id
            ] = record