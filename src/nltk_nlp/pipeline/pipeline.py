from nltk_nlp.domain.models import NLPResult
from nltk_nlp.tokenizer.tokenizer import Tokenizer
from nltk_nlp.normalization.lowercase import LowercaseNormalizer
from nltk_nlp.normalization.stopwords import StopwordFilter
from nltk_nlp.normalization.stemming import Stemmer
from nltk_nlp.statistics.frequency import FrequencyCounter
from nltk_nlp.statistics.vocabulary import Vocabulary

class NLPPipeline:

  def __init__(self) -> None:

    self.tokenizer = Tokenizer()
    self.lowercase = LowercaseNormalizer()
    self.stopwords = StopwordFilter()
    self.stemmer = Stemmer()
    self.frequency = FrequencyCounter()
    self.vocabulary = Vocabulary()

  def process(self, text: str) -> dict:

    # 1. Tokenização
    tokens = self.tokenizer.tokenize(text)

    # 2. Lowercase
    normalized = self.lowercase.normalize(tokens)

    # 3. Stopwords
    filtered = self.stopwords.filter(normalized)

    # 4. Stemming
    stems = [
      self.stemmer.stem(token)
      for token in filtered
    ]

    # 5. Frequência
    frequencies = self.frequency.count(filtered)

    # 6. Vocabulário
    vocabulary = self.vocabulary.build(filtered)

    return {
      "original": text,
      "tokens": tokens,
      "normalized": normalized,
      "without_stopwords": filtered,
      "stems": stems,
      "frequencies": frequencies,
      "vocabulary": vocabulary,
    }