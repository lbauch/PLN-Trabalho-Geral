from core.base_scrapper import BaseScraper

class Scraper(BaseScraper):

    def extract_fields(self, tds):
        if len(tds) >= 1:
            for strong in tds[0].find_all("strong"):
                strong.string = f"**{strong.get_text()}**"

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