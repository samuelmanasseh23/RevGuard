import sqlite3
import pandas as pd

conn = sqlite3.connect("database/revguard.db")

# export transactions
transactions = pd.read_sql("SELECT * FROM transactions", conn)
transactions.to_csv("data/processed/transactions_powerbi.csv", index=False)

# export customer risk table
risk = pd.read_sql("SELECT * FROM customer_risk", conn)
risk.to_csv("data/processed/customer_risk_powerbi.csv", index=False)

conn.close()

print("Power BI datasets exported successfully")