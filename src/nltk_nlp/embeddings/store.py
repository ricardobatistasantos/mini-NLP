from dataclasses import dataclass


@dataclass
class EmbeddingRecord:

    id: str

    text: str

    vector: list[float]

    metadata: dict


class EmbeddingStore:

    def __init__(self):

        self.records: list[
            EmbeddingRecord
        ] = []

    def add(
        self,
        record: EmbeddingRecord,
    ):

        self.records.append(
            record
        )

    def get_all(
        self,
    ) -> list[EmbeddingRecord]:

        return self.records

    def get(
        self,
        record_id: str,
    ):

        for record in self.records:

            if record.id == record_id:
                return record

        return None

    def clear(self):

        self.records.clear()

    def __len__(self):

        return len(self.records)