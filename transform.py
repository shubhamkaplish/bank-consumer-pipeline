
import pandas as pd

def add_time_features(df_txn: pd.DataFrame) -> pd.DataFrame:
    df = df_txn.copy()
    df['txn_ts'] = pd.to_datetime(df['txn_ts'])
    df['month'] = df['txn_ts'].dt.to_period('M')
    df['abs_amount'] = df['amount'].abs()
    df['flagged_10k'] = df['abs_amount'] > 10_000
    return df

def join_with_customers(df_txn: pd.DataFrame, df_accounts: pd.DataFrame, df_customers: pd.DataFrame) -> pd.DataFrame:
    df = df_txn.merge(df_accounts[['account_id','customer_id','account_type']], on='account_id', how='left')
    df = df.merge(df_customers[['customer_id','first_name','last_name','join_date']], on='customer_id', how='left')
    return df
