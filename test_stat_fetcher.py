import unittest
import dotenv
import os

from stat_fetcher import StatFetcher


class TestStatFetcher(unittest.TestCase):
    
    def setUp(self) -> None:
        dotenv.load_dotenv()
        COOKIE = os.environ.get("COOKIE")
        self.fetcher = StatFetcher(COOKIE)

    def test_fetch_returns_dict(self):
       output = self.fetcher.fetch_stats()
       self.assertIsInstance(output, dict)