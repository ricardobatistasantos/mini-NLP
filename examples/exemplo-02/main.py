"""
Exemplo 02 - Normalização de Texto

Conceito: Reduzir variações do texto para uniformizar o processamento.
- Lowercase (tudo minúsculo)
- Remoção de stopwords (palavras sem significado: "o", "a", "de", "que")
- Stemming (reduzir ao radical: "comprando" → "compr")

Sem normalização, "Python" e "python" seriam tratadas como palavras diferentes.
"""

from nltk_nlp.tokenizer.tokenizer import Tokenizer
from nltk_nlp.normalization.lowercase import LowercaseNormalizer
from nltk_nlp.normalization.stopwords import StopwordFilter
from nltk_nlp.normalization.stemming import Stemmer


def main():
    text = "Os programadores estão estudando as linguagens de programação modernas"

    # 1. Tokenizar
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)
    print("=== TOKENS ORIGINAIS ===")
    print(f"  {tokens}")

    # 2. Lowercase
    lowercase = LowercaseNormalizer()
    normalized = lowercase.normalize(tokens)
    print("\n=== APÓS LOWERCASE ===")
    print(f"  {normalized}")

    # 3. Remover stopwords
    stopwords = StopwordFilter()
    filtered = stopwords.filter(normalized)
    print("\n=== SEM STOPWORDS ===")
    print(f"  {filtered}")
    print(f"  Removidas: {len(normalized) - len(filtered)} palavras")

    # 4. Stemming
    stemmer = Stemmer()
    stems = stemmer.stem(filtered)
    print("\n=== STEMS (RADICAIS) ===")
    for word, stem in zip(filtered, stems):
        print(f"  {word} → {stem}")


if __name__ == "__main__":
    main()
