import unittest
import dotenv
import os
import datetime

from stat_fetcher import StatFetcher, format_stats


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

class TestFormatStats(unittest.TestCase):

    def setUp(self) -> None:
        dotenv.load_dotenv()
        COOKIE = os.environ.get("COOKIE")

        self.fetcher = StatFetcher(COOKIE)


    def test_formatter_returns_tuple(self):
        puzzle_date = datetime.date(2023, 4, 17)
        stats = self.fetcher.fetch_stats(puzzle_date)

        values = format_stats(stats, puzzle_date)
        self.assertIsInstance(values, tuple)

    def test_formatter_fails_on_unsolved_puzzle(self):
        # to avoid the issue of me solving the puzzle, below is a mock output from 4/19/2023 prior to solving:
        UNSOLVED_STATS = {'eligible': True, 'id': '74267487-20990', 'isPuzzleInfoRead': False, 'lastUpdateTime': 0, 'solved': False, 'timeElapsed': 0, 'unmerged': True}
        puzzle_date = datetime.date(2023, 4, 19)

        values = format_stats(UNSOLVED_STATS, puzzle_date)
        self.assertEqual(values, None)

    def test_formatter_formats_properly(self):
        puzzle_date = datetime.date(2023, 4, 17)
        stats = self.fetcher.fetch_stats(puzzle_date)

        values = format_stats(stats, puzzle_date)
        self.assertEqual(len(values), 7)