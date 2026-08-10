class FrequencyCounter:

  def count(
    self,
    tokens: list[str],
  ) -> dict[str, int]:

    frequencies: dict[str, int] = {}

    for token in tokens:
      frequencies[token] = (
        frequencies.get(token, 0) + 1
      )

    return frequencies

  def most_common(
    self,
    tokens: list[str],
    limit: int = 10,
  ) -> list[tuple[str, int]]:

    frequencies = self.count(tokens)

    return sorted(
      frequencies.items(),
      key=lambda item: item[1],
      reverse=True,
    )[:limit]