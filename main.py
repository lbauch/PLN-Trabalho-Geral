import os
from dotenv import load_dotenv
from pathlib import Path
# from config.data_types import DATA_TYPES
# from core.initial_pipeline import DataPipeline
from core.data_cleaner import DataCleaner

load_dotenv()

def main():

    """
    Contém o fluxo das tratativas iniciais (scrapping, salvamento e ajustes)
    """

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

    # print("Starting data pipeline...")
    # pipeline.run()
    # print("Data pipeline completed.")

    #endregion

    # region Cleaning & Indexing

    # Parte abaixo comentada para não ser executada novamente

    # Etapa de limpeza adicional
    # cleaner = DataCleaner(
    #     input_path = BASE_DIR / os.getenv("DATA_TO_CLEAN"),
    #     output_path = BASE_DIR / os.getenv("CLEAN_OUTPUT_PATH")
    # )

    # print("Starting data cleaning...")
    # cleaner.run()
    # print("Data cleaning completed.")

if __name__ == "__main__":
    main()