# Exemplo 07 - Busca Lexical com BM25

## O que é BM25?

BM25 (Best Matching 25) é o algoritmo de **ranqueamento de documentos** usado por search engines como Elasticsearch, Lucene e Solr. Dada uma query, ele pontua cada documento pela relevância.

É a evolução do TF-IDF para busca: combina frequência do termo, raridade no corpus e normalização pelo tamanho do documento.

## Onde isso é usado?

- Elasticsearch / OpenSearch — BM25 é o algoritmo padrão de scoring
- Google (parcialmente) — usa BM25 como um dos sinais de relevância
- Busca interna de apps — pesquisa em produtos, artigos, FAQ
- Legal discovery — buscar documentos jurídicos relevantes
- Busca acadêmica — encontrar papers por palavras-chave

## Como funciona neste exemplo

### A Fórmula BM25

```
score(D, Q) = Σ IDF(qi) × [f(qi, D) × (k1 + 1)] / [f(qi, D) + k1 × (1 - b + b × |D|/avgdl)]
```

Onde:
- `f(qi, D)` = frequência do termo qi no documento D
- `|D|` = tamanho do documento (em tokens)
- `avgdl` = tamanho médio dos documentos no corpus
- `k1` = controla saturação de TF (padrão: 1.5)
- `b` = controla normalização por tamanho (padrão: 0.75)

### Parâmetros k1 e b

- **k1 = 1.5** — controla quão rápido a frequência satura. Com k1 alto, uma palavra repetida 10x conta muito mais que 5x. Com k1 baixo, a diferença é menor.
- **b = 0.75** — controla o peso do tamanho do documento. Com b = 1, documentos longos são muito penalizados. Com b = 0, o tamanho é ignorado.

### Uso no código

```python
from nltk_nlp.retrieval.bm25 import BM25
from nltk_nlp.retrieval.models import RetrievalDocument

documents = [
    RetrievalDocument(id="1", text="Python para ciência de dados"),
    RetrievalDocument(id="2", text="Java para aplicações web"),
]

bm25 = BM25(documents, k1=1.5, b=0.75)
results = bm25.search("ciência de dados", top_k=3)
# [RetrievalResult(id="1", score=2.83, ...)]
```

### Pipeline interno

1. Tokeniza a query e todos os documentos (lowercase + regex `\b\w+\b`)
2. Calcula document frequency (DF) para cada termo
3. Para cada par (query_term, documento), calcula o score BM25
4. Soma os scores de todos os termos da query
5. Ordena documentos por score decrescente

## Como rodar

```bash
uv run python main.py
```

## Saída esperada

```
=== QUERY: "linguagem de programação Python" ===
  1. [3.3786] Python é uma linguagem de programação de alto nível usada pa...
  2. [1.1632] FastAPI é um framework Python para criar APIs web de alto de...
  3. [0.8755] Java é uma linguagem orientada a objetos muito usada em apli...

=== QUERY: "aprender padrões com dados" ===
  1. [3.7902] Machine learning usa algoritmos para aprender padrões a part...
  2. [0.8144] Python é uma linguagem de programação de alto nível usada pa...
  3. [0.0000] (irrelevante) Java é uma linguagem orientada a objetos...
```

## Arquivos do projeto

```
exemplo-07/
├── main.py
├── pyproject.toml        # Sem dependências externas!
└── nltk_nlp/
    └── retrieval/
        ├── models.py      # RetrievalDocument, RetrievalResult
        ├── lexical.py     # Tokenizador por regex
        └── bm25.py        # Implementação completa do BM25
```

## Como evoluir

1. **Tunar k1 e b** — experimentar diferentes valores e ver como afeta o ranking
2. **Adicionar query expansion** — expandir "ML" para "machine learning" antes de buscar
3. **Implementar BM25+** — variante que garante scores não-negativos para matching parcial
4. **Adicionar phrase search** — buscar documentos que contenham a sequência exata de palavras
5. **Implementar indexação invertida** — ao invés de iterar todos os documentos, construir um índice {termo → [doc_ids]} para busca O(1)
6. **Combinar com filtros** — aplicar filtros por metadata (source, date) antes do scoring
7. **Comparar com Elasticsearch** — rodar a mesma query num ES local e comparar scores
8. **Próximo passo natural** → ir para o **Exemplo 08** que usa embeddings para busca semântica (encontra sinônimos que BM25 não encontraria)
