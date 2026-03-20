import os
import importlib
from dotenv import load_dotenv
from config.data_types import DATA_TYPES

load_dotenv()

def main():

    # data_type = os.getenv("DATA_TYPE")
    raw_file_name = os.getenv("RAW_FILE_NAME")
    processed_file_name = os.getenv("PROCESSED_FILE_NAME")

    for data_type in DATA_TYPES:
        # if not data_type:
        #     raise ValueError("DATA_TYPE not defined in .env")

        base_path = os.path.join("data_types", data_type, 'data')

        scraper_module = importlib.import_module(
            f"data_types.{data_type}.scraper"
        )

        csv_module = importlib.import_module(
            f"data_types.{data_type}.csv_manager"
        )

        scraper = scraper_module.Scraper()
        csv_manager = csv_module.CSVManager()

        print("Starting scraping process...")
        data = scraper.collect_full_year()

        raw_output_path = os.path.join(base_path, raw_file_name)
        processed_output_path = os.path.join(base_path, processed_file_name)

        print("Saving raw file...")
        csv_manager.save(data, raw_output_path)

        print("Processing file...")
        csv_manager.process(raw_output_path, processed_output_path)

        print("Process completed successfully.")


if __name__ == "__main__":
    main()