from pathlib import Path
from scrapper import Scraper
from csv_manager import CSVManager

class DataPipeline:
    """
    Contém o fluxo inicial para fazer o webscrapping e salvar em um arquivo .csv
    """
    def __init__(self, raw_file_name, processed_file_name):
        self.raw_file_name = raw_file_name
        self.processed_file_name = processed_file_name

    def run(self):
        BASE_DIR = Path(__file__).resolve().parent

        print(f"Starting scraping process...")
        data = Scraper.collect_full_year()

        raw_output_path = BASE_DIR.parent / "data_output" / self.raw_file_name
        processed_output_path = BASE_DIR.parent / "data_output" / self.processed_file_name

        print(f"Saving raw file...")
        CSVManager.save(data, raw_output_path)

        print(f"Processing file...")
        CSVManager.process(raw_output_path, processed_output_path)

        print(f"Process completed successfully.\n")