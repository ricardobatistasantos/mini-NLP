# Exemplo 09 - Retrieval Híbrido (BM25 + Vetorial + Reranking)

## O que é Retrieval Híbrido?

Busca híbrida combina **duas estratégias complementares** de recuperação de documentos:

- **BM25 (lexical)** — boa para correspondência exata de palavras. Se a query diz "FastAPI", encontra documentos com "FastAPI".
- **Vetorial (semântico)** — boa para sinônimos e conceitos. A query "framework web" encontra documentos sobre "FastAPI" mesmo sem a palavra exata.

Nenhuma das duas é perfeita sozinha. A combinação pega o melhor de ambas.

## Onde isso é usado?

- Elasticsearch com kNN — combina BM25 clássico com busca vetorial
- Pinecone / Weaviate / Qdrant — vector databases com busca híbrida nativa
- RAG em produção — Langchain e LlamaIndex usam retrieval híbrido por padrão
- E-commerce — busca por nome do produto (lexical) + "parecidos com" (semântica)
- Perguntas e respostas — encontrar trechos relevantes em bases de conhecimento

## Como funciona neste exemplo

### Pipeline completo

```
Query
  ├── BM25 → [doc3: 0.95, doc1: 0.80, doc5: 0.60]  (lexical)
  └── Vector → [doc1: 0.92, doc3: 0.85, doc2: 0.70]  (semântico)
        │
        ▼
   Reciprocal Rank Fusion → combina rankings
        │
        ▼
   Deduplicator → remove documentos duplicados
        │
        ▼
   Reranker → reordena por relevância final
        │
        ▼
   Threshold → remove resultados com score muito baixo
        │
        ▼
   Top-K → retorna os melhores
```

### Reciprocal Rank Fusion (RRF)

Combina múltiplos rankings sem precisar normalizar scores:

```
RRF_score(d) = Σ 1 / (k + rank_i(d))
```

Onde `k=60` (constante) e `rank_i(d)` é a posição do documento d no ranking i.

```python
fusion = ReciprocalRankFusion(k=60)
combined = fusion.fuse([bm25_results, vector_results])
```

**Vantagem:** funciona mesmo quando os scores de diferentes sistemas têm escalas incompatíveis.

### Keyword Reranker

Reordena os resultados finais medindo overlap entre query e documento:

```python
reranker = KeywordReranker()
reranked = reranker.rerank(query="Python ML", results=candidates)
```

**Score de rerank:** porcentagem dos termos da query encontrados no documento.

### Score Threshold

Remove resultados com relevância abaixo de um mínimo:

```python
threshold = ScoreThreshold(threshold=0.01)
filtered = threshold.apply(results)
```

### Deduplicator

Remove documentos que aparecem em ambos os rankings:

```python
deduplicator = Deduplicator()
unique = deduplicator.deduplicate(results)
```

## Como rodar

```bash
uv run python main.py
```

## Saída esperada

```
=== QUERY: "Python para machine learning" ===

--- BM25 (Lexical) ---
  [2.8321] Machine learning pode ser implementado com scikit-learn em P...
  [1.2802] TensorFlow e PyTorch são frameworks de deep learning em Pyth...

--- Vetorial ---
  [0.7217] Python é usado para inteligência artificial e aprendizado de...
  [0.5547] Machine learning pode ser implementado com scikit-learn em P...

--- Híbrido (Reciprocal Rank Fusion) ---
  [0.0325] (rerank: 0.75) Machine learning pode ser implementado...
  [0.0323] (rerank: 0.50) Python é usado para inteligência artificial...
```

## Arquivos do projeto

```
exemplo-09/
├── main.py
├── pyproject.toml
└── nltk_nlp/
    ├── embeddings/
    │   ├── base.py
    │   ├── hash_embedding.py
    │   └── similarity.py
    ├── vector_store/
    │   ├── models.py
    │   ├── vector_store.py
    │   ├── distance.py
    │   ├── filters.py
    │   └── memory_store.py
    └── retrieval/
        ├── models.py          # RetrievalDocument, RetrievalResult
        ├── lexical.py         # Tokenizador para BM25
        ├── bm25.py            # Busca lexical
        ├── vector.py          # Busca vetorial
        ├── hybrid.py          # Combina lexical + vetorial
        ├── fusion.py          # RRF + normalização de scores
        ├── reranker.py        # Reordena por keywords
        ├── threshold.py       # Filtra scores baixos
        └── deduplicator.py    # Remove duplicatas
```

## Como evoluir

1. **Tunar pesos** — dar mais peso para BM25 ou vetorial dependendo do domínio
2. **Cross-encoder reranker** — usar um modelo que recebe (query, documento) juntos para reranking mais preciso
3. **Query decomposition** — quebrar queries complexas em sub-queries e fusionar resultados
4. **Feedback loop** — usar cliques do usuário para ajustar os pesos do rankeamento
5. **Mais signals** — adicionar recência, popularidade, PageRank ao score final
6. **Implementar RetrievalPipeline** — compor todos os passos em uma pipeline configurável (já existe em `retrieval/pipeline.py` no código completo)
7. **Avaliar com métricas** — implementar NDCG, MAP, MRR para medir qualidade do ranking
8. **Próximo passo natural** → ir para o **Exemplo 10** que usa esse retrieval para alimentar um LLM (RAG)
