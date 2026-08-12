"""
Exemplo 07 - Busca Lexical com BM25

Conceito: Buscar documentos relevantes usando ranqueamento BM25.
- BM25 combina TF, IDF e normalização de tamanho do documento
- É o algoritmo padrão de search engines como Elasticsearch
- Não precisa de embeddings ou modelos treinados

A ideia: dado uma pergunta, quais documentos do corpus são mais relevantes?
"""

from nltk_nlp.retrieval.models import RetrievalDocument
from nltk_nlp.retrieval.bm25 import BM25


def main():
    # Corpus de documentos
    documents = [
        RetrievalDocument(
            id="doc-1",
            text="Python é uma linguagem de programação de alto nível usada para ciência de dados",
            metadata={"source": "wiki"},
        ),
        RetrievalDocument(
            id="doc-2",
            text="Java é uma linguagem orientada a objetos muito usada em aplicações corporativas",
            metadata={"source": "wiki"},
        ),
        RetrievalDocument(
            id="doc-3",
            text="Machine learning usa algoritmos para aprender padrões a partir de dados",
            metadata={"source": "wiki"},
        ),
        RetrievalDocument(
            id="doc-4",
            text="FastAPI é um framework Python para criar APIs web de alto desempenho",
            metadata={"source": "docs"},
        ),
        RetrievalDocument(
            id="doc-5",
            text="O gato dormiu no sofá durante toda a tarde de domingo",
            metadata={"source": "random"},
        ),
    ]

    # Criar índice BM25
    bm25 = BM25(documents, k1=1.5, b=0.75)

    # Buscar
    queries = [
        "linguagem de programação Python",
        "aprender padrões com dados",
        "framework web API",
    ]

    for query in queries:
        print(f"=== QUERY: \"{query}\" ===")
        results = bm25.search(query, top_k=3)

        for i, result in enumerate(results, 1):
            if result.score > 0:
                print(f"  {i}. [{result.score:.4f}] {result.text[:60]}...")
            else:
                print(f"  {i}. [{result.score:.4f}] (irrelevante) {result.text[:40]}...")
        print()


if __name__ == "__main__":
    main()
