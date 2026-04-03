import pandas as pd


class DataCleaner:
    """
    Adiciona colunas necessárias para a análise e reorganiza a ordem das colunas do .csv
    Não envolve lematização, stemming ou outras tratativas mais avançadas.
    """
    def __init__(self, input_path, output_path):
        self.input_path = input_path
        self.output_path = output_path

    def run(self):
        df = self._load_data()
        df = self._transform(df)
        self._save(df)

    def _load_data(self):
        return pd.read_csv(self.input_path)

    def _transform(self, df):
        # Criar coluna id_day
        df['id_day'] = df.groupby('date').cumcount() + 1

        # Lowercase na descrição
        df['description_lower'] = df['description'].str.lower()

        # Reorganizar colunas
        df = df[['id_day', 'date', 'description', 'death_date', 'description_lower']]

        return df

    def _save(self, df):
        df.to_csv(self.output_path, index=False)