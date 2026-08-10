from nltk.stem import RSLPStemmer

class Stemmer:
  def __init__(self) -> None:
    self._stemmer = RSLPStemmer()
    
  def stem(self, tokens: list[str]) -> list[str]:
    return [
      self._stemmer.stem(token)
      for token in tokens
    ]