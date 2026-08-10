import nltk

def main() -> None:
  resources = [
    "punkt",
    "punkt_tab",
    "stopwords",
    "wordnet",
    "omw-1.4",
  ]
  for resource in resources:
    nltk.download(resource)
    
if __name__ == "__main__":
  main()