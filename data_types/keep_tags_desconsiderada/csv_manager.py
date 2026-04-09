import re
from core.base_csv_manager import BaseCSVManager


class CSVManager(BaseCSVManager):

    def _remove_numbered_prefix(self, text: str) -> str:
        """
        Remove prefixos numerados no início da description de linhas HTML ou texto simples.
        Caso tratado:
        <p><strong>numero*.</strong> ...
        <p><strong>numero♦.</strong> ...
        <p><strong>numero*</strong> ...
        <p><strong>numero♦</strong> ...
        <p><strong>numero</strong> ...
        <p><strong>numero</strong><strong>♦.   </strong> ...
        Mantém sempre o <p> inicial se existir.
        """
        if not isinstance(text, str):
            return text  # evita erro caso seja NaN ou outro tipo
        
        text = re.sub(
            r'^(<p>\s*)'
            r'(?:'
                r'<strong>\d{1,2}</strong>\s*<strong>\s*[*♦]\.?\s*</strong>'  # dois strong
                r'|'
                r'<strong>\d{1,2}[*♦]?\.?\s*</strong>'                        # um strong só
            r')\s*',
            r'\1',
            text
        )

        return text