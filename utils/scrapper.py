import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from utils.date_generator import generate_year_dates

load_dotenv()


class Scraper():
    """
    Usada para fazer a extração dos arquivos via Scrapping
    Possui métodos que devem ser sobrescritos para cada tipo de tratativa (data_type)
    """

    def __init__(self):
        self.base_url = os.getenv("BASE_URL")
        self.year = int(os.getenv("YEAR"))

        if not self.base_url:
            raise ValueError("BASE_URL not defined in .env")


    def _extract_fields(self, tds):
        if len(tds) >= 1:
            description = tds[0].get_text(" ", strip=True)
        else:
            description = ""

        if len(tds) >= 3:
            death_date = tds[2].get_text(" ", strip=True)
        else:
            death_date = ""

        if description:
            return {
                "description": description,
                "death_date": death_date
            }

        return None


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
                    result = self._extract_fields(tds)

                    if result:
                        result["date"] = date
                        all_data.append(result)

            except Exception as e:
                print(f"Error on {date}: {e}")

        return all_data