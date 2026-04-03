import os
import importlib


class DataPipeline:

    """
    Contém o fluxo para fazer o webscrapping e salvar em um
    arquivo .csv para cada tipo de texto final (data_type)
    """

    def __init__(self, data_types, raw_file_name, processed_file_name):
        self.data_types = data_types
        self.raw_file_name = raw_file_name
        self.processed_file_name = processed_file_name

    def run(self):
        for data_type in self.data_types:
            self._process_data_type(data_type)

    def _process_data_type(self, data_type):
        base_path = os.path.join("data_types", data_type, "data")

        # scraper_module = importlib.import_module(
        #     f"data_types.{data_type}.scraper"
        # )

        csv_module = importlib.import_module(
            f"data_types.{data_type}.csv_manager"
        )

        # scraper = scraper_module.Scraper()
        csv_manager = csv_module.CSVManager()

        # print(f"[{data_type}] Starting scraping process...")
        # data = scraper.collect_full_year()

        raw_output_path = os.path.join(base_path, self.raw_file_name)
        processed_output_path = os.path.join(base_path, self.processed_file_name)

        # print(f"[{data_type}] Saving raw file...")
        # csv_manager.save(data, raw_output_path)

        print(f"[{data_type}] Processing file...")
        csv_manager.process(raw_output_path, processed_output_path)

        print(f"[{data_type}] Process completed successfully.\n")