# Exemplo 02 - Normalização de Texto

## O que é Normalização?

Normalização é o processo de **padronizar** os tokens para reduzir variações que não agregam significado. Sem ela, "Python", "python" e "PYTHON" seriam três palavras completamente diferentes para o computador.

Este exemplo aplica três técnicas de normalização em sequência:

1. **Lowercase** — converte tudo para minúsculo
2. **Remoção de Stopwords** — remove palavras sem carga semântica
3. **Stemming** — reduz palavras ao seu radical

## Onde isso é usado?

- Motores de busca — normalizam query e documento para que "Comprar" encontre "compras"
- Classificadores de texto — reduzem o vocabulário para melhorar performance
- Análise de sentimento — "ÓTIMO" e "ótimo" devem ter o mesmo peso
- Sistemas de recomendação — ao comparar descrições de produtos
- Chatbots — normalizam a mensagem do usuário antes de buscar a intenção

## Como funciona neste exemplo

### Lowercase (`LowercaseNormalizer`)

O mais simples dos normalizadores — converte todos os tokens para minúsculo:

```python
lowercase = LowercaseNormalizer()
resultado = lowercase.normalize(["Python", "NLTK", "NLP"])
# ["python", "nltk", "nlp"]
```

**Quando NÃO usar:** quando a capitalização importa (NER precisa saber que "Apple" é diferente de "apple")

### Remoção de Stopwords (`StopwordFilter`)

Remove palavras de alta frequência mas baixo significado semântico. Usa a lista de stopwords em português do NLTK (~200 palavras como "o", "a", "de", "que", "em", "para"):

```python
stopwords = StopwordFilter()
resultado = stopwords.filter(["python", "é", "uma", "linguagem"])
# ["python", "linguagem"]
```

**Por que remover?** Essas palavras aparecem em praticamente todos os textos e não ajudam a distinguir o assunto. Removê-las:
- Reduz o tamanho do vocabulário
- Acelera o processamento
- Melhora a qualidade de métricas como TF-IDF

### Stemming (`Stemmer`)

Reduz palavras à sua raiz morfológica usando o algoritmo RSLP (stemmer específico para português):

```python
stemmer = Stemmer()
resultado = stemmer.stem(["programadores", "programação", "programando"])
# ["program", "program", "program"]
```

**Como funciona o RSLP:**
- Remove sufixos conhecidos do português (-ção, -ando, -mente, -ores, etc.)
- Aplica regras específicas para cada classe de sufixo
- É mais agressivo que lemmatização (pode gerar radicais que não são palavras reais)

## Como rodar

```bash
# Primeira vez: baixar dados do NLTK
uv run python download_nltk.py

# Executar
uv run python main.py
```

## Saída esperada

```
=== TOKENS ORIGINAIS ===
  ['Os', 'programadores', 'estão', 'estudando', 'as', 'linguagens', 'de', 'programação', 'modernas']

=== APÓS LOWERCASE ===
  ['os', 'programadores', 'estão', 'estudando', 'as', 'linguagens', 'de', 'programação', 'modernas']

=== SEM STOPWORDS ===
  ['programadores', 'estudando', 'linguagens', 'programação', 'modernas']
  Removidas: 4 palavras

=== STEMS (RADICAIS) ===
  programadores → program
  estudando → estud
  linguagens → lingu
  programação → program
  modernas → modern
```

## Arquivos do projeto

```
exemplo-02/
├── main.py              # Pipeline: tokenizar → lowercase → stopwords → stem
├── download_nltk.py        # Download dos dados NLTK
├── pyproject.toml       # Dependências (nltk)
└── nltk_nlp/
    ├── tokenizer/
    │   └── tokenizer.py
    └── normalization/
        ├── lowercase.py   # Converte para minúsculo
        ├── stopwords.py   # Remove palavras irrelevantes
        └── stemming.py    # Reduz ao radical (RSLP)
```

## Como evoluir

1. **Implementar lemmatização** — ao invés de cortar sufixos (stemming), usar um dicionário para encontrar a forma base real da palavra ("foi" → "ir", "melhores" → "bom"). Ver `nltk_nlp/linguistic/lemmatization/`
2. **Criar stopwords customizadas** — adicionar ou remover palavras da lista padrão dependendo do domínio (ex: em textos jurídicos, "lei" pode ser stopword)
3. **Adicionar remoção de acentos** — `unicodedata.normalize()` para tratar "programação" e "programacao" como iguais
4. **Normalizar números** — substituir "1.000", "mil", "1000" por um token genérico `<NUM>`
5. **Comparar stemmers** — testar SnowballStemmer vs RSLPStemmer e ver diferenças no resultado
6. **Próximo passo natural** → ir para o **Exemplo 03** que usa esses tokens normalizados para gerar estatísticas
