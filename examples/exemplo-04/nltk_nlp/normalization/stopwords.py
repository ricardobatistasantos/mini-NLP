from nltk.corpus import stopwords

class StopwordFilter:
  def __init__(self) -> None:
    self.stopwords = set(
      stopwords.words("portuguese")
    )
    
  def filter(self, tokens: list[str])-> list[str]:
    return [
      token
      for token in tokens
      if token not in self.stopwords
    ]