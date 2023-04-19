import os
import datetime
import requests
import dotenv

class StatFetcher:

    PUZZLE_INFO = "https://nyt-games-prd.appspot.com/svc/crosswords/v2/puzzle/daily-{date}.json"
    SOLVE_INFO = "https://nyt-games-prd.appspot.com/svc/crosswords/v2/game/{puzzle_id}.json"

    def __init__(self, cookie):
        self.cookie: dict[str, str|None] = {'NYT-S': cookie}

    def get_puzzle_id(self, puzzle_date: datetime.date) -> str:
        """ Returns the puzzle ID for the specified date. """
        date_str = puzzle_date.strftime("%Y-%m-%d")
        response = requests.get(self.PUZZLE_INFO.format(date=date_str))
        response.raise_for_status()

        puzzle_id = response.json()["results"][0]["puzzle_id"]

        return puzzle_id

    def fetch_stats(self, puzzle_date: datetime.date) -> dict[str, str]:
        """ Returns the user's stats for the specified date. """
        puzzle_id = self.get_puzzle_id(puzzle_date)
        response = requests.get(
            self.SOLVE_INFO.format(puzzle_id=puzzle_id),
            cookies=self.cookie    
        )
        return response.json()["results"]


if __name__ == "__main__":
    dotenv.load_dotenv()
    COOKIE = os.environ.get("COOKIE")
    fetcher = StatFetcher(COOKIE)
    stats = fetcher.fetch_stats(datetime.date(2023, 4, 19))

    print(stats)
