A classe main está com o fluxo comentado para não ficar executando novamente todos os passos a cada execução.
Caso se deseje executar todo o fluxo, é possível definir (em config) quas tipos de texto se deseja extrair e descomentar as linhas de main, contemplando todas as etapas.

A pasta_data_types, possui as tratativas para cada extração dos textos por webscrapping, salvando os textos em diferentes formatos (salvos dentro das pastas data dos respectivos data_types). Cada csvmanager e scrapper herdam das classes de core.

Os arquivos dentro de core foram utilizados até estes passos, dentro da classe main.py.

Para os passos seguintes, como lematização, stemming, tokenização, remoção de stopwords, adição de colunas essenciais para a análise futura e análise de BoW e TF-ID, optou-se pelo uso do data_type get_text_split_words.
Para análise mais acurada, estas tratativas mais complexas foram feitas no arquivo .ipynb dentro de analysis, fazendo uma análise de BoW e TF-IDF das seguintes combinações:
1) Usando a coluna description_lower: remoção de stopwords > lematização
2) Usando a coluna description_lower: remoção de stopwords > stemming
3) Usando a coluna description_lower: lematização > remoção de stopwords
4) Usando a coluna description_lower: stemming > remoção de stopwords
5 - 8) Mesmos passos utilizando a coluna description para a análise.