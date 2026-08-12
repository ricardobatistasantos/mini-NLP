"""
Exemplo 08 - Embeddings e Busca Vetorial

Conceito: Representar texto como vetores densos em um espaço vetorial.
- Embeddings capturam SIGNIFICADO, não apenas palavras
- Busca vetorial encontra textos semanticamente similares
- Vector Store armazena e busca por similaridade de cosseno

Diferente do BM25 (lexical), embeddings entendem que
"automóvel" e "carro" são a mesma coisa.
"""

from nltk_nlp.embeddings.hash_embedding import HashEmbedding
from nltk_nlp.vector_store.memory_store import MemoryVectorStore
from nltk_nlp.vector_store.models import VectorRecord


def main():
    # Modelo de embedding (hash-based, sem dependência externa)
    embedding_model = HashEmbedding(dimensions=64)

    # Criar vector store
    store = MemoryVectorStore()

    # Documentos para indexar
    documents = [
        ("doc-1", "Python é excelente para ciência de dados e machine learning"),
        ("doc-2", "JavaScript é a linguagem principal para desenvolvimento web"),
        ("doc-3", "Docker permite criar containers para deploy de aplicações"),
        ("doc-4", "Pandas e NumPy são bibliotecas Python para análise de dados"),
        ("doc-5", "React e Vue são frameworks frontend para aplicações web"),
    ]

    # Indexar documentos
    print("=== INDEXANDO DOCUMENTOS ===")
    for doc_id, text in documents:
        vector = embedding_model.embed(text)
        record = VectorRecord(
            id=doc_id,
            vector=vector,
            text=text,
            metadata={"source": "knowledge_base"},
        )
        store.add(record)
        print(f"  ✓ {doc_id}: {text[:50]}...")

    print(f"\n  Total indexados: {store.count()}")

    # Buscar por similaridade
    print("\n=== BUSCA VETORIAL ===")
    queries = [
        "análise de dados com Python",
        "criar sites e aplicações web",
        "containers e deploy",
    ]

    for query in queries:
        query_vector = embedding_model.embed(query)
        results = store.search(query_vector, top_k=3)

        print(f"\n  Query: \"{query}\"")
        for i, result in enumerate(results, 1):
            print(f"    {i}. [{result.score:.4f}] {result.text[:55]}...")


if __name__ == "__main__":
    main()
