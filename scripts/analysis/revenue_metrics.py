import sqlite3
import pandas as pd

conn = sqlite3.connect("database/revguard.db")

# TOTAL REVENUE
total_revenue_query = """
SELECT SUM(amount) AS total_revenue
FROM transactions
WHERE status = 'success'
"""

total_revenue = pd.read_sql(total_revenue_query, conn)
print("\nTotal Revenue")
print(total_revenue)


# FAILED PAYMENTS
failed_query = """
SELECT COUNT(*) AS failed_payments
FROM transactions
WHERE status = 'failed'
"""

failed_payments = pd.read_sql(failed_query, conn)
print("\nFailed Payments")
print(failed_payments)


# SUCCESSFUL PAYMENTS
success_query = """
SELECT COUNT(*) AS successful_payments
FROM transactions
WHERE status = 'success'
"""

successful_payments = pd.read_sql(success_query, conn)
print("\nSuccessful Payments")
print(successful_payments)


# REVENUE BY REGION
region_query = """
SELECT region, SUM(amount) AS revenue
FROM transactions
WHERE status = 'success'
GROUP BY region
ORDER BY revenue DESC
"""

revenue_region = pd.read_sql(region_query, conn)
print("\nRevenue by Region")
print(revenue_region)


# REVENUE BY PLAN
plan_query = """
SELECT plan, SUM(amount) AS revenue
FROM transactions
WHERE status = 'success'
GROUP BY plan
ORDER BY revenue DESC
"""

revenue_plan = pd.read_sql(plan_query, conn)
print("\nRevenue by Plan")
print(revenue_plan)

conn.close()