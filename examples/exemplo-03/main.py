"""
Exemplo 03 - Estatísticas e Vocabulário

Conceito: Analisar a frequência e distribuição das palavras.
- Contagem de frequência (quantas vezes cada palavra aparece)
- Vocabulário (palavras únicas)
- Palavras mais comuns

Isso é a base para entender a distribuição de um corpus e
depois construir representações numéricas (vetores).
"""

from nltk_nlp.tokenizer.tokenizer import Tokenizer
from nltk_nlp.normalization.lowercase import LowercaseNormalizer
from nltk_nlp.normalization.stopwords import StopwordFilter
from nltk_nlp.statistics.frequency import FrequencyCounter
from nltk_nlp.statistics.vocabulary import Vocabulary


def main():
    text = (
        "Python é uma linguagem de programação. "
        "Python é usada para ciência de dados. "
        "A linguagem Python é simples e poderosa. "
        "Programação em Python é produtiva."
    )

    # Pipeline de pré-processamento
    tokenizer = Tokenizer()
    lowercase = LowercaseNormalizer()
    stopwords = StopwordFilter()

    tokens = tokenizer.tokenize(text)
    normalized = lowercase.normalize(tokens)
    filtered = stopwords.filter(normalized)

    print("=== TOKENS FILTRADOS ===")
    print(f"  {filtered}")

    # Frequência
    frequency = FrequencyCounter()
    frequencies = frequency.count(filtered)

    print("\n=== FREQUÊNCIA DE PALAVRAS ===")
    for word, count in sorted(frequencies.items(), key=lambda x: x[1], reverse=True):
        bar = "█" * count
        print(f"  {word:15} {bar} ({count})")

    # Top 5 mais comuns
    most_common = frequency.most_common(filtered, limit=5)
    print("\n=== TOP 5 MAIS COMUNS ===")
    for word, count in most_common:
        print(f"  {word}: {count}x")

    # Vocabulário
    vocab = Vocabulary()
    unique_words = vocab.build(filtered)
    print(f"\n=== VOCABULÁRIO ===")
    print(f"  Tamanho: {vocab.size(filtered)} palavras únicas")
    print(f"  Palavras: {sorted(unique_words)}")


if __name__ == "__main__":
    main()
