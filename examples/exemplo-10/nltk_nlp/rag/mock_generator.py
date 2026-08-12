from .generator import Generator


class MockGenerator(Generator):

    def generate(
        self,
        prompt: str,
    ) -> str:

        if "CONTEXTO:" in prompt and "PERGUNTA:" in prompt:
            context_start = prompt.index("CONTEXTO:") + len("CONTEXTO:")
            question_start = prompt.index("PERGUNTA:")
            context = prompt[context_start:question_start].strip()

            return (
                f"[Resposta baseada em "
                f"{len(context)} chars de contexto]"
            )

        return "[Sem contexto disponível]"
