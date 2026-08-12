# Exemplo 10 - RAG (Retrieval-Augmented Generation)

## O que é RAG?

RAG (Retrieval-Augmented Generation) é o padrão que permite uma LLM responder perguntas baseando-se em **documentos externos**, sem precisar ter sido treinada neles. É a arquitetura por trás de:

- ChatGPT com upload de PDFs
- Perplexity AI (busca + resposta)
- GitHub Copilot (contexto do repositório)
- Assistentes corporativos que consultam bases de conhecimento internas

## O problema que RAG resolve

LLMs têm duas limitações:
1. **Corte de conhecimento** — não sabem nada após a data de treino
2. **Alucinação** — inventam respostas quando não sabem

RAG resolve ambos: busca informação atualizada em documentos e força o modelo a responder **apenas com base no contexto encontrado**.

## Onde isso é usado?

- Chatbots de atendimento — respondem baseados na FAQ/documentação da empresa
- Assistentes jurídicos — consultam contratos e legislação
- Suporte técnico — buscam em manuais e troubleshooting guides
- Pesquisa acadêmica — sintetizam informação de múltiplos papers
- Documentação interna — permitem perguntar sobre processos da empresa

## Como funciona neste exemplo

### Pipeline RAG completo

```
┌─────────────────────────────────────────────────────────┐
│ INGESTÃO (offline, uma vez)                              │
│                                                          │
│ Documento → Chunking → Embedding → Vector Store          │
└─────────────────────────────────────────────────────────┘

┌─────────────────────────────────────────────────────────┐
│ CONSULTA (runtime, por pergunta)                         │
│                                                          │
│ Query → Embedding → Busca → Chunks relevantes            │
│                                     ↓                    │
│                              Contexto montado            │
│                                     ↓                    │
│                              Prompt construído           │
│                                     ↓                    │
│                              LLM → Resposta             │
└─────────────────────────────────────────────────────────┘
```

### 1. Chunking (`TextChunker`)

Divide o documento em pedaços menores com overlap:

```python
chunker = TextChunker(chunk_size=15, overlap=3)
chunks = chunker.split(document)
```

**Por que chunking?**
- Embeddings têm limite de tokens (geralmente 512)
- Chunks menores = busca mais precisa (retorna trecho relevante, não o documento inteiro)
- Overlap garante que informação na fronteira entre chunks não se perca

**Parâmetros:**
- `chunk_size=15` — cada chunk tem no máximo 15 palavras
- `overlap=3` — os últimos 3 tokens de um chunk aparecem no início do próximo

### 2. Indexação (`RAGIndexer`)

Para cada chunk, gera embedding e armazena no vector store:

```python
indexer = RAGIndexer(embedding_model, vector_store)
indexer.index_chunks(chunks)
```

### 3. Retrieval (`Retriever`)

Dado uma pergunta, encontra os chunks mais relevantes:

```python
retriever = Retriever(embedding_model, vector_store)
chunks = retriever.retrieve("Para que serve Python?", top_k=3)
```

### 4. Contexto (`ContextBuilder`)

Monta uma string formatada com os chunks recuperados:

```python
context_builder = ContextBuilder()
context = context_builder.build(chunks)
# "[Contexto 1]\nPython é usado para...\n\n[Contexto 2]\n..."
```

### 5. Prompt (`PromptBuilder`)

Constrói o prompt final para a LLM com instruções, contexto e pergunta:

```python
prompt_builder = PromptBuilder()
prompt = prompt_builder.build(query="...", context="...")
```

**Template do prompt:**
```
Você é um assistente que responde perguntas
utilizando exclusivamente o contexto fornecido.
Se a resposta não estiver presente no contexto,
diga que não encontrou informação suficiente.
Não invente informações.

CONTEXTO:
[chunks recuperados]

PERGUNTA:
[pergunta do usuário]

RESPOSTA:
```

### 6. Geração (`Generator`)

O MockGenerator simula a resposta. Em produção, use `OllamaGenerator`:

