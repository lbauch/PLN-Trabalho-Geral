import csv
import pandas as pd
import re

class CSVManager():
    """
    Usada para tratar com o arquivo .csv.
    """

    def save(self, data, output_path):
        with open(output_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["date", "description", "death_date"]
            )
            writer.writeheader()
            writer.writerows(data)

    def _remove_numbered_prefix(self, text: str) -> str:
        """
        Remove prefixos do tipo:
        "2.", "3*.", "8♦.", "5", "10♦"
        Apenas quando aparecem no início da string.
        """
        if not isinstance(text, str):
            return text  # evita erro caso seja NaN ou outro tipo
        
        pattern = r'^\d{1,2}[*♦]?\.?\s*'
        return re.sub(pattern, '', text)


    def _clean_description(self, df: pd.DataFrame, coluna: str = "description") -> pd.DataFrame:
        """
        Aplica a remoção do prefixo numerado em uma coluna do DataFrame.
        """
        df[coluna] = df[coluna].apply(self._remove_numbered_prefix)
        return df


    def process(self, data_in, data_out):
        df = pd.read_csv(f"{data_in}")

        df = self._clean_description(df)

        df.to_csv(f"{data_out}", index=False)