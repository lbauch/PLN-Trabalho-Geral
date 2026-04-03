import csv
import pandas as pd
from abc import ABC, abstractmethod

class BaseCSVManager(ABC):
    """
    Usada para tratar com o arquivo .csv.
    Possui métodos que devem ser sobrescritos para cada tipo de tratativa (data_type)
    """

    def save(self, data, output_path):
        with open(output_path, "w", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(
                file,
                fieldnames=["date", "description", "death_date"]
            )
            writer.writeheader()
            writer.writerows(data)


    @abstractmethod
    def _remove_numbered_prefix(self, texto: str) -> str:
        raise ValueError('Static Method Not Implemented')


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