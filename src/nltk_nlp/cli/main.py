from nltk_nlp.pipeline.pipeline import NLPPipeline


def main() -> None:
    pipeline = NLPPipeline()

    text = input("Digite um texto: ")

    result = pipeline.process(text)

    print("\nTexto:")
    print(result["original"])

    print("\nSentenças:")
    print(result["sentences"])

    print("\nTokens:")
    print(result["tokens"])

    print("\nTokens normalizados:")
    print(result["normalized"])

    print("\nSem stopwords:")
    print(result["without_stopwords"])

    print("\nStems:")
    print(result["stems"])

    print("\nFrequências:")
    print(result["frequencies"])

    print("\nVocabulário:")
    print(result["vocabulary"])
