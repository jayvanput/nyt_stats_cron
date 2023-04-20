import os
import datetime
import requests
import dotenv

class StatFetcher:

    PUZZLE_INFO = "https://nyt-games-prd.appspot.com/svc/crosswords/v2/puzzle/daily-{date}.json"
    SOLVE_INFO = "https://nyt-games-prd.appspot.com/svc/crosswords/v2/game/{puzzle_id}.json"
    
    def __init__(self, cookie: str|None):
        self.cookie: dict[str, str|None] = {'NYT-S': cookie}

    def get_puzzle_id(self, puzzle_date: datetime.date) -> str:
        """ Returns the puzzle ID for the specified date. """
        date_str = puzzle_date.strftime("%Y-%m-%d")
        response = requests.get(self.PUZZLE_INFO.format(date=date_str))
        response.raise_for_status()

        puzzle_id = response.json()["results"][0]["puzzle_id"]

        return puzzle_id

    def fetch_stats(self, puzzle_date: datetime.date) -> dict[str,bool|str|int]:
        """ Returns the user's stats for the specified date. """
        puzzle_id = self.get_puzzle_id(puzzle_date)
        response = requests.get(
            self.SOLVE_INFO.format(puzzle_id=puzzle_id),
            cookies=self.cookie    
        )
        return response.json()["results"]

def format_stats(stats: dict[str, bool|str|int], puzzle_date: datetime.date) -> tuple[int|str, ...]:
    if stats["solved"] == False:
        return None
    puzzle_date_str: str = puzzle_date.strftime("%Y-%m-%d")
    solve_date: str  = datetime.datetime.fromtimestamp(stats["firstCleared"]).strftime("%Y-%m-%d")
    elapsed_seconds: str = stats["timeElapsed"]
    streak: int = 1 if stats["eligible"] else 0
    owner_id: int = 1
    day: str = puzzle_date.strftime("%A")
    used_help = 1 if 'firstChecked' in stats or 'firstRevealed' in stats else 0

    output = (puzzle_date_str, solve_date, elapsed_seconds, streak, owner_id, day, used_help)
    return output

    

if __name__ == "__main__":
    dotenv.load_dotenv()
    COOKIE = os.environ.get("COOKIE")
    fetcher = StatFetcher(COOKIE)
    stats = fetcher.fetch_stats(datetime.date(2023, 4, 17))

    print(format_stats(stats, datetime.date(2023, 4, 17)))
