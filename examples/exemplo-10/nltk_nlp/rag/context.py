from .models import RetrievedChunk


class ContextBuilder:

    def build(
        self,
        chunks: list[RetrievedChunk],
    ) -> str:

        if not chunks:
            return ""

        parts = []

        for index, chunk in enumerate(
            chunks,
            start=1,
        ):

            parts.append(
                (
                    f"[Contexto {index}]\n"
                    f"{chunk.text}"
                )
            )

        return "\n\n".join(
            parts
        )