import csv
import pandas as pd
import re

class CSVManager():
    """
    Usada para tratar com o arquivo .csv.
    """
    def __init__(self):
        # Linhas a serem removidas do dataset - referentes ao dia 29/02, anotadas dia 28/02.
        self.linhas_remover = [751, 750, 749, 748]
        # Frases contidas nos dias 28 e 29 que distorcem o dataset.
        self.frases_remover = [
            " Nos anos bissextos omitem-se os seguintes:",
            "NOS ANOS BISSEXTOS 1. ",
            " Nos anos não bissextos continua-se:"
        ]


    def save(self, data, output_path):
        """
        Salvar os dados recebidos do scrapper e tratados em csv
        """
        with open(output_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["date", "description", "death_date"]
            )
            writer.writeheader()
            writer.writerows(data)

    # region Tratativa Inicial 
    def _remove_prefix(self, text: str) -> str:
        """
        Remove prefixos dos tipos:
        "2.", "3*.", "8♦.", "5", "10♦"
        Apenas quando aparecem no início da string.
        """
        if not isinstance(text, str):
            return text  # evita erro caso seja NaN ou outro tipo
        
        pattern = r'^\d{1,2}[*♦]?\.?\s*'
        return re.sub(pattern, '', text)


    def _remover_linhas_duplicadas(self, df: pd.DataFrame):
        """
        Remove linhas do DataFrame pelos índices.
        """
        df = df.drop(self.linhas_remover)
        return df.drop_duplicates()
    

    def _remover_frases(self, text: str) -> str:
        """
        Remove frases específicas, do dia 28 e 29/02
        Também remove trechos iniciados por ', hoje'
        até a próxima vírgula ou ponto.

        Exemplos:
        ', hoje na Itália,' -> ''
        ', hoje em Roma.' -> '.'
        """
        for frase in self.frases_remover:
            text = text.replace(frase, '')

        pattern = r', hoje[^,.]*([,.])'

        return re.sub(pattern, r'\1', text)


    def _clean_description(self, df: pd.DataFrame, coluna: str = 'description') -> pd.DataFrame:
        """
        Aplica a remoção do prefixo numerado em uma coluna do DataFrame.
        """
        df[coluna] = df[coluna].apply(self._remove_prefix)
        df[coluna] = df[coluna].apply(self._remover_frases)
        return df


    def _description_lower_id_by_day(self, df):
        # Criar coluna id_day
        df['id_day'] = df.groupby('date').cumcount() + 1

        # Lowercase na descrição
        df['description_lower'] = df['description'].str.lower()

        # Reorganizar colunas
        df = df[['id_day', 'date', 'description', 'death_date', 'description_lower']]

        return df


    def pre_process(self, data_in, data_out):
        df = pd.read_csv(f'{data_in}')

        df = self._clean_description(df)
        df = self._remover_linhas_duplicadas(df)
        df = self._description_lower_id_by_day(df)

        df.to_csv(f"{data_out}", index=False)
    # endregion