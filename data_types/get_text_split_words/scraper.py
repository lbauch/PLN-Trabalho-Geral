from core.base_scrapper import BaseScraper

class Scraper(BaseScraper):

    def extract_fields(self, tds):
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