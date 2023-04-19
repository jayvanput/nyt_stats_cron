import dotenv
import os
import datetime

from stat_fetcher import StatFetcher


if __name__ == "__main__":
    dotenv.load_dotenv()

    # Get cookies
    COOKIE = os.environ.get("COOKIE")
    fetcher = StatFetcher(COOKIE)

    # get today's date.
    todays_date = datetime.date.today()
    output = fetcher.fetch_stats(todays_date)

    print(output)