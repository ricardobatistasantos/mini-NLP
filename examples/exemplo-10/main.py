"""
Exemplo 10 - RAG (Retrieval-Augmented Generation)

Conceito: Combinar busca de documentos + geração de resposta com LLM.
Este é o padrão usado por ChatGPT com documentos, Perplexity, etc.

Pipeline RAG completo:
1. Ingerir documento → chunking (dividir em pedaços)
2. Indexar chunks → gerar embeddings e armazenar
3. Query → buscar chunks relevantes
4. Montar contexto → construir prompt com os chunks
5. Gerar resposta → LLM responde baseado no contexto

Este exemplo usa um MockGenerator (sem LLM real).
Para usar com Ollama, troque por OllamaGenerator.
"""

from nltk_nlp.embeddings.hash_embedding import HashEmbedding
from nltk_nlp.vector_store.memory_store import MemoryVectorStore
from nltk_nlp.rag import (
    Document,
    TextChunker,
    MockGenerator,
    RAGPipeline,
)


def main():
    # Setup
    embedding_model = HashEmbedding(dimensions=128)
    vector_store = MemoryVectorStore()
    generator = MockGenerator()
    chunker = TextChunker(chunk_size=15, overlap=3)

    # Pipeline RAG
    rag = RAGPipeline(
        embedding_model=embedding_model,
        vector_store=vector_store,
        generator=generator,
        chunker=chunker,
    )

    # Documento para ingerir
    document = Document(
        id="python-guide",
        text="""
        Python é uma linguagem de programação de alto nível criada por Guido van Rossum.
        Ela é muito utilizada para ciência de dados, machine learning e automação.
        Python possui uma sintaxe simples e legível, facilitando o aprendizado.
        Bibliotecas populares incluem NumPy, Pandas, Matplotlib e Scikit-learn.
        Para desenvolvimento web, os frameworks mais usados são Django e FastAPI.
        Python também é usado para automação de tarefas com scripts simples.
        A comunidade Python é grande e ativa, com milhares de pacotes no PyPI.
        """,
        metadata={"source": "python_guide.txt", "category": "programming"},
    )

    # 1. Ingerir
    print("=== 1. INGESTÃO (Chunking) ===")
    chunks = rag.ingest(document)
    for chunk in chunks:
        print(f"  Chunk {chunk.position}: \"{chunk.text[:50]}...\"")

    print(f"\n  Total chunks: {len(chunks)}")
    print(f"  Vetores armazenados: {vector_store.count()}")

    # 2. Perguntar
    print("\n=== 2. RAG - PERGUNTAR ===")
    queries = [
        "Para que Python é utilizada?",
        "Quais são os frameworks web em Python?",
        "Quem criou Python?",
    ]

    for query in queries:
        result = rag.ask(query, top_k=2)

        print(f"\n  Pergunta: \"{query}\"")
        print(f"  Chunks recuperados: {len(result['chunks'])}")
        for i, chunk in enumerate(result['chunks'], 1):
            print(f"    {i}. [{chunk.score:.4f}] \"{chunk.text[:50]}...\"")
        print(f"  Resposta: {result['answer']}")


if __name__ == "__main__":
    main()
