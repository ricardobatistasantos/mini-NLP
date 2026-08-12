from nltk.tokenize import word_tokenize

class Tokenizer:
  def tokenize(self, text: str) ->list[str]:
    return word_tokenize(text, language="portuguese")