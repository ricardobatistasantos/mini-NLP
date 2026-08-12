# Exemplo 05 - Representação Vetorial (Bag of Words + TF-IDF)

## O que é Representação Vetorial?

Computadores trabalham com números, não com texto. Para que algoritmos possam comparar, classificar ou buscar documentos, precisamos transformar texto em **vetores numéricos**.

Este exemplo implementa duas abordagens clássicas:

- **Bag of Words (BoW)** — cada dimensão = contagem de uma palavra
- **TF-IDF** — pondera pela importância relativa (palavras raras valem mais)
- **Similaridade de Cosseno** — mede quão parecidos dois vetores são

## Onde isso é usado?

- Motores de busca (Elasticsearch, Solr) — indexam documentos como vetores TF-IDF
- Classificação de spam — representa emails como vetores e treina um classificador
- Sistemas de recomendação — compara descrições de produtos por similaridade
- Clustering de documentos — agrupa textos similares automaticamente
- Detecção de duplicatas — documentos com alta similaridade de cosseno são provavelmente duplicados

## Como funciona neste exemplo

### Bag of Words (`BagOfWords`)

Cria um vocabulário global e representa cada documento como vetor de contagens:

```python
bow = BagOfWords()
vocabulary, vectors = bow.fit_transform([
    ["python", "linguagem"],
    ["java", "linguagem"],
])
# vocabulary: {"java": 0, "linguagem": 1, "python": 2}
# vectors: [[0, 1, 1], [1, 1, 0]]
```

**Limitação:** todas as palavras têm o mesmo peso. "linguagem" aparece em ambos documentos mas conta igual a "python" que é específico.

### TF-IDF (`TFIDF`)

Resolve a limitação do BoW ponderando cada termo por sua raridade no corpus:

```
TF-IDF(t, d) = TF(t, d) × IDF(t)

TF(t, d) = frequência do termo t no documento d / total de termos em d
IDF(t) = log(total de documentos / documentos que contêm t)
```

```python
tfidf = TFIDF()
vectors = tfidf.fit_transform([
    ["python", "linguagem", "programação"],
    ["java", "linguagem", "programação"],
    ["gato", "dormiu", "sofá"],
])
```

**Resultado:** "linguagem" e "programação" recebem peso baixo (aparecem em 2 de 3 docs), enquanto "python" e "java" recebem peso alto (aparecem em apenas 1 doc).

### Similaridade de Cosseno

Mede o ângulo entre dois vetores (ignora magnitude, foca na direção):

```python
from nltk_nlp.similarity.cosine import cosine_similarity

score = cosine_similarity([1, 0, 1], [1, 0, 0])
# 0.707 (similares)

score = cosine_similarity([1, 0, 0], [0, 1, 0])
# 0.0 (completamente diferentes)
```

**Escala:** 0 = nenhuma similaridade, 1 = idênticos

## Como rodar

```bash
uv run python download_nltk.py   # primeira vez
uv run python main.py
```

## Saída esperada

```
=== BAG OF WORDS ===
  Vocabulário: {'dormiu': 0, 'gato': 1, 'java': 2, 'linguagem': 3, ...}
  Doc 1: [0, 0, 0, 1, 1, 1, 0, 0]
  Doc 2: [0, 0, 1, 1, 1, 0, 0, 0]
  Doc 3: [1, 1, 0, 0, 0, 0, 1, 1]

=== TF-IDF ===
  Doc 1: ['0.000', '0.000', '0.000', '0.135', '0.135', '0.366', ...]

=== SIMILARIDADE DE COSSENO ===
  Doc 1 vs Doc 2 (programação): 0.2141
  Doc 1 vs Doc 3 (diferente):   0.0000
  → Documentos sobre programação são mais similares entre si!
```

## Arquivos do projeto

```
exemplo-05/
├── main.py
├── download_nltk.py
├── pyproject.toml
└── nltk_nlp/
    ├── tokenizer/
    │   └── tokenizer.py
    ├── normalization/
    │   ├── lowercase.py
    │   └── stopwords.py
    ├── features/
    │   ├── bag_of_words.py   # BoW: vocabulário + vetorização
    │   ├── tf.py             # Term Frequency
    │   ├── idf.py            # Inverse Document Frequency
    │   └── tfidf.py          # TF-IDF combinado
    └── similarity/
        └── cosine.py         # Similaridade de cosseno
```

## Como evoluir

1. **Adicionar distância euclidiana e Manhattan** — implementar outras métricas de distância e comparar com cosseno
2. **N-grams como features** — ao invés de apenas unigramas, incluir bigramas no vocabulário ("machine learning" como um token)
3. **Limitar vocabulário** — implementar `max_features` para usar apenas os N termos mais frequentes (reduz dimensionalidade)
4. **Normalização L2** — normalizar vetores TF-IDF para que todos tenham magnitude 1
5. **Visualizar com PCA** — reduzir vetores para 2D com PCA e plotar documentos no espaço
6. **Comparar com sklearn** — ver como `TfidfVectorizer` do scikit-learn se comporta vs sua implementação
7. **Próximo passo natural** → ir para o **Exemplo 06** que usa esses vetores para classificação de texto
