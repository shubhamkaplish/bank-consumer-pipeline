-- Schema for a simple banking consumer dataset
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS accounts;
DROP TABLE IF EXISTS transactions;

CREATE TABLE customers (
    customer_id INTEGER PRIMARY KEY,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT,
    join_date DATE
);

CREATE TABLE accounts (
    account_id INTEGER PRIMARY KEY,
    customer_id INTEGER NOT NULL,
    account_type TEXT CHECK(account_type IN ('checking','savings','credit')),
    open_date DATE,
    status TEXT CHECK(status IN ('active','closed')) DEFAULT 'active',
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);

CREATE TABLE transactions (
    txn_id INTEGER PRIMARY KEY,
    account_id INTEGER NOT NULL,
    amount NUMERIC NOT NULL, -- positive=credit, negative=debit
    txn_type TEXT CHECK(txn_type IN ('deposit','withdrawal','purchase','transfer_in','transfer_out','fee','interest')),
    merchant TEXT,
    txn_ts TIMESTAMP NOT NULL,
    channel TEXT CHECK(channel IN ('branch','online','mobile','atm')),
    FOREIGN KEY (account_id) REFERENCES accounts(account_id)
);

CREATE INDEX IF NOT EXISTS idx_txn_account_ts ON transactions(account_id, txn_ts);
