class LowercaseNormalizer:
  def normalize(self, tokens: list[str]) -> list[str]:
    return [
      token.lower()
      for token in tokens
    ]