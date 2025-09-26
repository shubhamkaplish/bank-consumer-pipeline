
from sqlalchemy import create_engine, text
import pandas as pd
from pathlib import Path

BASE = Path(__file__).resolve().parents[1]
DB_URL = f"sqlite:///{BASE / 'bank.db'}"

def get_engine():
    return create_engine(DB_URL)

def read_sql(query: str, params: dict | None = None) -> pd.DataFrame:
    engine = get_engine()
    with engine.begin() as conn:
        df = pd.read_sql(text(query), conn, params=params or {})
    return df

if __name__ == "__main__":
    # quick smoke test
    q = "SELECT * FROM transactions ORDER BY txn_ts LIMIT 5"
    print(read_sql(q))
