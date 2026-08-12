# Mini NLP

Projeto educacional de NLP (Processamento de Linguagem Natural) em Python.
Cada exemplo é um **projeto independente** com complexidade progressiva, indo de tokenização básica até um pipeline RAG completo.

## Requisitos

- Python 3.10+
- [uv](https://docs.astral.sh/uv/getting-started/installation/)

## Como rodar

Cada exemplo é um projeto Python independente. Entre na pasta e use `uv`:

```bash
cd examples/exemplo-01

# Instalar dependências
uv sync

# Para exemplos 01-06, baixar dados do NLTK (primeira vez):
uv run python download_nltk.py

# Rodar
uv run python main.py
```

---

## Exemplos

### Exemplo 01 — Tokenização Básica

O ponto de partida de qualquer pipeline NLP: quebrar texto bruto em peças manipuláveis.

- Tokenização de sentenças (implementação manual por pontuação)
- Tokenização de palavras (NLTK `word_tokenize` para português)

**Entrada:** `"Python é incrível. Ela facilita NLP!"`
**Saída:** sentenças separadas + lista de tokens individuais

**Dependências:** `nltk`

---

### Exemplo 02 — Normalização de Texto

Padronizar tokens para reduzir variações que não agregam significado.

- Lowercase — "Python" e "python" viram a mesma coisa
- Stopwords — remove palavras sem carga semântica ("o", "de", "que")
- Stemming — reduz ao radical com RSLPStemmer ("programando" → "program")

**Entrada:** `"Os programadores estão estudando as linguagens de programação modernas"`
**Saída:** `["program", "estud", "lingu", "program", "modern"]`

**Dependências:** `nltk`

---

### Exemplo 03 — Estatísticas e Vocabulário

Quantificar o texto: frequência, distribuição e vocabulário.

- Contagem de frequência — quantas vezes cada palavra aparece
- Top N mais comuns — ranking das palavras dominantes
- Vocabulário — conjunto de palavras únicas

**Entrada:** texto com repetição de "python", "linguagem", etc.
**Saída:** histograma de frequências + tamanho do vocabulário

**Dependências:** `nltk`

---

### Exemplo 04 — Análise Linguística (POS, NER, N-grams)

Extrair estrutura do texto: função gramatical, entidades e colocações.

- POS Tagging — classifica tokens (verbo, substantivo, pronome, etc.)
- NER — reconhece entidades nomeadas (valores monetários R$)
- N-grams — gera bigramas e trigramas (sequências de palavras consecutivas)

**Entrada:** `"Eu quero comprar um notebook por R$ 3.500,00 para estudar Python"`
**Saída:** tags gramaticais + entidade MONEY detectada + bigramas/trigramas

**Dependências:** `nltk`

---

### Exemplo 05 — Representação Vetorial (Bag of Words + TF-IDF)

Transformar texto em números para que algoritmos possam comparar documentos.

- Bag of Words — vetor de contagem por palavra
- TF-IDF — pondera pela raridade (palavras comuns valem menos)
- Similaridade de Cosseno — mede quão parecidos dois documentos são (0 a 1)

**Entrada:** 3 documentos (2 sobre programação, 1 sobre gato)
**Saída:** vetores numéricos + score de similaridade mostrando que docs de programação são mais parecidos entre si

**Dependências:** `nltk`

---

### Exemplo 06 — Classificação de Texto (Naive Bayes)

Categorizar textos automaticamente usando probabilidade bayesiana.

- Treinar com documentos rotulados (financeiro, suporte, cancelamento)
- Prever a categoria de textos novos
- Suavização de Laplace para lidar com palavras nunca vistas

**Entrada:** mensagens de atendimento ao cliente
**Saída:** classificação automática por departamento

**Dependências:** `nltk`

---

### Exemplo 07 — Busca Lexical com BM25

Ranquear documentos por relevância usando o algoritmo padrão de search engines.

- BM25 combina TF, IDF e normalização pelo tamanho do documento
- Mesmo algoritmo usado por Elasticsearch e Solr
- Não precisa de embeddings ou modelos treinados

**Entrada:** corpus de 5 documentos + queries de busca
**Saída:** documentos ranqueados por score de relevância

**Dependências:** nenhuma (implementação pura Python)

---

### Exemplo 08 — Embeddings e Busca Vetorial

Representar texto como vetores densos que capturam significado semântico.

- HashEmbedding — embedding determinístico sem API externa
- Vector Store em memória — armazena e busca por similaridade
- Filtros de metadata — refinar resultados por atributos

**Entrada:** 5 documentos indexados + queries semânticas
**Saída:** documentos mais similares por significado (não apenas palavras exatas)

**Dependências:** nenhuma (implementação pura Python)

---

### Exemplo 09 — Retrieval Híbrido (BM25 + Vetorial + Reranking)

Combinar busca lexical e semântica para o melhor dos dois mundos.

- BM25 para correspondência exata de termos
- Busca vetorial para similaridade semântica
- Reciprocal Rank Fusion (RRF) para fundir os rankings
- Reranker por keywords + threshold + deduplicação

**Entrada:** corpus de 6 documentos + query "Python para machine learning"
**Saída:** comparação BM25 vs Vetorial vs Híbrido com scores

**Dependências:** nenhuma (implementação pura Python)

---

### Exemplo 10 — RAG (Retrieval-Augmented Generation)

Pipeline completo que permite uma LLM responder perguntas com base em documentos externos.

- Ingestão: documento → chunking com overlap → embedding → vector store
- Consulta: query → busca vetorial → monta contexto → prompt → LLM → resposta
- MockGenerator para rodar sem LLM (troque por OllamaGenerator para usar com Ollama)

**Entrada:** documento sobre Python + perguntas
**Saída:** chunks recuperados + resposta gerada com base no contexto

**Dependências:** `requests` (para integração com Ollama)

---

## Mapa de aprendizado

```
Texto bruto
    │
    ▼
[01] Tokenização ──── quebrar em peças
    │
    ▼
[02] Normalização ─── limpar e padronizar
    │
    ▼
[03] Estatísticas ─── entender a distribuição
    │
    ▼
[04] Linguística ──── entender a estrutura
    │
    ▼
[05] Vetorização ──── transformar em números
    │
    ▼
[06] Classificação ── categorizar automaticamente
    │
    ▼
[07] Busca lexical ── encontrar por palavras (BM25)
    │
    ▼
[08] Embeddings ───── encontrar por significado
    │
    ▼
[09] Híbrido ──────── combinar estratégias
    │
    ▼
[10] RAG ──────────── responder perguntas com documentos
```

## Estrutura de cada exemplo

```
exemplo-XX/
├── main.py              # Script principal executável
├── download_nltk.py     # Download de dados NLTK (exemplos 01-06)
├── pyproject.toml       # Dependências do projeto
├── .python-version      # Versão do Python
├── README.md            # Documentação detalhada do conceito
└── nltk_nlp/            # Módulos necessários (apenas os que o exemplo usa)
```
