from .loaders import (
    DocumentLoader,
    TxtLoader,
    MarkdownLoader,
    JsonLoader,
    CsvLoader,
)


class LoaderRegistry:

    def __init__(
        self,
        loaders: list[
            DocumentLoader
        ] | None = None,
    ):

        self.loaders = loaders or [
            TxtLoader(),
            MarkdownLoader(),
            JsonLoader(),
            CsvLoader(),
        ]

    def get_loader(
        self,
        path: str,
    ) -> DocumentLoader:

        for loader in self.loaders:

            if loader.supports(path):
                return loader

        raise ValueError(
            f"No loader found for: {path}"
        )