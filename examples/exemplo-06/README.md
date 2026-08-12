# Exemplo 06 - Classificação de Texto (Naive Bayes)

## O que é Classificação de Texto?

Classificação é o problema de atribuir automaticamente uma **categoria** (label) a um documento. É uma das tarefas mais comuns em NLP: dado um texto, qual é a sua classe?

Este exemplo implementa **Naive Bayes** do zero — um classificador probabilístico simples mas surpreendentemente eficaz.

## Onde isso é usado?

- Filtro de spam — classificar emails como "spam" ou "não spam"
- Roteamento de tickets — direcionar chamados para o time correto (financeiro, suporte, etc.)
- Análise de sentimento — classificar reviews como "positivo", "negativo", "neutro"
- Categorização de notícias — esportes, política, tecnologia, etc.
- Detecção de idioma — qual língua é esse texto?
- Triagem médica — classificar sintomas por urgência

## Como funciona neste exemplo

### Naive Bayes - A Teoria

O classificador usa o Teorema de Bayes para calcular a probabilidade de cada classe dado um documento:

```
P(classe | documento) ∝ P(classe) × P(palavra₁ | classe) × P(palavra₂ | classe) × ...
```

**"Naive" (ingênuo)** porque assume que as palavras são independentes entre si — o que raramente é verdade, mas funciona bem na prática.

### Treinamento (`fit`)

```python
classifier = NaiveBayes()
classifier.fit(
    documents=[["pagar", "boleto"], ["erro", "sistema"]],
    labels=["financeiro", "suporte"],
)
```

**O que acontece internamente:**
1. Conta quantos documentos pertencem a cada classe → P(classe)
2. Conta quantas vezes cada palavra aparece em cada classe → P(palavra | classe)
3. Armazena o vocabulário total para suavização

### Predição (`predict`)

```python
prediction = classifier.predict(["pagar", "conta"])
# "financeiro"
```

**O que acontece internamente:**
1. Para cada classe, calcula: `log P(classe) + Σ log P(palavra | classe)`
2. Usa **suavização de Laplace** (+1) para evitar probabilidade zero em palavras nunca vistas
3. Retorna a classe com maior probabilidade

### Suavização de Laplace

Se uma palavra nunca apareceu em uma classe, P(palavra | classe) = 0, e toda a multiplicação zera. Laplace resolve:

```
P(palavra | classe) = (contagem + 1) / (total_palavras_classe + tamanho_vocabulário)
```

## Como rodar

```bash
uv run python download_nltk.py   # primeira vez
uv run python main.py
```

## Saída esperada

```
=== CLASSIFICADOR NAIVE BAYES ===
  Classes: ['cancelamento', 'financeiro', 'suporte']
  Vocabulário: 35 palavras

=== PREVISÕES ===
  "Quero verificar meu extrato bancário"
    → financeiro

  "O app está dando erro ao abrir"
    → suporte

  "Não quero mais pagar esse plano"
    → cancelamento
```

## Arquivos do projeto

```
exemplo-06/
├── main.py              # Treino e previsão
├── download_nltk.py
├── pyproject.toml
└── nltk_nlp/
    ├── tokenizer/
    │   └── tokenizer.py
    ├── normalization/
    │   ├── lowercase.py
    │   └── stopwords.py
    └── ml/
        └── naive_bayes.py   # Implementação completa do classificador
```

## Como evoluir

1. **Calcular accuracy** — separar dados em treino/teste e medir % de acertos
2. **Matriz de confusão** — visualizar quais classes estão sendo confundidas
3. **Adicionar mais dados** — quanto mais exemplos de treino, melhor a classificação
4. **Implementar TF-IDF como features** — ao invés de contagem, usar pesos TF-IDF para calcular probabilidades
5. **Implementar Log-Likelihood Ratio** — identificar quais palavras são mais discriminativas para cada classe
6. **Multi-label** — permitir que um documento pertença a múltiplas classes
7. **Comparar com sklearn** — `from sklearn.naive_bayes import MultinomialNB` e comparar resultados
8. **Próximo passo natural** → ir para o **Exemplo 07** que usa ranqueamento (BM25) para encontrar documentos relevantes
