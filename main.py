
from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sqlalchemy import create_engine, text

# Local modules
from scripts.extract import read_sql
from scripts.transform import add_time_features, join_with_customers
from scripts.analyze import kpi_monthly_volume, kpi_customer_summary, kpi_top_merchants

BASE = Path(__file__).resolve().parent
DB_URL = f"sqlite:///{BASE / 'bank.db'}"
OUTPUT_DIR = BASE / "output"
VIS_DIR = BASE / "visuals"
OUTPUT_DIR.mkdir(exist_ok=True, parents=True)
VIS_DIR.mkdir(exist_ok=True, parents=True)

def load_tables():
    q_txn = "SELECT * FROM transactions"
    q_acc = "SELECT * FROM accounts"
    q_cus = "SELECT * FROM customers"
    df_txn = read_sql(q_txn)
    df_acc = read_sql(q_acc)
    df_cus = read_sql(q_cus)
    return df_txn, df_acc, df_cus

def make_charts(monthly: pd.DataFrame):
    # Line chart of monthly total amount
    fig = plt.figure()
    plt.plot(monthly['month'], monthly['total_amount'])
    plt.title("Monthly Net Transaction Amount")
    plt.xlabel("Month")
    plt.ylabel("Amount")
    fig.tight_layout()
    fig.savefig(VIS_DIR / "monthly_amount.png", dpi=150)
    plt.close(fig)

    # Bar chart of monthly total transactions
    fig2 = plt.figure()
    plt.bar(monthly['month'], monthly['total_txns'])
    plt.title("Monthly Transaction Count")
    plt.xlabel("Month")
    plt.ylabel("Transactions")
    fig2.tight_layout()
    fig2.savefig(VIS_DIR / "monthly_txn_count.png", dpi=150)
    plt.close(fig2)

def main():
    # Ensure DB exists (ask user to run build_db.py first)
    if not (BASE / "bank.db").exists():
        raise SystemExit("bank.db not found. Run: python scripts/build_db.py")

    df_txn, df_acc, df_cus = load_tables()
    df_txn = add_time_features(df_txn)
    df_join = join_with_customers(df_txn, df_acc, df_cus)

    monthly = kpi_monthly_volume(df_join)
    cust = kpi_customer_summary(df_join)
    top_merchants = kpi_top_merchants(df_join, n=10)

    # Export to Excel with multiple sheets
    out_file = OUTPUT_DIR / "customer_metrics.xlsx"
    with pd.ExcelWriter(out_file, engine="openpyxl") as xw:
        monthly.to_excel(xw, sheet_name="Monthly KPIs", index=False)
        cust.to_excel(xw, sheet_name="Customer Summary", index=False)
        top_merchants.to_excel(xw, sheet_name="Top Merchants", index=False)

    # Make charts
    make_charts(monthly)
    print(f"Wrote: {{out_file}}")
    print(f"Charts in: {{VIS_DIR}}")

if __name__ == "__main__":
    main()
