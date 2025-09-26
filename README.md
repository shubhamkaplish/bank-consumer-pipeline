# Bank Consumer Pipeline (Mini Project)

An end-to-end **SQL → Python → Report** pipeline using a small banking consumer dataset.

## What it does
- Builds a SQLite database (`bank.db`) from SQL schema + sample data
- Extracts data with SQL (via SQLAlchemy)
- Transforms and generates KPIs in pandas
- Exports a multi-sheet Excel report and saves charts

## Stack
- SQLite (can swap to MySQL/Postgres by changing the connection URL)
- Python: pandas, SQLAlchemy, matplotlib, openpyxl

## Project Structure
```
bank_consumer_pipeline/
├── bank.db                # created after step 1
├── sql/
│   ├── create_schema.sql
│   └── load_sample_data.sql
├── scripts/
│   ├── build_db.py
│   ├── extract.py
│   ├── transform.py
│   └── analyze.py
├── output/
│   └── customer_metrics.xlsx
├── visuals/
│   ├── monthly_amount.png
│   └── monthly_txn_count.png
├── main.py
└── requirements.txt
```

## How to run (locally)
1. **Install deps**
   ```bash
   pip install -r requirements.txt
   ```

2. **Build the database**
   ```bash
   python scripts/build_db.py
   ```

3. **Run the pipeline**
   ```bash
   python main.py
   ```

## KPIs Produced
- **Monthly KPIs:** total net amount, count of transactions, count of flagged (>10k) transactions
- **Customer Summary:** total amount, average txn, txn count, flagged count per customer
- **Top Merchants:** biggest spend (most negative) merchants

## Swap to a real SQL server
- Replace the SQLite URL in `scripts/extract.py` and `main.py` with your DSN, e.g.
  ```python
  DB_URL = "postgresql+psycopg://user:pwd@host:5432/dbname"
  # or
  DB_URL = "mysql+pymysql://user:pwd@host:3306/dbname"
  ```

## Notes
- Data is synthetic and small, designed for a resume-ready demo.
- Extend with: Airflow/Prefect orchestration, dbt for modeling, or Power BI dashboard fed by `output/customer_metrics.xlsx`.
