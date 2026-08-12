"""
Exemplo 06 - Classificação de Texto (Naive Bayes)

Conceito: Ensinar uma máquina a categorizar textos automaticamente.
- Treinar com documentos rotulados
- Prever a categoria de textos novos

Usa Naive Bayes — um classificador probabilístico simples mas eficiente.
Aplica suavização de Laplace para evitar probabilidade zero.
"""

from nltk_nlp.tokenizer.tokenizer import Tokenizer
from nltk_nlp.normalization.lowercase import LowercaseNormalizer
from nltk_nlp.normalization.stopwords import StopwordFilter
from nltk_nlp.ml.naive_bayes import NaiveBayes


def preprocess(text: str) -> list[str]:
    tokenizer = Tokenizer()
    lowercase = LowercaseNormalizer()
    stopwords = StopwordFilter()
    tokens = tokenizer.tokenize(text)
    normalized = lowercase.normalize(tokens)
    return stopwords.filter(normalized)


def main():
    # Dados de treino
    training_data = [
        ("Preciso pagar o boleto do cartão de crédito", "financeiro"),
        ("Qual o saldo da minha conta corrente", "financeiro"),
        ("Quero fazer uma transferência bancária", "financeiro"),
        ("Meu pagamento não foi processado", "financeiro"),
        ("Preciso de suporte técnico para o computador", "suporte"),
        ("Meu sistema está com erro na tela", "suporte"),
        ("O aplicativo travou e não abre mais", "suporte"),
        ("Como resetar a minha senha de acesso", "suporte"),
        ("Quero cancelar minha assinatura do plano", "cancelamento"),
        ("Gostaria de encerrar minha conta", "cancelamento"),
        ("Não quero mais o serviço mensal", "cancelamento"),
        ("Como faço para cancelar o plano premium", "cancelamento"),
    ]

    # Pré-processar e separar
    documents = [preprocess(text) for text, _ in training_data]
    labels = [label for _, label in training_data]

    # Treinar
    classifier = NaiveBayes()
    classifier.fit(documents, labels)

    print("=== CLASSIFICADOR NAIVE BAYES ===")
    print(f"  Classes: {sorted(classifier.classes)}")
    print(f"  Vocabulário: {len(classifier.vocabulary)} palavras")

    # Prever textos novos
    print("\n=== PREVISÕES ===")
    test_texts = [
        "Quero verificar meu extrato bancário",
        "O app está dando erro ao abrir",
        "Não quero mais pagar esse plano",
        "Como faço um PIX para outra conta",
    ]

    for text in test_texts:
        processed = preprocess(text)
        prediction = classifier.predict(processed)
        print(f"  \"{text}\"")
        print(f"    → {prediction}")
        print()


if __name__ == "__main__":
    main()
