from mini_nlp.embeddings.hash_embedding import (
    HashEmbedding,
)

from mini_nlp.vector_store.memory_store import (
    MemoryVectorStore,
)

from mini_nlp.rag import (
    Document,
    TextChunker,
    MockGenerator,
    RAGPipeline,
)


embedding_model = HashEmbedding(
    dimensions=128
)

vector_store = MemoryVectorStore()

generator = MockGenerator()

chunker = TextChunker(
    chunk_size=20,
    overlap=5,
)


rag = RAGPipeline(
    embedding_model=embedding_model,
    vector_store=vector_store,
    generator=generator,
    chunker=chunker,
)


document = Document(
    id="python-001",
    text="""
    Python é uma linguagem de programação
    de alto nível. Ela possui uma sintaxe
    simples e pode ser utilizada para
    desenvolvimento web, automação,
    ciência de dados e inteligência
    artificial.
    """,
    metadata={
        "source": "python.txt",
        "category": "programming",
    },
)


chunks = rag.ingest(
    document
)


print(
    f"Chunks criados: {len(chunks)}"
)


result = rag.ask(
    query="Para que Python pode ser utilizada?",
    top_k=3,
)


print(
    "\nRESPOSTA:"
)

print(
    result["answer"]
)


print(
    "\nCONTEXTO:"
)

print(
    result["context"]
)