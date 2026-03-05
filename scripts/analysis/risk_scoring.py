import sqlite3
import pandas as pd

conn = sqlite3.connect("database/revguard.db")

# load transactions
query = "SELECT * FROM transactions"
df = pd.read_sql(query, conn)

# calculate anomaly threshold
mean_amount = df["amount"].mean()
std_amount = df["amount"].std()

threshold = mean_amount + 2 * std_amount

df["anomaly"] = df["amount"] > threshold

# group by customer
customer_metrics = df.groupby("customer_id").agg(
    total_transactions=("transaction_id","count"),
    failed_payments=("status", lambda x: (x=="failed").sum()),
    anomalies=("anomaly","sum"),
    total_revenue=("amount","sum")
).reset_index()

# failed payment rate
customer_metrics["failed_rate"] = (
    customer_metrics["failed_payments"] /
    customer_metrics["total_transactions"]
)

# risk scoring formula
customer_metrics["risk_score"] = (
    customer_metrics["failed_rate"] * 0.6 +
    (customer_metrics["anomalies"] > 0).astype(int) * 0.3 +
    (customer_metrics["failed_payments"] > 3).astype(int) * 0.1
)

# classify risk
def classify(score):
    if score > 0.7:
        return "High"
    elif score > 0.4:
        return "Medium"
    else:
        return "Low"

customer_metrics["risk_level"] = customer_metrics["risk_score"].apply(classify)

print("\nCustomer Risk Scores")
print(customer_metrics.head())

# save results
customer_metrics.to_sql(
    "customer_risk",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("\nCustomer risk table created in database")