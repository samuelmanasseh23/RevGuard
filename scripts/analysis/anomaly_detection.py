import sqlite3
import pandas as pd

# connect to database
conn = sqlite3.connect("database/revguard.db")

# load transaction data
query = "SELECT * FROM transactions"
df = pd.read_sql(query, conn)

# compute statistics
mean_amount = df["amount"].mean()
std_amount = df["amount"].std()

threshold = mean_amount + 2 * std_amount

print(f"Average transaction amount: {mean_amount:.2f}")
print(f"Standard deviation: {std_amount:.2f}")
print(f"Anomaly threshold: {threshold:.2f}")

# detect anomalies
df["anomaly"] = df["amount"] > threshold

anomalies = df[df["anomaly"] == True]

print("\nPotential Revenue Anomalies")
print(anomalies[["transaction_id","customer_id","amount","region","plan"]])

conn.close()