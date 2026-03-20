import os
import requests
from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from core.date_csv_generator import generate_year_dates

load_dotenv()


class BaseScraper(ABC):

    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.year = int(os.getenv("YEAR"))

        if not self.base_url:
            raise ValueError("BASE_URL not defined in .env")


    @abstractmethod
    def extract_fields(self, tds):
        """
        Coleta todos os <tr> da tabela de um dia específico
        Must return:
        {
            "description": str,
            "death_date": str
        }
        or None
        """
        raise ValueError('Static Method Not Implemented')


    def collect_full_year(self):
        dates = generate_year_dates(self.year)
        all_data = []

        for date in dates:
            print(f"Collecting {date}...")
            url = f"{self.base_url}{date}"

            try:
                response = requests.get(url, timeout=10)
                response.raise_for_status()

                soup = BeautifulSoup(response.text, "html.parser")
                table = soup.find("table")

                if not table:
                    continue

                rows = table.find_all("tr")

                for row in rows:
                    tds = row.find_all("td")
                    result = self.extract_fields(tds)

                    if result:
                        result["date"] = date
                        all_data.append(result)

            except Exception as e:
                print(f"Error on {date}: {e}")

        return all_data