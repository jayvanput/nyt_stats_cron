import dotenv
import os
import datetime
import sqlite3

from stat_fetcher import StatFetcher, format_stats


if __name__ == "__main__":
    dotenv.load_dotenv()

    # Get cookies
    COOKIE = os.environ.get("COOKIE")
    fetcher = StatFetcher(COOKIE)

    # get today's date.
    todays_date = datetime.date.today()
    output = fetcher.fetch_stats(todays_date)

    values = format_stats(output, todays_date)

    print(values)
    con = sqlite3.connect("D:\\Projects\\nyt_dashboard_api\\db.sqlite3")
    cur = con.cursor()
    res = cur.execute(f"INSERT INTO api_entry (puzzle_date, solve_date, elapsed_seconds, streak, owner_id, day, used_help) VALUES {values};")
    con.commit()
    con.close()