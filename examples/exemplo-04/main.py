"""
Exemplo 04 - Análise Linguística (POS Tagging, NER, N-grams)

Conceito: Entender a estrutura do texto além das palavras isoladas.
- POS Tagging: identificar classe gramatical (verbo, substantivo, etc.)
- NER: reconhecer entidades nomeadas (dinheiro, nomes, etc.)
- N-grams: sequências de N palavras consecutivas

Estas são técnicas fundamentais de linguística computacional.
"""

from nltk_nlp.tokenizer.tokenizer import Tokenizer
from nltk_nlp.normalization.lowercase import LowercaseNormalizer
from nltk_nlp.normalization.stopwords import StopwordFilter
from nltk_nlp.linguistic.pos.manual import ManualPOSTagger
from nltk_nlp.linguistic.ner.manual import ManualNER
from nltk_nlp.linguistic.ngrams.manual import NGramGenerator


def main():
    text = "Eu quero comprar um notebook por R$ 3.500,00 para estudar Python"

    # Tokenizar
    tokenizer = Tokenizer()
    tokens = tokenizer.tokenize(text)

    # === POS Tagging ===
    print("=== POS TAGGING (CLASSES GRAMATICAIS) ===")
    pos_tagger = ManualPOSTagger()
    pos_tags = pos_tagger.tag(tokens)
    for token, tag in pos_tags:
        print(f"  {token:15} → {tag}")

    # === NER ===
    print("\n=== NER (ENTIDADES NOMEADAS) ===")
    ner = ManualNER()
    entities = ner.extract(text)
    if entities:
        for entity in entities:
            print(f"  [{entity['type']}] \"{entity['text']}\" (posição {entity['start']}:{entity['end']})")
    else:
        print("  Nenhuma entidade encontrada")

    # === N-grams ===
    print("\n=== N-GRAMS ===")
    # Pré-processar para n-grams
    lowercase = LowercaseNormalizer()
    stopwords = StopwordFilter()
    filtered = stopwords.filter(lowercase.normalize(tokens))

    ngram_generator = NGramGenerator()

    bigrams = ngram_generator.bigram(filtered)
    print("  Bigramas:")
    for bigram in bigrams:
        print(f"    {bigram}")

    trigrams = ngram_generator.trigram(filtered)
    print("\n  Trigramas:")
    for trigram in trigrams:
        print(f"    {trigram}")


if __name__ == "__main__":
    main()
