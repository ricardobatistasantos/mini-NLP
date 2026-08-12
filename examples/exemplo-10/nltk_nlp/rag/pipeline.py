from nltk_nlp.embeddings.base import (
    EmbeddingModel,
)

from nltk_nlp.vector_store.vector_store import (
    VectorStore,
)

from .chunker import TextChunker
from .context import ContextBuilder
from .generator import Generator
from .indexer import RAGIndexer
from .models import Document
from .prompt import PromptBuilder
from .retriever import Retriever


class RAGPipeline:

    def __init__(
        self,
        embedding_model: EmbeddingModel,
        vector_store: VectorStore,
        generator: Generator,
        chunker: TextChunker | None = None,
    ):

        self.embedding_model = (
            embedding_model
        )

        self.vector_store = (
            vector_store
        )

        self.generator = generator

        self.chunker = (
            chunker
            or TextChunker()
        )

        self.indexer = RAGIndexer(
            embedding_model,
            vector_store,
        )

        self.retriever = Retriever(
            embedding_model,
            vector_store,
        )

        self.context_builder = (
            ContextBuilder()
        )

        self.prompt_builder = (
            PromptBuilder()
        )

    def ingest(
        self,
        document: Document,
    ):

        chunks = self.chunker.split(
            document
        )

        self.indexer.index_chunks(
            chunks
        )

        return chunks

    def ask(
        self,
        query: str,
        top_k: int = 5,
        filters: dict | None = None,
    ):

        retrieved_chunks = (
            self.retriever.retrieve(
                query=query,
                top_k=top_k,
                filters=filters,
            )
        )

        context = (
            self.context_builder.build(
                retrieved_chunks
            )
        )

        prompt = (
            self.prompt_builder.build(
                query=query,
                context=context,
            )
        )

        answer = (
            self.generator.generate(
                prompt
            )
        )

        return {
            "query": query,
            "answer": answer,
            "context": context,
            "chunks": retrieved_chunks,
            "prompt": prompt,
        }