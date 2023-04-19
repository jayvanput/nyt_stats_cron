import dotenv
import os
import datetime
import sqlite3

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
    con = sqlite3.connect("D:\\Projects\\nyt_dashboard_api\\db.sqlite3")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM api_entry;")

    print(res.fetchone())
