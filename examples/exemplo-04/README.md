# Exemplo 04 - Análise Linguística (POS Tagging, NER, N-grams)

## O que é Análise Linguística?

Além de contar palavras, podemos extrair **estrutura** do texto: qual é a função de cada palavra na frase? Existem nomes de pessoas, lugares ou valores? Quais palavras costumam aparecer juntas?

Este exemplo implementa três técnicas:

- **POS Tagging** — Part-of-Speech, classificar cada palavra por função gramatical
- **NER** — Named Entity Recognition, identificar entidades nomeadas
- **N-grams** — sequências de N palavras consecutivas

## Onde isso é usado?

### POS Tagging
- Tradução automática — a ordem das classes gramaticais muda entre idiomas
- Desambiguação — "banco" é verbo ou substantivo?
- Extração de informação — encontrar todos os verbos de ação
- Geração de texto — manter a estrutura gramatical coerente

### NER
- Chatbots financeiros — extrair valores monetários de mensagens
- Assistentes pessoais — identificar datas, horários, locais
- Compliance — detectar CPF, CNPJ, dados sensíveis
- Jornalismo — extrair nomes de pessoas e organizações de notícias

### N-grams
- Corretor ortográfico — sugerir a próxima palavra baseado no bigrama anterior
- Detecção de plágio — comparar sequências de n-grams entre documentos
- Geração de texto — modelos de linguagem simples baseados em n-grams
- Análise de sentimento — "não gostei" (bigrama negativo) vs "gostei" (unigrama positivo)

## Como funciona neste exemplo

### POS Tagger Manual (`ManualPOSTagger`)

Classificador baseado em regras com listas de palavras por categoria:

```python
pos_tagger = ManualPOSTagger()
tags = pos_tagger.tag(["Eu", "quero", "comprar"])
# [("Eu", "PRON"), ("quero", "VERB"), ("comprar", "VERB")]
```

**Categorias implementadas:**
- `VERB` — verbos conhecidos (sou, é, quero, comprar, pagar, etc.)
- `DET` — artigos (o, a, um, uma, os, as)
- `PRON` — pronomes (eu, ele, nós, vocês)
- `PROPN` — nomes próprios (palavras com maiúscula)
- `NOUN` — tudo que não encaixa nas categorias acima

### NER Manual (`ManualNER`)

Extrai entidades usando expressões regulares:

```python
ner = ManualNER()
entities = ner.extract("Paguei R$ 3.500,00 no notebook")
# [{"text": "R$ 3.500,00", "type": "MONEY", "start": 7, "end": 18}]
```

**Pattern implementado:** valores monetários no formato `R$ X.XXX,XX`

### N-gram Generator (`NGramGenerator`)

Gera sequências de N palavras consecutivas:

```python
ngram = NGramGenerator()
ngram.bigram(["python", "machine", "learning"])
# [("python", "machine"), ("machine", "learning")]

ngram.trigram(["python", "machine", "learning", "ia"])
# [("python", "machine", "learning"), ("machine", "learning", "ia")]
```

**Algoritmo:** janela deslizante de tamanho N sobre a lista de tokens.

## Como rodar

```bash
uv run python download_nltk.py   # primeira vez
uv run python main.py
```

## Saída esperada

```
=== POS TAGGING (CLASSES GRAMATICAIS) ===
  Eu              → PRON
  quero           → VERB
  comprar         → VERB
  um              → DET
  notebook        → NOUN
  ...

=== NER (ENTIDADES NOMEADAS) ===
  [MONEY] "R$ 3.500,00" (posição 33:44)

=== N-GRAMS ===
  Bigramas:
    ('quero', 'comprar')
    ('comprar', 'notebook')
    ...
```

## Arquivos do projeto

```
exemplo-04/
├── main.py
├── download_nltk.py
├── pyproject.toml
└── nltk_nlp/
    ├── tokenizer/
    │   └── tokenizer.py
    ├── normalization/
    │   ├── lowercase.py
    │   └── stopwords.py
    └── linguistic/
        ├── pos/
        │   └── manual.py      # POS tagger baseado em regras
        ├── ner/
        │   └── manual.py      # NER por regex (R$)
        └── ngrams/
            └── manual.py      # Gerador de n-grams
```

## Como evoluir

1. **Expandir o NER** — adicionar patterns para CPF (`\d{3}\.\d{3}\.\d{3}-\d{2}`), datas (`\d{2}/\d{2}/\d{4}`), emails, telefones
2. **POS Tagger estatístico** — treinar um Hidden Markov Model (HMM) com um corpus anotado ao invés de usar listas fixas
3. **N-grams com probabilidade** — calcular P(palavra | contexto) para criar um modelo de linguagem simples
4. **Collocations** — identificar bigramas que aparecem juntos com frequência anormal (ex: "machine learning", "inteligência artificial")
5. **Dependency parsing** — ir além do POS e entender as relações entre palavras ("quero" → objeto → "notebook")
6. **Usar spaCy** — comparar os resultados manuais com um modelo treinado (`spacy.load("pt_core_news_sm")`)
7. **Próximo passo natural** → ir para o **Exemplo 05** que transforma esses tokens em vetores numéricos
