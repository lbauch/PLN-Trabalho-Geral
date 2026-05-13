# region Imports
import os
from dotenv import load_dotenv
from pathlib import Path
from utils.scrapper import Scraper
from utils.csv_manager import CSVManager
from utils.text_normalizer import TextNormalizer
# endregion

def main():
    """
    Contém o fluxo das tratativas iniciais (scrapping, salvamento e ajustes)
    """
    load_dotenv()
    BASE_DIR = Path(__file__).resolve().parent

    # region Arquivos
    raw_file_name = os.getenv("RAW_FILE_NAME")
    pre_processed_file_name = os.getenv("PRE_PROCESSED_FILE_NAME")
    normalized_file_name = os.getenv("NOMALIZED_FILE_NAME")

    raw_output_path = BASE_DIR / "data_output" / raw_file_name
    pre_processed_output_path = BASE_DIR / "data_output" / pre_processed_file_name
    processed_output_path = (BASE_DIR / "data_output" / normalized_file_name)
    # endregion

    # region Scrapping
    print(f"Starting scraping process...")
    data = Scraper().collect_full_year()

    print(f"Saving raw file...")
    CSVManager().save(data, raw_output_path)
    # endregion

    # region Pré-Processamento
    print(f"Processing file...")
    CSVManager().pre_process(raw_output_path, pre_processed_output_path)

    print(f"Process completed successfully.\n")
    # endregion

    # region Normalização
    print("Running text normalization...")

    TextNormalizer().process(pre_processed_output_path, processed_output_path)
    # endregion

if __name__ == "__main__":
    main()