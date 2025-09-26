
import sqlite3
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DB_PATH = BASE / "bank.db"
SQL_DIR = BASE / "sql"

def exec_sql_file(cur, path):
    with open(path, "r", encoding="utf-8") as f:
        cur.executescript(f.read())

def main():
    if DB_PATH.exists():
        DB_PATH.unlink()
    con = sqlite3.connect(DB_PATH)
    cur = con.cursor()
    exec_sql_file(cur, SQL_DIR / "create_schema.sql")
    exec_sql_file(cur, SQL_DIR / "load_sample_data.sql")
    con.commit()
    con.close()
    print(f"Built SQLite database at: {DB_PATH}")

if __name__ == "__main__":
    main()
