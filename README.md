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

### Exemplo 11 — Avaliação de Retrieval (Métricas)

Medir a qualidade de um sistema de busca com métricas padrão da indústria.

- Precision@K, Recall@K, MRR, NDCG
- Ground truth: definir quais documentos são relevantes por query
- Métricas médias para avaliar o sistema como um todo

**Entrada:** queries com relevância esperada (ground truth)
**Saída:** scores de qualidade por query e médias gerais

**Dependências:** nenhuma (implementação pura Python)

---

### Exemplo 12 — Embeddings Reais (Ollama)

Trocar HashEmbedding por embeddings semânticos reais via Ollama.

- nomic-embed-text gera vetores de 768 dimensões
- Captura sinônimos: "carro" ≈ "automóvel"
- Busca semântica de verdade

**Entrada:** pares de palavras + documentos para busca
**Saída:** scores de similaridade reais + resultados semânticos

**Dependências:** `requests` | **Requer:** Ollama + nomic-embed-text

---

### Exemplo 13 — Ingestão de Documentos (Loaders + Chunkers)

Carregar arquivos e dividir em chunks para indexação.

- ParagraphChunker — divide por `\n\n`
- MarkdownChunker — divide por seções (`#`)
- RecursiveChunker — respeita tamanho máximo agrupando parágrafos
- IDs, checksums e metadata automáticos

**Entrada:** textos e markdown
**Saída:** chunks com offsets, IDs e metadata

**Dependências:** nenhuma (implementação pura Python)

---

### Exemplo 14 — RAG com LLM Real (Ollama)

Pipeline RAG com respostas geradas por uma LLM real.

- Ollama para embeddings E geração
- Responde baseado exclusivamente no contexto
- Prompt engineering anti-alucinação

**Entrada:** documento sobre FastAPI + perguntas
**Saída:** respostas em linguagem natural geradas pela LLM

**Dependências:** `requests` | **Requer:** Ollama + nomic-embed-text + llama3.2

---

### Exemplo 15 — Chat com Memória (Multi-turno)

Conversação interativa com histórico de conversa.

- ChatMemory armazena turnos anteriores
- Prompt inclui histórico + documentos + pergunta
- Entende referências anafóricas ("ele", "me fale mais")

**Entrada:** chat interativo no terminal
**Saída:** respostas contextualizadas com memória

**Dependências:** `requests` | **Requer:** Ollama + nomic-embed-text + llama3.2

---

### Exemplo 16 — Fine-tuning de Retrieval (Feedback)

Usar feedback do usuário para melhorar a busca sem retreinar modelos.

- Rocchio Algorithm — ajusta vetor da query com feedback
- Query Expansion — adiciona termos dos documentos relevantes
- Melhora ranking sem custo de treinamento

**Entrada:** query + feedback (relevante/irrelevante)
**Saída:** ranking melhorado após feedback

**Dependências:** nenhuma (implementação pura Python)

---

### Exemplo 17 — API REST (FastAPI)

Empacotar o RAG como microserviço com endpoints REST.

- POST /ingest — ingerir documentos
- POST /ask — fazer perguntas (RAG)
- GET /documents — listar documentos
- Swagger UI automática em /docs

**Entrada:** requisições HTTP (JSON)
**Saída:** respostas JSON com chunks e resposta gerada

**Dependências:** `fastapi`, `uvicorn`, `requests`

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
    │
    ▼
[11] Avaliação ────── medir qualidade (Precision, Recall, NDCG)
    │
    ▼
[12] Embeddings reais ─ semântica de verdade (Ollama)
    │
    ▼
[13] Ingestão ─────── carregar e chunkar arquivos reais
    │
    ▼
[14] RAG real ─────── respostas com LLM (Ollama)
    │
    ▼
[15] Chat ─────────── conversação com memória
    │
    ▼
[16] Feedback ─────── melhorar busca com feedback do usuário
    │
    ▼
[17] API REST ─────── deploy como microserviço (FastAPI)
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

---

## Roadmap completo (18-80)

### RAG em Produção (18-24)

| # | Tema | Descrição |
|---|------|-----------|
| 18 | Persistência (JSON Vector Store) | Salvar vetores em disco, versionamento com checksum |
| 19 | Multi-documento RAG | Ingerir múltiplos arquivos de uma pasta e buscar entre todos |
| 20 | Streaming de Respostas | Gerar token a token com Server-Sent Events |
| 21 | Guardrails (Anti-alucinação) | Verificar se a resposta está fundamentada no contexto |
| 22 | Agentes (Tool Calling) | LLM que decide qual ferramenta usar |
| 23 | Evaluation Pipeline (RAGAS) | Métricas end-to-end: faithfulness, relevancy, context recall |
| 24 | Docker + Deploy | Containerizar com Docker Compose (Ollama + API + volume) |

### Técnicas Avançadas (25-34)

