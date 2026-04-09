import re
from core.base_csv_manager import BaseCSVManager


class CSVManager(BaseCSVManager):

    def _remove_numbered_prefix(self, text: str) -> str:
        """
        Remove prefixos do tipo:
        **2.      **
        **3*.     **
        **8♦.     **
        **13** **♦.   **
        Apenas quando aparecem no início da string.
        """
        if not isinstance(text, str):
            return text  # evita erro caso seja NaN ou outro tipo
        
        pattern = r'^\*\*\d{1,2}(?:[*♦]?\.?)?\s*\*\*(?:\s*\*\*\s*[*♦]\.?\s*\*\*)?\s*'
        return re.sub(pattern, '', text)