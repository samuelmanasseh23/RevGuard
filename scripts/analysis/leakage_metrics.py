import pandas as pd

# Load processed data
df = pd.read_csv("data/processed/customer_analytics.csv")

# Normalize helper function
def normalize(series):
    return (series - series.min()) / (series.max() - series.min() + 1e-6)

# Leakage components
df["failed_payment_score"] = normalize(df["failed_payments"])
df["low_usage_score"] = 1 - normalize(df["total_usage_hours"])
df["support_risk_score"] = normalize(df["avg_resolution_time"])

# Final leakage score (weighted)
df["leakage_score"] = (
    0.4 * df["failed_payment_score"] +
    0.3 * df["low_usage_score"] +
    0.3 * df["support_risk_score"]
)

# Risk category
df["risk_level"] = pd.cut(
    df["leakage_score"],
    bins=[-1, 0.3, 0.6, 1.1],
    labels=["Low", "Medium", "High"]
)

# Save for dashboarding
df.to_csv("data/processed/leakage_analysis.csv", index=False)

print("Leakage metrics calculated.")