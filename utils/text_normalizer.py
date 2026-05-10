import pandas as pd
from pathlib import Path
import spacy
import nltk
from nltk.corpus import stopwords

# Downloads necessários
try:
    stopwords.words("portuguese")
except LookupError:
    nltk.download("stopwords")
    nltk.download("rslp")

# Carregar modelo spaCy
nlp = spacy.load("pt_core_news_sm")

# Stemmer
stemmer = nltk.stem.RSLPStemmer()

# Stopwords customizadas
custom_stopwords = set(stopwords.words("portuguese"))

# Remover variações de "São"
EXCLUDE_WORDS = {"são", "sao", "São", "Sao"}

for w in EXCLUDE_WORDS:
    custom_stopwords.discard(w)

# Funções base de processamento

def tokenize(text):
    doc = nlp(str(text))
    return [t.text for t in doc if not t.is_punct]

def remove_stopwords(tokens):
    return [t for t in tokens if t.lower() not in custom_stopwords]

def apply_stemming(tokens):
    return [
        t if t in EXCLUDE_WORDS else stemmer.stem(t)
        for t in tokens
    ]

def apply_lemmatization(tokens):
    doc = nlp(" ".join(tokens))
    
    result = []
    for original_token, spacy_token in zip(tokens, doc):
        if original_token.lower() in EXCLUDE_WORDS:
            result.append(original_token)
        else:
            result.append(spacy_token.lemma_)
    
    return result

# Pipeline genérico (ordem controlada)

def process_pipeline(text_series, order):
    results = []

    for text in text_series:
        tokens = tokenize(text)

        if order == "stop_lemma":
            tokens = remove_stopwords(tokens)
            tokens = apply_lemmatization(tokens)

        elif order == "stop_stem":
            tokens = remove_stopwords(tokens)
            tokens = apply_stemming(tokens)

        elif order == "stop":
            tokens = remove_stopwords(tokens)    

        results.append(" ".join(tokens))

    return results


# Carregar dataset e gerar colunas

BASE_DIR = Path(__file__).resolve().parent if "__file__" in globals() else Path().resolve()

INPUT_PATH = BASE_DIR.parent / "data" / "data_cleaned_indexed_by_day.csv"
OUTPUT_PATH = BASE_DIR.parent / "data" / "processed_text.csv"

df = pd.read_csv(INPUT_PATH)
df.to_csv(OUTPUT_PATH, index=False)

df["stop"] = process_pipeline(df["description_lower"], "stop")
df["stop_lemma"] = process_pipeline(df["description_lower"], "stop_lemma")
df["stop_stem"] = process_pipeline(df["description_lower"], "stop_stem")


df.to_csv(OUTPUT_PATH, index=False)

print("Arquivo processado salvo com sucesso.")