
import pandas as pd

def kpi_monthly_volume(df: pd.DataFrame) -> pd.DataFrame:
    out = (df.groupby('month', as_index=False)
             .agg(total_amount=('amount','sum'),
                  total_txns=('txn_id','count'),
                  flagged_txns=('flagged_10k','sum')))
    # Ensure month is string for Excel friendliness
    out['month'] = out['month'].astype(str)
    return out

def kpi_customer_summary(df: pd.DataFrame) -> pd.DataFrame:
    out = (df.groupby(['customer_id','first_name','last_name'], as_index=False)
             .agg(total_amount=('amount','sum'),
                  avg_txn=('amount','mean'),
                  txns=('txn_id','count'),
                  flagged_txns=('flagged_10k','sum')))
    return out

def kpi_top_merchants(df: pd.DataFrame, n:int=10) -> pd.DataFrame:
    out = (df[df['amount']<0]
             .groupby('merchant', as_index=False)
             .agg(spend=('amount','sum'), txns=('txn_id','count'))
             .sort_values('spend'))  # spend is negative, more negative = larger spend
    return out.head(n)
