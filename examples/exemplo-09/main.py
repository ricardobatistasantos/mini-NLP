"""
Exemplo 09 - Retrieval Híbrido (BM25 + Vetorial + Reranking)

Conceito: Combinar busca lexical (BM25) com busca vetorial para
obter o melhor dos dois mundos:
- BM25 → bom para correspondência exata de palavras
- Vetorial → bom para similaridade semântica
- Fusion → combina os dois rankings (Reciprocal Rank Fusion)
- Reranking → reordena resultados finais por relevância

Este é o padrão usado em sistemas de busca modernos.
"""

from nltk_nlp.embeddings.hash_embedding import HashEmbedding
from nltk_nlp.vector_store.memory_store import MemoryVectorStore
from nltk_nlp.vector_store.models import VectorRecord
from nltk_nlp.retrieval.models import RetrievalDocument
from nltk_nlp.retrieval.bm25 import BM25
from nltk_nlp.retrieval.vector import VectorRetriever
from nltk_nlp.retrieval.hybrid import HybridRetriever
from nltk_nlp.retrieval.reranker import KeywordReranker
from nltk_nlp.retrieval.threshold import ScoreThreshold
from nltk_nlp.retrieval.deduplicator import Deduplicator


def main():
    # Corpus
    corpus = [
        ("doc-1", "Python é usado para inteligência artificial e aprendizado de máquina"),
        ("doc-2", "O framework Django permite criar aplicações web em Python rapidamente"),
        ("doc-3", "TensorFlow e PyTorch são frameworks de deep learning em Python"),
        ("doc-4", "JavaScript com Node.js é popular para backend de APIs REST"),
        ("doc-5", "Ciência de dados usa Python com Pandas para análise exploratória"),
        ("doc-6", "Machine learning pode ser implementado com scikit-learn em Python"),
    ]

    # --- Setup BM25 ---
    retrieval_docs = [
        RetrievalDocument(id=doc_id, text=text)
        for doc_id, text in corpus
    ]
    bm25 = BM25(retrieval_docs)

    # --- Setup Vector Retriever ---
    embedding_model = HashEmbedding(dimensions=64)
    vector_store = MemoryVectorStore()

    for doc_id, text in corpus:
        vector = embedding_model.embed(text)
        vector_store.add(VectorRecord(
            id=doc_id,
            vector=vector,
            text=text,
            metadata={},
        ))

    vector_retriever = VectorRetriever(
        embedding_model=embedding_model,
        vector_store=vector_store,
    )

    # --- Hybrid ---
    hybrid = HybridRetriever(
        lexical_retriever=bm25,
        vector_retriever=vector_retriever,
    )

    # --- Pipeline completo ---
    reranker = KeywordReranker()
    threshold = ScoreThreshold(threshold=0.0)
    deduplicator = Deduplicator()

    query = "Python para machine learning"
    print(f"=== QUERY: \"{query}\" ===\n")

    # 1. Busca lexical (BM25)
    print("--- BM25 (Lexical) ---")
    bm25_results = bm25.search(query, top_k=3)
    for r in bm25_results:
        print(f"  [{r.score:.4f}] {r.text[:60]}...")

    # 2. Busca vetorial
    print("\n--- Vetorial ---")
    vector_results = vector_retriever.search(query, top_k=3)
    for r in vector_results:
        print(f"  [{r.score:.4f}] {r.text[:60]}...")

    # 3. Híbrido (fusão)
    print("\n--- Híbrido (Reciprocal Rank Fusion) ---")
    hybrid_results = hybrid.search(query, top_k=4)
    hybrid_results = deduplicator.deduplicate(hybrid_results)
    hybrid_results = reranker.rerank(query, hybrid_results)
    hybrid_results = threshold.apply(hybrid_results)

    for r in hybrid_results[:4]:
        print(f"  [{r.score:.4f}] (rerank: {r.rerank_score:.2f}) {r.text[:55]}...")


if __name__ == "__main__":
    main()
