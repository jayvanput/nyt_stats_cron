import os


class StatFetcher:

    def __init__(self, cookie):
        self.cookie: str|None = cookie

    def fetch_stats(self):
        print(self.cookie)


if __name__ == "__main__":
    stat_fetcher = StatFetcher()
    stat_fetcher.fetch_stats()