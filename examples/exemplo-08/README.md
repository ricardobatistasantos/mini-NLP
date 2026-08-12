# Exemplo 08 - Embeddings e Busca Vetorial

## O que são Embeddings?

Embeddings são **vetores densos** que representam o significado semântico de um texto. Diferente de BoW/TF-IDF (vetores esparsos com milhares de dimensões), embeddings são compactos (64-1536 dimensões) e capturam similaridade de significado.

Com embeddings, textos com palavras diferentes mas significado similar ficam próximos no espaço vetorial:
- "automóvel" ≈ "carro" ≈ "veículo" (próximos no espaço)
- "automóvel" ≠ "banana" (distantes no espaço)

## Onde isso é usado?

- Busca semântica — encontrar documentos por significado, não apenas por palavras-chave
- Sistemas de recomendação — recomendar itens com embeddings similares
- Detecção de duplicatas — textos com alta similaridade de embedding são duplicatas semânticas
- Clustering — agrupar documentos semanticamente similares sem labels
- RAG (Retrieval-Augmented Generation) — recuperar contexto relevante para LLMs
- Anomaly detection — embeddings muito distantes da média são anômalos

## Como funciona neste exemplo

### HashEmbedding (implementação didática)

Gera embeddings determinísticos usando hash — sem modelo de ML, sem API:

```python
from nltk_nlp.embeddings.hash_embedding import HashEmbedding

model = HashEmbedding(dimensions=64)
vector = model.embed("Python para ciência de dados")
# [0.0, 0.408, 0.0, ..., 0.408, 0.0]  (64 dimensões)
```

**Como funciona:**
1. Tokeniza o texto (split por espaço + lowercase)
2. Para cada token, calcula hash SHA-256
3. Usa o hash para determinar qual posição do vetor incrementar
4. Normaliza o vetor final (magnitude = 1)

**Limitação:** não captura semântica real — palavras sinônimas vão para posições diferentes. Em produção, use `sentence-transformers` ou embeddings do Ollama.

### Vector Store (`MemoryVectorStore`)

Armazena vetores e busca os mais similares:

```python
from nltk_nlp.vector_store.memory_store import MemoryVectorStore
from nltk_nlp.vector_store.models import VectorRecord

store = MemoryVectorStore()
store.add(VectorRecord(id="1", vector=[0.1, 0.9], text="...", metadata={}))

results = store.search(query_vector=[0.2, 0.8], top_k=3)
# [SearchResult(id="1", score=0.99, ...)]
```

**Pipeline de busca:**
1. Calcula similaridade de cosseno entre query_vector e todos os vetores armazenados
2. Aplica filtros de metadata (opcional)
3. Ordena por score decrescente
4. Retorna top_k resultados

### Filtros de Metadata

```python
results = store.search(
    query_vector=[...],
    top_k=5,
    filters={"source": "knowledge_base"},  # só retorna docs dessa source
)
```

## Como rodar

```bash
uv run python main.py
```

## Saída esperada

```
=== INDEXANDO DOCUMENTOS ===
  ✓ doc-1: Python é excelente para ciência de dados e machine...
  ✓ doc-2: JavaScript é a linguagem principal para desenvolvi...
  ...
  Total indexados: 5

=== BUSCA VETORIAL ===
  Query: "análise de dados com Python"
    1. [0.5657] Pandas e NumPy são bibliotecas Python para análise de d...
    2. [0.4243] Docker permite criar containers para deploy de aplicaçõ...
    3. [0.3873] Python é excelente para ciência de dados e machine lear...
```

## Arquivos do projeto

```
exemplo-08/
├── main.py
├── pyproject.toml         # Sem dependências externas!
└── nltk_nlp/
    ├── embeddings/
    │   ├── base.py           # Classe abstrata EmbeddingModel
    │   ├── hash_embedding.py # Implementação por hash (didática)
    │   └── similarity.py     # Cosseno + euclidiana
    └── vector_store/
        ├── models.py         # VectorRecord, SearchResult
        ├── vector_store.py   # Classe abstrata VectorStore
        ├── distance.py       # Cosseno para busca
        ├── filters.py        # Filtro de metadata
        └── memory_store.py   # Implementação em memória
```

## Como evoluir

1. **Usar embeddings reais** — instalar `sentence-transformers` e usar `all-MiniLM-L6-v2` para embeddings semânticos de verdade
2. **Persistir com JSON** — usar `JsonVectorStore` para salvar vetores em disco e não perder ao reiniciar
3. **Implementar HNSW** — algoritmo de busca aproximada (ANN) para milhões de vetores sem iterar todos
4. **Adicionar batch embedding** — embeddar múltiplos textos de uma vez para eficiência
5. **Visualizar embeddings** — usar t-SNE ou UMAP para plotar documentos em 2D
6. **Usar Ollama** — `OllamaEmbedding(model="nomic-embed-text")` para embeddings locais de alta qualidade
7. **Próximo passo natural** → ir para o **Exemplo 09** que combina BM25 (lexical) + vetorial (semântico) em um sistema híbrido
