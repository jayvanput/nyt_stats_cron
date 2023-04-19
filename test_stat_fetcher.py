import unittest
import dotenv
import os
import datetime

from stat_fetcher import StatFetcher


class TestStatFetcher(unittest.TestCase):
    


    def setUp(self) -> None:
        dotenv.load_dotenv()
        COOKIE = os.environ.get("COOKIE")
        self.fetcher = StatFetcher(COOKIE)
        self.puzzle_date = datetime.date(2023, 4, 17)

    def test_fetch_returns_dict(self):
        output = self.fetcher.fetch_stats(self.puzzle_date)
        self.assertIsInstance(output, dict)

    def test_get_puzzle_id(self):
        # 4/17/2023 puzzle ID is 20984.
        puzzle_id = self.fetcher.get_puzzle_id(self.puzzle_date)
        self.assertEqual(puzzle_id, 20984)
        
    def test_puzzle_returns_date_stats_from_datetime(self):
        # On 4/17 I solved the monday in 4:44.
        output = self.fetcher.fetch_stats(self.puzzle_date)

        self.assertEqual(output["timeElapsed"], 284)