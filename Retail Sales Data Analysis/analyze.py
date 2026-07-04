"""
analyze.py
----------
A simple Python + SQL data pipeline:

  1. EXTRACT : read raw CSVs (customers.csv, sales.csv)
  2. LOAD    : load them into a SQLite database (sales.db) as real tables
  3. QUERY   : run SQL (joins, aggregations, GROUP BY) to answer business questions
  4. VISUALIZE: pull query results back into pandas and plot charts with matplotlib

Run:  python analyze.py
Output: sales.db, and PNG charts in the charts/ folder.
"""

import os
import sqlite3
import pandas as pd
import matplotlib.pyplot as plt

DB_PATH = "sales.db"
CHART_DIR = "charts"
os.makedirs(CHART_DIR, exist_ok=True)

# ------------------------------------------------------------------
# 1 & 2. EXTRACT + LOAD: read CSVs with pandas, load into SQLite
# ------------------------------------------------------------------
customers_df = pd.read_csv("customers.csv")
sales_df = pd.read_csv("sales.csv")

conn = sqlite3.connect(DB_PATH)
customers_df.to_sql("customers", conn, if_exists="replace", index=False)
sales_df.to_sql("sales", conn, if_exists="replace", index=False)

print(f"Loaded {len(customers_df)} customers and {len(sales_df)} sales records into {DB_PATH}")

# ------------------------------------------------------------------
# 3. QUERY: plain SQL against the database
# ------------------------------------------------------------------

# Q1: Top 10 products by revenue
q1 = """
SELECT product,
       SUM(quantity * unit_price) AS revenue
FROM sales
GROUP BY product
ORDER BY revenue DESC
LIMIT 10;
"""
top_products = pd.read_sql_query(q1, conn)

# Q2: Month-wise revenue trend
q2 = """
SELECT strftime('%Y-%m', order_date) AS month,
       SUM(quantity * unit_price) AS revenue
FROM sales
GROUP BY month
ORDER BY month;
"""
monthly_revenue = pd.read_sql_query(q2, conn)

# Q3: Region-wise revenue (JOIN sales with customers)
q3 = """
SELECT c.region,
       SUM(s.quantity * s.unit_price) AS revenue
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.region
ORDER BY revenue DESC;
"""
region_revenue = pd.read_sql_query(q3, conn)

# Q4: Top 5 customers by total spend (JOIN + aggregation)
q4 = """
SELECT c.customer_name,
       c.region,
       SUM(s.quantity * s.unit_price) AS total_spend
FROM sales s
JOIN customers c ON s.customer_id = c.customer_id
GROUP BY c.customer_id
ORDER BY total_spend DESC
LIMIT 5;
"""
top_customers = pd.read_sql_query(q4, conn)

conn.close()

print("\nTop 10 products by revenue:\n", top_products)
print("\nMonthly revenue trend:\n", monthly_revenue)
print("\nRegion-wise revenue:\n", region_revenue)
print("\nTop 5 customers by spend:\n", top_customers)

# ------------------------------------------------------------------
# 4. VISUALIZE: matplotlib charts saved as PNG
# ------------------------------------------------------------------

# Chart 1: Top 10 products by revenue (bar chart)
plt.figure(figsize=(9, 5))
plt.barh(top_products["product"], top_products["revenue"], color="#2E75B6")
plt.xlabel("Revenue (₹)")
plt.title("Top 10 Products by Revenue")
plt.gca().invert_yaxis()
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/top_products.png", dpi=120)
plt.close()

# Chart 2: Monthly revenue trend (line chart)
plt.figure(figsize=(9, 5))
plt.plot(monthly_revenue["month"], monthly_revenue["revenue"], marker="o", color="#2E75B6")
plt.xticks(rotation=45)
plt.ylabel("Revenue (₹)")
plt.title("Monthly Revenue Trend (2025)")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/monthly_revenue.png", dpi=120)
plt.close()

# Chart 3: Region-wise revenue (bar chart)
plt.figure(figsize=(7, 5))
plt.bar(region_revenue["region"], region_revenue["revenue"], color="#70AD47")
plt.ylabel("Revenue (₹)")
plt.title("Revenue by Region")
plt.tight_layout()
plt.savefig(f"{CHART_DIR}/region_revenue.png", dpi=120)
plt.close()

print(f"\nCharts saved in ./{CHART_DIR}/")