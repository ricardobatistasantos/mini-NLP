class PromptBuilder:

    def build(
        self,
        query: str,
        context: str,
    ) -> str:

        return f"""
Você é um assistente que responde
perguntas utilizando exclusivamente
o contexto fornecido.

Se a resposta não estiver presente
no contexto, diga que não encontrou
informação suficiente.

Não invente informações.

CONTEXTO:

{context}

PERGUNTA:

{query}

RESPOSTA:
""".strip()