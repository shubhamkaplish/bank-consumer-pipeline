-- Sample data (small but realistic-ish)
BEGIN TRANSACTION;

INSERT INTO customers (customer_id, first_name, last_name, email, join_date) VALUES
(101, 'Alex', 'Carter', 'alex.carter@example.com', '2022-03-15'),
(102, 'Maria', 'Singh', 'maria.singh@example.com', '2023-08-01'),
(103, 'James', 'Nguyen', 'james.nguyen@example.com', '2021-11-20'),
(104, 'Priya', 'Patel', 'priya.patel@example.com', '2024-01-05');

INSERT INTO accounts (account_id, customer_id, account_type, open_date, status) VALUES
(1001, 101, 'checking', '2022-03-16', 'active'),
(1002, 101, 'savings',  '2022-03-16', 'active'),
(1003, 102, 'checking', '2023-08-02', 'active'),
(1004, 103, 'credit',   '2022-01-15', 'active'),
(1005, 104, 'checking', '2024-01-06', 'active');

-- Transactions across several months (small set)
INSERT INTO transactions (txn_id, account_id, amount, txn_type, merchant, txn_ts, channel) VALUES
(1, 1001,  2500.00, 'deposit',    'Employer Pty', '2025-01-31 09:01:00', 'online'),
(2, 1001,  -120.45, 'purchase',   'Woolworths',   '2025-02-01 18:21:00', 'online'),
(3, 1001,  -65.00,  'withdrawal', 'ATM-123',      '2025-02-03 07:45:00', 'atm'),
(4, 1002,   10.25,  'interest',   'Bank',         '2025-02-28 23:55:00', 'online'),
(5, 1003,  3800.00, 'deposit',    'ContractorCo', '2025-03-01 10:05:00', 'online'),
(6, 1003,  -950.00, 'purchase',   'JB Hi-Fi',     '2025-03-02 14:10:00', 'online'),
(7, 1003,  -120.00, 'fee',        'Monthly Fee',  '2025-03-31 23:59:00', 'online'),
(8, 1004, -1600.00, 'purchase',   'Qantas',       '2025-04-04 12:00:00', 'online'),
(9, 1004,  1600.00, 'transfer_in','Checking',     '2025-04-05 09:00:00', 'online'),
(10,1005,  4200.00, 'deposit',    'Employer Pty', '2025-05-01 08:59:00', 'online'),
(11,1005,  -300.00, 'purchase',   'Coles',        '2025-05-02 19:45:00', 'online'),
(12,1005,  -25.00,  'withdrawal', 'ATM-987',      '2025-05-03 11:30:00', 'atm'),
(13,1001,  2500.00, 'deposit',    'Employer Pty', '2025-06-30 09:02:00', 'online'),
(14,1001,  -80.00,  'purchase',   '7-Eleven',     '2025-07-05 08:10:00', 'online'),
(15,1002,   10.40,  'interest',   'Bank',         '2025-07-31 23:55:00', 'online'),
(16,1003,  40000.00,'deposit',    'Bonus',        '2025-08-01 09:05:00', 'online'),
(17,1003, -12000.00,'purchase',   'HarveyNorman', '2025-08-03 13:05:00', 'online'),
(18,1005,  -500.00, 'transfer_out','Savings',     '2025-08-15 15:15:00', 'online'),
(19,1004,  -75.00,  'fee',        'Late Fee',     '2025-08-28 12:00:00', 'online'),
(20,1005,  4300.00, 'deposit',    'Employer Pty', '2025-09-01 08:59:00', 'online'),
(21,1005,  -900.00, 'purchase',   'IKEA',         '2025-09-02 10:35:00', 'online'),
(22,1005,  -70.00,  'withdrawal', 'ATM-111',      '2025-09-03 17:10:00', 'atm'),
(23,1001,  -45.00,  'fee',        'Overdraft',    '2025-09-07 22:05:00', 'online'),
(24,1002,   10.55,  'interest',   'Bank',         '2025-09-30 23:55:00', 'online');

COMMIT;
