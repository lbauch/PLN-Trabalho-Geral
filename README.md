Os arquivos dentro de utils foram utilizados para tratamento inicial dos dados

Para os passos seguintes, como lematização, stemming, tokenização, remoção de stopwords, adição de colunas essenciais para a análise futura e análise de BoW e TF-ID, optou-se pelo uso do data_type get_text_split_words.
Para análise mais acurada, estas tratativas mais complexas foram feitas no arquivo data_preparation_and_analysis.ipynb dentro de analysis, fazendo uma análise de BoW e TF-IDF das seguintes combinações, todas utilizando a coluna description_lower:
1) lower_stop: Apenas remoção de stopwords
2) lower_stop_lemma: remoção de stopwords > lematização
3) lower_stop_stem: remoção de stopwords > stemming