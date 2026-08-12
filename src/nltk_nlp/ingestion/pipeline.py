from pathlib import Path

from mini_nlp.documents.loader_registry import (
    LoaderRegistry,
)

from mini_nlp.documents.chunkers.base import (
    DocumentChunker,
)

from mini_nlp.vector_store.vector_store import (
    VectorStore,
)

from .models import (
    IngestionResult,
    IngestionStatus,
)

from .processor import (
    DocumentProcessor,
)

from .registry import (
    DocumentRegistry,
)


class IngestionPipeline:

    def __init__(
        self,
        loader_registry: LoaderRegistry,
        processor: DocumentProcessor,
        document_registry: DocumentRegistry,
        vector_store: VectorStore,
    ):

        self.loader_registry = (
            loader_registry
        )

        self.processor = processor

        self.document_registry = (
            document_registry
        )

        self.vector_store = (
            vector_store
        )

    def ingest(
        self,
        path: str,
    ) -> list[IngestionResult]:

        loader = (
            self.loader_registry.get_loader(
                path
            )
        )

        documents = loader.load(
            path
        )

        results = []

        for document in documents:

            results.append(
                self._process_document(
                    document
                )
            )

        return results

    def _process_document(
        self,
        document,
    ) -> IngestionResult:

        try:

            state = (
                self.document_registry.get(
                    document.id
                )
            )

            if (
                state
                and state.checksum
                == document.checksum
            ):

                return IngestionResult(
                    document_id=document.id,
                    source=document.source,
                    status=(
                        IngestionStatus.SKIPPED
                    ),
                    metadata={
                        "reason": (
                            "unchanged"
                        )
                    },
                )

            if state:

                document.version = (
                    state.version + 1
                )

            chunks = (
                self.processor.process(
                    document
                )
            )

            self.document_registry.register(
                document_id=document.id,
                checksum=document.checksum,
                version=document.version,
            )

            return IngestionResult(
                document_id=document.id,
                source=document.source,
                status=(
                    IngestionStatus.SUCCESS
                ),
                chunks=len(chunks),
                metadata={
                    "version": (
                        document.version
                    ),
                },
            )

        except Exception as error:

            return IngestionResult(
                document_id=document.id,
                source=document.source,
                status=(
                    IngestionStatus.FAILED
                ),
                error=str(error),
            )