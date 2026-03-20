from datetime import datetime, timedelta


def generate_year_dates(year: int):
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)

    dates = []
    current = start_date

    while current <= end_date:
        dates.append(current.strftime("%Y-%m-%d"))
        current += timedelta(days=1)

    return dates