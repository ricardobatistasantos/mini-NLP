# from nltk_nlp.tokenizer.tokenizer import Tokenizer

# tokenizer = Tokenizer()

# teste = tokenizer.tokenize("Quero pagar meu boleto amanhã.")

# print(teste)

from nltk_nlp.pipeline.pipeline import NLPPipeline

def main() -> None:
  pipeline = NLPPipeline()

  text = input("Digite um texto: ")

  result = pipeline.process(text)

  print("\nTexto:")
  print(result.original_text)

  print("\nTokens:")
  print(result.tokens)

  print("\nTokens normalizados:")
  print(result.normalized_tokens)

  print("\nStems:")
  print(result.stems)


if __name__ == "__main__":
    main()