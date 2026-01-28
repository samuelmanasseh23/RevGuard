# Revenue Leakage Analytics & Risk Prioritization Dashboard

## 🔹 Problem Statement
SaaS companies lose revenue not only through churn, but also through hidden revenue leakage caused by failed payments, low product usage, and high support costs.  
These signals are often analyzed in isolation, making it difficult to identify which customers actually pose the highest revenue risk.

This project identifies high-risk customers and helps teams prioritize retention and recovery efforts.

---

## 🔹 Solution Overview
This project implements an end-to-end analytics workflow to surface revenue leakage risk:

- Built an automated ETL pipeline to clean, transform, and aggregate customer, transaction, usage, and support data.
- Engineered a customer-level leakage risk score using operational and financial indicators.
- Designed an executive Power BI dashboard to visualize KPIs, customer rankings, and overall risk distribution.

The focus is on decision-ready insights rather than exploratory analysis.

---

## 🔹 Tech Stack
- Python (pandas)
- Power BI
- CSV-based data modeling
- SQL-style aggregations using pandas

---

## 🔹 Key Metrics
- Total Revenue
- Failed Payments
- Leakage Risk Score
- High-Risk Customer Count

---

## 🔹 Dashboard Highlights
- Executive KPI overview for rapid assessment
- Customer-level leakage risk ranking
- Risk distribution by severity (High / Low)
- Interactive filtering by plan and region

The dashboard is designed so stakeholders can identify who to act on within seconds.

---

## 🔹 Business Impact
- Helps revenue and customer success teams focus on the customers that matter most
- Surfaces hidden revenue risk early instead of reacting after churn
- Demonstrates how operational data can be converted into actionable business insights

---

## 🔹 How to Run
1. Run the ETL pipeline:
2. Load the processed CSV files into Power BI
3. Open the Power BI report to explore the dashboard