```python
# Mock (este exemplo):
generator = MockGenerator()

# Produção (com Ollama rodando localmente):
from nltk_nlp.rag.ollama_generator import OllamaGenerator
generator = OllamaGenerator(model="llama3")
```

### Tudo junto (`RAGPipeline`)

```python
rag = RAGPipeline(
    embedding_model=embedding_model,
    vector_store=vector_store,
    generator=generator,
    chunker=chunker,
)

# Ingerir documento
rag.ingest(document)

# Perguntar
result = rag.ask("Para que Python é utilizada?")
print(result["answer"])
```

## Como rodar

```bash
uv run python main.py
```

## Saída esperada

```
=== 1. INGESTÃO (Chunking) ===
  Chunk 0: "Python é uma linguagem de programação de alto níve..."
  Chunk 1: "van Rossum. Ela é muito utilizada para ciência de ..."
  ...
  Total chunks: 7
  Vetores armazenados: 7

=== 2. RAG - PERGUNTAR ===
  Pergunta: "Para que Python é utilizada?"
  Chunks recuperados: 2
    1. [0.4104] "frameworks mais usados são Django e FastAPI. Pytho..."
    2. [0.3464] "van Rossum. Ela é muito utilizada para ciência de ..."
  Resposta: [Resposta baseada em 213 chars de contexto]
```

## Arquivos do projeto

```
exemplo-10/
├── main.py
├── pyproject.toml          # Dependência: requests (para Ollama)
└── nltk_nlp/
    ├── embeddings/
    │   ├── base.py            # Classe abstrata EmbeddingModel
    │   ├── hash_embedding.py  # Embedding por hash (didático)
    │   └── similarity.py      # Cosseno
    ├── vector_store/
    │   ├── models.py          # VectorRecord, SearchResult
    │   ├── vector_store.py    # ABC
    │   ├── distance.py
    │   ├── filters.py
    │   └── memory_store.py    # Armazenamento em memória
    └── rag/
        ├── models.py          # Document, Chunk, RetrievedChunk
        ├── loader.py          # Carrega documentos de texto/arquivo
        ├── chunker.py         # Divide em chunks com overlap
        ├── indexer.py         # Gera embeddings e armazena
        ├── retriever.py       # Busca chunks por similaridade
        ├── context.py         # Monta contexto formatado
        ├── prompt.py          # Constrói prompt para LLM
        ├── generator.py       # ABC para geradores
        ├── mock_generator.py  # Simula resposta (sem LLM)
        ├── ollama_generator.py # Gerador real via Ollama API
        ├── retrieval_adapter.py # Adapta RetrievalPipeline para RAG
        └── pipeline.py        # Orquestra todo o fluxo
```

## Como usar com LLM real (Ollama)

1. Instale o Ollama: https://ollama.ai
2. Baixe um modelo: `ollama pull llama3`
3. No código, troque o generator:

```python
from nltk_nlp.rag.ollama_generator import OllamaGenerator
generator = OllamaGenerator(model="llama3")
```

## Como evoluir

1. **Usar embeddings reais** — trocar HashEmbedding por `OllamaEmbedding(model="nomic-embed-text")` para capturar semântica de verdade
2. **Chunking inteligente** — dividir por parágrafos ou seções ao invés de contagem de palavras (ver `documents/chunkers/`)
3. **Retrieval híbrido** — usar `RetrievalAdapter` para combinar BM25 + vetorial (exemplo 09) como retriever do RAG
4. **Múltiplos documentos** — ingerir vários arquivos e buscar entre todos
5. **Streaming** — implementar geração com streaming para UX mais responsiva
6. **Evaluation** — medir qualidade com métricas como RAGAS (faithfulness, relevancy, context_recall)
7. **Chat com memória** — manter histórico de conversas e usar como contexto adicional
8. **Guardrails** — adicionar verificação de alucinação (a resposta está fundamentada no contexto?)
9. **Ingestão de arquivos** — usar `documents/loaders/` para carregar PDFs, CSVs, JSONs automaticamente
10. **Deploy** — empacotar como API com FastAPI para servir o RAG como microserviço
