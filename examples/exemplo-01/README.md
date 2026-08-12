# Exemplo 01 - Tokenização Básica

## O que é Tokenização?

Tokenização é o processo de dividir texto bruto em unidades menores chamadas **tokens**. É o primeiro e mais fundamental passo em qualquer pipeline de NLP, porque computadores não entendem texto — eles precisam de peças discretas para processar.

Existem dois níveis principais de tokenização:

- **Tokenização de sentenças** — divide o texto em frases individuais
- **Tokenização de palavras** — divide cada frase em palavras/símbolos

## Onde isso é usado?

- Motores de busca (Google, Elasticsearch) — tokenizam queries e documentos antes de indexar
- Chatbots e assistentes virtuais — quebram a mensagem do usuário para entender a intenção
- Análise de sentimento — cada token é analisado individualmente
- Tradutores automáticos — a tradução trabalha token a token
- Qualquer aplicação de NLP — é sempre o primeiro passo

## Como funciona neste exemplo

### Tokenizador de Sentenças (`SentenceTokenizer`)

Implementação manual que percorre caractere por caractere procurando pontuação final (`.`, `!`, `?`):

```python
sentence_tokenizer = SentenceTokenizer()
sentences = sentence_tokenizer.tokenize("Olá mundo. Como vai?")
# ["Olá mundo.", "Como vai?"]
```

**Lógica interna:**
1. Acumula caracteres em um buffer
2. Ao encontrar `.`, `!` ou `?`, salva o buffer como sentença
3. Texto restante sem pontuação final é tratado como sentença incompleta

### Tokenizador de Palavras (`Tokenizer`)

Usa o `word_tokenize` do NLTK com suporte a português:

```python
tokenizer = Tokenizer()
tokens = tokenizer.tokenize("Python é incrível!")
# ["Python", "é", "incrível", "!"]
```

**Por que NLTK e não um simples `.split()`?**
- `split()` não separa pontuação: `"incrível!"` seria um token só
- NLTK entende contrações: `"do"` pode ser separado em `"de" + "o"`
- NLTK lida com abreviações: `"Dr."` não é fim de sentença

## Como rodar

```bash
# Primeira vez: baixar dados do NLTK
uv run python download_nltk.py

# Executar
uv run python main.py
```

## Saída esperada

```
=== TOKENIZAÇÃO DE SENTENÇAS ===
  Sentença 1: Python é uma linguagem incrível.
  Sentença 2: Ela facilita o aprendizado de NLP!

=== TOKENIZAÇÃO DE PALAVRAS ===
  Tokens: ['Python', 'é', 'uma', 'linguagem', 'incrível', '.', 'Ela', 'facilita', 'o', 'aprendizado', 'de', 'NLP', '!']
  Total: 13 tokens
```

## Arquivos do projeto

```
exemplo-01/
├── main.py              # Script principal
├── download_nltk.py        # Download dos dados NLTK (punkt)
├── pyproject.toml       # Dependências (nltk)
└── nltk_nlp/
    └── tokenizer/
        ├── tokenizer.py   # Tokenizador de palavras (NLTK)
        └── sentence.py    # Tokenizador de sentenças (manual)
```

## Como evoluir

1. **Adicionar tokenização por regex** — criar um tokenizador que use expressões regulares para lidar com casos especiais (emails, URLs, hashtags)
2. **Tokenizar subpalavras (subword tokenization)** — implementar BPE (Byte Pair Encoding), a técnica usada pelo GPT e BERT para lidar com palavras desconhecidas
3. **Lidar com edge cases** — abreviações ("Sr.", "Dr."), números decimais ("3.14"), reticências ("...")
4. **Comparar com spaCy** — instalar spaCy e comparar a qualidade da tokenização com a do NLTK
5. **Próximo passo natural** → ir para o **Exemplo 02** que normaliza esses tokens (lowercase, stopwords, stemming)
