import dotenv
import os

from stat_fetcher import StatFetcher


if __name__ == "__main__":
    dotenv.load_dotenv()
    COOKIE = os.environ.get("COOKIE")
    fetcher = StatFetcher(COOKIE)
    fetcher.fetch_stats()