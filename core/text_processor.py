import pandas as pd
import spacy
import nltk
from nltk.corpus import stopwords


class TextProcessor:
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

        # Carregar modelo spaCy PT-BR
        self.nlp = spacy.load("pt_core_news_sm")

        # Stopwords
        try:
            self.stopwords = set(stopwords.words("portuguese"))
        except LookupError:
            nltk.download("stopwords")
            nltk.download('rslp')
            self.stopwords = set(stopwords.words("portuguese"))

    def run(self):
        df = pd.read_csv(self.input_path)

        df["tokens"] = df["description"].apply(self._tokenize)
        df["no_stopwords"] = df["tokens"].apply(self._remove_stopwords)
        df["stemmed"] = df["no_stopwords"].apply(self._stem)
        df["lemmatized"] = df["no_stopwords"].apply(self._lemmatize)

        df.to_csv(self.output_path, index=False)

    def _tokenize(self, text):
        doc = self.nlp(str(text))
        return [token.text for token in doc if not token.is_punct]

    def _remove_stopwords(self, tokens):
        return [t for t in tokens if t.lower() not in self.stopwords]

    def _stem(self, tokens):
        # NLTK RSLP Stemmer (melhor opção pra PT-BR no NLTK)
        stemmer = nltk.stem.RSLPStemmer()
        return [stemmer.stem(t) for t in tokens]

    def _lemmatize(self, tokens):
        doc = self.nlp(" ".join(tokens))
        return [token.lemma_ for token in doc]