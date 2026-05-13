import pandas as pd
import spacy
import nltk
from nltk.corpus import stopwords


class TextNormalizer:

    def __init__(self):
        # Downloads necessários
        try:
            stopwords.words("portuguese")
        except LookupError:
            nltk.download("stopwords")
            nltk.download("rslp")

        # Modelo spaCy
        self.nlp = spacy.load("pt_core_news_sm")

        # Stemmer
        self.stemmer = nltk.stem.RSLPStemmer()

        # Stopwords customizadas
        self.custom_stopwords = set(stopwords.words("portuguese"))

        # Preservar "São"
        self.EXCLUDE_WORDS = {"são", "sao", "São", "Sao"}

        for w in self.EXCLUDE_WORDS:
            self.custom_stopwords.discard(w)

    # region Normalização

    def _tokenize(self, text):
        doc = self.nlp(str(text))
        return [t.text for t in doc if not t.is_punct]

    def _remove_stopwords(self, tokens):
        return [
            t for t in tokens
            if t.lower() not in self.custom_stopwords
        ]

    def _apply_stemming(self, tokens):
        return [
            t if t in self.EXCLUDE_WORDS else self.stemmer.stem(t)
            for t in tokens
        ]


    def _apply_lemmatization(self, tokens):
        doc = self.nlp(" ".join(tokens))

        result = []

        for original_token, spacy_token in zip(tokens, doc):

            if original_token.lower() in self.EXCLUDE_WORDS:
                result.append(original_token)

            else:
                result.append(spacy_token.lemma_)

        return result
    # endregion

    # region Pipeline
    def _process_pipeline(self, text_series, order):

        results = []

        for text in text_series:

            tokens = self._tokenize(text)

            if order == "stop_lemma":
                tokens = self._remove_stopwords(tokens)
                tokens = self._apply_lemmatization(tokens)

            elif order == "stop_stem":
                tokens = self._remove_stopwords(tokens)
                tokens = self._apply_stemming(tokens)

            elif order == "stop":
                tokens = self._remove_stopwords(tokens)

            results.append(" ".join(tokens))

        return results
    # endregion

    # region Execução Principal
    def process(self, input_path, output_path):

        df = pd.read_csv(input_path)

        df["stop"] = self._process_pipeline(
            df["description_lower"],
            "stop"
        )

        df["stop_lemma"] = self._process_pipeline(
            df["description_lower"],
            "stop_lemma"
        )

        df["stop_stem"] = self._process_pipeline(
            df["description_lower"],
            "stop_stem"
        )

        df.to_csv(output_path, index=False)

        print("Arquivo processado salvo com sucesso.")
    # endregion