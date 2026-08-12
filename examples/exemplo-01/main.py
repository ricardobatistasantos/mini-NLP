"""
Exemplo 01 - Tokenização Básica

Conceito: Transformar texto em unidades menores (tokens).
- Tokenização de palavras (word_tokenize)
- Tokenização de sentenças (manual)

Este é o primeiro passo de qualquer pipeline NLP:
quebrar o texto bruto em peças manipuláveis.
"""

from nltk_nlp.tokenizer.tokenizer import Tokenizer
from nltk_nlp.tokenizer.sentence import SentenceTokenizer


def main():
    text = "Python é uma linguagem incrível. Ela facilita o aprendizado de NLP!"

    # Tokenização de sentenças
    sentence_tokenizer = SentenceTokenizer()
    sentences = sentence_tokenizer.tokenize(text)

    print("=== TOKENIZAÇÃO DE SENTENÇAS ===")
    for i, sentence in enumerate(sentences, 1):
        print(f"  Sentença {i}: {sentence}")

    # Tokenização de palavras
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)

    print("\n=== TOKENIZAÇÃO DE PALAVRAS ===")
    print(f"  Tokens: {tokens}")
    print(f"  Total: {len(tokens)} tokens")


if __name__ == "__main__":
    main()
