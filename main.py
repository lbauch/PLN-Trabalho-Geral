import os
from dotenv import load_dotenv
from config.data_types import DATA_TYPES
from core.initial_pipeline import DataPipeline
from core.data_cleaner import DataCleaner
from pathlib import Path

load_dotenv()

def main():
    BASE_DIR = Path(__file__).resolve().parent

    # region Initial Treatment

    # Parte abaixo comentada para não ser executada novamente

    # raw_file_name = os.getenv("RAW_FILE_NAME")
    # processed_file_name = os.getenv("PROCESSED_FILE_NAME")

    # pipeline = DataPipeline(
    #     data_types=DATA_TYPES,
    #     raw_file_name=raw_file_name,
    #     processed_file_name=processed_file_name,
    # )

    # pipeline.run()

    # end region

    data_to_clean = BASE_DIR / os.getenv("DATA_TO_CLEAN")
    clean_output_path = BASE_DIR / os.getenv("CLEAN_OUTPUT_PATH")

    # Etapa de limpeza adicional
    cleaner = DataCleaner(
        input_path=data_to_clean,
        output_path=clean_output_path,
    )

    print("Starting data cleaning...")
    cleaner.run()

if __name__ == "__main__":
    main()