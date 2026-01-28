import pandas as pd
import os

# -------------------------------------------------
# Ensure output directory exists
# -------------------------------------------------
os.makedirs("data/processed", exist_ok=True)

# -------------------------------------------------
# Load raw data
# -------------------------------------------------
customers = pd.read_csv("data/raw/customers.csv")
transactions = pd.read_csv("data/raw/transactions.csv")
usage = pd.read_csv("data/raw/usage_logs.csv")
tickets = pd.read_csv("data/raw/support_tickets.csv")

# -------------------------------------------------
# Convert dates safely (mixed formats handled)
# -------------------------------------------------
customers["join_date"] = pd.to_datetime(
    customers["join_date"], errors="coerce"
)
customers["last_active_date"] = pd.to_datetime(
    customers["last_active_date"], errors="coerce"
)

transactions["payment_date"] = pd.to_datetime(
    transactions["payment_date"], errors="coerce"
)

usage["usage_date"] = pd.to_datetime(
    usage["usage_date"], errors="coerce"
)

# -------------------------------------------------
# Revenue per customer
# -------------------------------------------------
revenue = (
    transactions[transactions["status"] == "Success"]
    .groupby("customer_id")["amount"]
    .sum()
    .reset_index(name="total_revenue")
)

# -------------------------------------------------
# Failed payments (revenue leakage signal)
# -------------------------------------------------
failed_payments = (
    transactions[transactions["status"] == "Failed"]
    .groupby("customer_id")
    .size()
    .reset_index(name="failed_payments")
)

# -------------------------------------------------
# Usage summary
# -------------------------------------------------
usage_summary = (
    usage.groupby("customer_id")["usage_hours"]
    .sum()
    .reset_index(name="total_usage_hours")
)

# -------------------------------------------------
# Support burden
# -------------------------------------------------
ticket_summary = (
    tickets.groupby("customer_id")["resolution_time_hours"]
    .mean()
    .reset_index(name="avg_resolution_time")
)

# -------------------------------------------------
# Merge everything
# -------------------------------------------------
final_df = (
    customers
    .merge(revenue, on="customer_id", how="left")
    .merge(failed_payments, on="customer_id", how="left")
    .merge(usage_summary, on="customer_id", how="left")
    .merge(ticket_summary, on="customer_id", how="left")
)

# -------------------------------------------------
# Fill missing values ONLY for numeric columns
# -------------------------------------------------
numeric_cols = final_df.select_dtypes(include="number").columns
final_df[numeric_cols] = final_df[numeric_cols].fillna(0)

# -------------------------------------------------
# Save processed data
# -------------------------------------------------
final_df.to_csv("data/processed/customer_analytics.csv", index=False)

print("ETL completed. Processed file created.")
