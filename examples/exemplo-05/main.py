"""
Exemplo 05 - Representação Vetorial (Bag of Words + TF-IDF)

Conceito: Transformar texto em vetores numéricos para que algoritmos
possam "entender" e comparar documentos matematicamente.

- Bag of Words: cada posição do vetor = contagem de uma palavra
- TF-IDF: pondera pela raridade (palavras comuns valem menos)
- Similaridade de cosseno: mede o ângulo entre dois vetores (1 = idênticos)
"""

from nltk_nlp.normalization.lowercase import LowercaseNormalizer
from nltk_nlp.normalization.stopwords import StopwordFilter
from nltk_nlp.tokenizer.tokenizer import Tokenizer
from nltk_nlp.features.bag_of_words import BagOfWords
from nltk_nlp.features.tfidf import TFIDF
from nltk_nlp.similarity.cosine import cosine_similarity


def preprocess(text: str) -> list[str]:
    tokenizer = Tokenizer()
    lowercase = LowercaseNormalizer()
    stopwords = StopwordFilter()
    tokens = tokenizer.tokenize(text)
    normalized = lowercase.normalize(tokens)
    return stopwords.filter(normalized)


def main():
    documents = [
        "Python é uma linguagem de programação",
        "Java também é uma linguagem de programação",
        "O gato dormiu no sofá da sala",
    ]

    # Pré-processar cada documento
    processed = [preprocess(doc) for doc in documents]

    print("=== DOCUMENTOS PRÉ-PROCESSADOS ===")
    for i, tokens in enumerate(processed):
        print(f"  Doc {i+1}: {tokens}")

    # === Bag of Words ===
    print("\n=== BAG OF WORDS ===")
    bow = BagOfWords()
    vocabulary, vectors = bow.fit_transform(processed)

    print(f"  Vocabulário: {vocabulary}")
    for i, vector in enumerate(vectors):
        print(f"  Doc {i+1}: {vector}")

    # === TF-IDF ===
    print("\n=== TF-IDF ===")
    tfidf = TFIDF()
    tfidf_vectors = tfidf.fit_transform(processed)

    print(f"  Vocabulário: {tfidf.vocabulary}")
    for i, vector in enumerate(tfidf_vectors):
        formatted = [f"{v:.3f}" for v in vector]
        print(f"  Doc {i+1}: {formatted}")

    # === Similaridade ===
    print("\n=== SIMILARIDADE DE COSSENO ===")
    sim_12 = cosine_similarity(tfidf_vectors[0], tfidf_vectors[1])
    sim_13 = cosine_similarity(tfidf_vectors[0], tfidf_vectors[2])
    sim_23 = cosine_similarity(tfidf_vectors[1], tfidf_vectors[2])

    print(f"  Doc 1 vs Doc 2 (programação): {sim_12:.4f}")
    print(f"  Doc 1 vs Doc 3 (diferente):   {sim_13:.4f}")
    print(f"  Doc 2 vs Doc 3 (diferente):   {sim_23:.4f}")
    print()
    print("  → Documentos sobre programação são mais similares entre si!")


if __name__ == "__main__":
    main()