| # | Tema | Descrição |
|---|------|-----------|
| 25 | Multi-modal (Imagens + Texto) | Descrever imagens com LLaVA e indexar junto com texto |
| 26 | Grafos de Conhecimento | Extrair entidades e relações, construir grafo, buscar por conexões |
| 27 | Summarização | Resumo automático (extractive + abstractive) |
| 28 | Tradução | Pipeline de tradução PT↔EN usando Ollama |
| 29 | Speech-to-Text + NLP | Transcrever áudio com Whisper e processar com o pipeline |
| 30 | Fine-tuning de Modelos | Ajustar modelo com dados próprios (LoRA) |
| 31 | RAG Multi-tenant | Isolamento por usuário/organização |
| 32 | Observabilidade | Tracing, métricas de latência, logs estruturados |
| 33 | Agentic RAG (Multi-step) | Decompor perguntas complexas em sub-queries e sintetizar |
| 34 | RAG com Web Scraping | Crawl → chunk → index de páginas web |

### Estado da Arte (35-45)

| # | Tema | Descrição |
|---|------|-----------|
| 35 | Semantic Cache | Cachear respostas por similaridade de embedding |
| 36 | Corrective RAG (CRAG) | Reformular query automaticamente se o retrieval falha |
| 37 | Self-RAG | LLM decide sozinha se precisa buscar ou já sabe responder |
| 38 | HyDE (Hypothetical Document Embeddings) | Gerar documento hipotético para melhorar recall |
| 39 | Late Chunking | Embeddar documento inteiro, depois separar vetores por chunk |
| 40 | Parent Document Retriever | Recuperar chunk pequeno mas retornar documento pai |
| 41 | Tabular RAG | RAG sobre tabelas e dados estruturados |
| 42 | RAG com Código | Indexar repositórios e responder perguntas sobre a codebase |
| 43 | Constitutional AI | LLM que se auto-corrige com princípios |
| 44 | Mixture of Agents | Múltiplos agentes especializados que colaboram |
| 45 | Benchmark Suite | Framework de testes para comparar configurações do pipeline |

### NLP Clássico Avançado (46-55)

| # | Tema | Descrição |
|---|------|-----------|
| 46 | Query Rewriting | Reescrever queries automaticamente para melhorar retrieval |
| 47 | Detecção de Idioma | Identificar a língua do texto automaticamente |
| 48 | Análise de Sentimento | Lexicon-based + ML para classificar polaridade |
| 49 | Topic Modeling (LDA) | Descobrir tópicos latentes em coleções de documentos |
| 50 | Word2Vec do Zero | Implementar word embeddings com skip-gram/CBOW |
| 51 | Attention Mechanism | Implementação manual do mecanismo de atenção |
| 52 | Transformer Decoder (mini-GPT) | Construir um decoder transformer simplificado |
| 53 | Tokenização BPE | Byte Pair Encoding — como GPT tokeniza texto |
| 54 | Sentence Embeddings (mean pooling) | Gerar embedding de sentença a partir de tokens |
| 55 | Cross-Encoder Reranker | Reranking neural com modelo que recebe (query, doc) junto |

### Deep Learning & Training (56-65)

| # | Tema | Descrição |
|---|------|-----------|
| 56 | Contrastive Learning para Embeddings | Treinar embeddings com pares positivos/negativos |
| 57 | Knowledge Distillation | Comprimir modelo grande em modelo pequeno |
| 58 | Multilingual RAG (PT/EN/ES) | RAG que funciona em múltiplos idiomas |
| 59 | Document Q&A com Tabelas | Extrair informação de tabelas em documentos |
| 60 | OCR + NLP | Extrair texto de imagens e processar |
| 61 | Regex Engine do Zero | Implementar um motor de expressões regulares |
| 62 | Finite State Transducer (FST) | Normalização de texto com autômatos |
| 63 | Spell Checker | Correção ortográfica (edit distance + dicionário) |
| 64 | Autocomplete | Sugestão de texto baseada em n-grams e frequência |
| 65 | Text Generation com Markov Chains | Gerar texto com cadeias de Markov |

### Avaliação & Qualidade (66-72)

| # | Tema | Descrição |
|---|------|-----------|
| 66 | Perplexity | Avaliar qualidade de modelos de linguagem |
| 67 | Beam Search | Decodificação com busca em feixe |
| 68 | Chunking Semântico | Dividir por mudança de assunto (não por tamanho) |
| 69 | Citation Verification | Verificar se a resposta cita corretamente o contexto |
| 70 | Adversarial Prompting | Detectar e bloquear prompt injection |
| 71 | Function Calling Schema | Structured output da LLM (JSON garantido) |
| 72 | Reranking Neural Local | Cross-encoder rodando localmente |

### Aplicações & Integração (73-80)

| # | Tema | Descrição |
|---|------|-----------|
| 73 | Recomendação por Texto | Collaborative filtering + similaridade textual |
| 74 | Document Clustering | Agrupar documentos por tema sem labels |
| 75 | Active Learning | Escolher quais exemplos anotar para máximo impacto |
| 76 | Data Augmentation para NLP | Paráfrase, back-translation, synonym replacement |
| 77 | Anonymization (PII) | Detectar e mascarar dados pessoais |
| 78 | Contradiction Detection | Identificar se duas frases se contradizem |
| 79 | Fact Extraction | Extrair triplas sujeito-predicado-objeto |
| 80 | Timeline Extraction | Extrair eventos e ordená-los temporalmente |
