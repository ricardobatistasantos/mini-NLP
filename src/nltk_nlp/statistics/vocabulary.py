class Vocabulary:

  def build(
    self,
    tokens: list[str],
  ) -> set[str]:

    return set(tokens)

  def size(
    self,
    tokens: list[str],
  ) -> int:

    return len(self.build(tokens))