# Exemplo 03 - Estatísticas e Vocabulário

## O que é Análise Estatística de Texto?

Depois de tokenizar e normalizar, o próximo passo é **quantificar** o texto. Estatísticas de frequência revelam quais palavras dominam um documento, quão rico é o vocabulário, e qual é a distribuição dos termos.

Esses números são a ponte entre texto e matemática — a base para tudo que vem depois (TF-IDF, classificadores, embeddings).

## Onde isso é usado?

- SEO e marketing — identificar palavras-chave mais frequentes em um nicho
- Detecção de autoria — cada autor tem uma distribuição de vocabulário única
- Resumo automático — palavras mais frequentes indicam o tema principal
- Pré-processamento para ML — entender a distribuição ajuda a decidir thresholds
- Monitoramento de redes sociais — palavras em tendência (trending)
- Linguística computacional — medir riqueza lexical de um texto

## Como funciona neste exemplo

### Contagem de Frequência (`FrequencyCounter`)

Conta quantas vezes cada token aparece no texto:

```python
frequency = FrequencyCounter()
frequencies = frequency.count(["python", "é", "python", "bom"])
# {"python": 2, "é": 1, "bom": 1}

# Top N mais comuns:
most_common = frequency.most_common(tokens, limit=5)
# [("python", 4), ("linguagem", 2), ...]
```

**Implementação interna:** usa um dicionário simples com `.get(token, 0) + 1` — sem dependências externas.

### Vocabulário (`Vocabulary`)

Extrai o conjunto de palavras únicas (sem repetição):

```python
vocab = Vocabulary()
unique = vocab.build(["python", "é", "python", "bom"])
# {"python", "é", "bom"}

size = vocab.size(["python", "é", "python", "bom"])
# 3
```

**Por que importa?** O tamanho do vocabulário define a dimensionalidade dos vetores em BoW e TF-IDF. Um vocabulário de 10.000 palavras = vetores de 10.000 dimensões.

## Conceitos importantes

### Lei de Zipf

A distribuição de frequência de palavras segue uma lei de potência: poucas palavras aparecem muitas vezes, e muitas palavras aparecem poucas vezes. Isso explica por que remover stopwords é tão eficiente — as palavras mais frequentes geralmente são as menos informativas.

### Type-Token Ratio (TTR)

Uma métrica de riqueza lexical: `vocabulário / total_tokens`. Um TTR alto indica texto variado; TTR baixo indica repetição.

## Como rodar

```bash
uv run python download_nltk.py   # primeira vez
uv run python main.py
```

## Saída esperada

```
=== FREQUÊNCIA DE PALAVRAS ===
  python          ████ (4)
  .               ████ (4)
  linguagem       ██ (2)
  programação     ██ (2)
  usada           █ (1)
  ...

=== TOP 5 MAIS COMUNS ===
  python: 4x
  .: 4x
  linguagem: 2x
  programação: 2x
  usada: 1x

=== VOCABULÁRIO ===
  Tamanho: 10 palavras únicas
  Palavras: ['.', 'ciência', 'dados', 'linguagem', ...]
```

## Arquivos do projeto

```
exemplo-03/
├── main.py              # Pipeline completo + estatísticas
├── download_nltk.py
├── pyproject.toml
└── nltk_nlp/
    ├── tokenizer/
    │   └── tokenizer.py
    ├── normalization/
    │   ├── lowercase.py
    │   └── stopwords.py
    └── statistics/
        ├── frequency.py    # Contagem + most_common
        └── vocabulary.py   # Palavras únicas + size
```

## Como evoluir

1. **Calcular Type-Token Ratio** — adicionar método `ttr()` ao Vocabulary para medir riqueza lexical
2. **Gerar gráficos** — usar matplotlib para plotar distribuição de frequência (curva de Zipf)
3. **Comparar documentos** — calcular estatísticas para múltiplos textos e comparar perfis
4. **Implementar frequência relativa** — normalizar contagem pelo total de tokens (base para TF)
5. **Adicionar frequência por documento** — contar em quantos documentos cada palavra aparece (base para IDF)
6. **Word clouds** — gerar nuvens de palavras onde o tamanho é proporcional à frequência
7. **Próximo passo natural** → ir para o **Exemplo 04** que adiciona análise estrutural (POS, NER, N-grams) aos tokens
