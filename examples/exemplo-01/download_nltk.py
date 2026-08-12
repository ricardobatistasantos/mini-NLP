import nltk


def main() -> None:
    """
    Baixa os modelos e dados do NLTK necessários para este exemplo.
    Execute uma vez antes de rodar o main.py.
    """
    resources = ["punkt", "punkt_tab"]

    for resource in resources:
        nltk.download(resource)
        print(f"  ✓ {resource}")

    print("\nTodos os recursos foram baixados.")


if __name__ == "__main__":
    main()
