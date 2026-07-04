"""
generate_data.py
-----------------
Creates a small, realistic retail dataset as two CSV files:
  - customers.csv  (customer_id, customer_name, region)
  - sales.csv       (order_id, order_date, customer_id, product, category, quantity, unit_price)

This simulates "raw data from a source system" so the rest of the
project can demonstrate a real extract -> load -> query -> visualize flow.
"""

import csv
import random
from datetime import date, timedelta

random.seed(42)

REGIONS = ["North", "South", "East", "West"]

CUSTOMER_FIRST = ["Aarav", "Priya", "Rohan", "Sneha", "Karthik", "Divya",
                   "Arjun", "Meera", "Vikram", "Anitha", "Suresh", "Kavya"]
CUSTOMER_LAST = ["Kumar", "Sharma", "Iyer", "Reddy", "Nair", "Patel",
                  "Menon", "Rao", "Pillai", "Das"]

PRODUCTS = [
    ("Wireless Mouse", "Electronics", 599),
    ("Bluetooth Speaker", "Electronics", 1499),
    ("Laptop Bag", "Accessories", 899),
    ("Office Chair", "Furniture", 4999),
    ("Study Lamp", "Furniture", 799),
    ("Notebook Set", "Stationery", 199),
    ("Water Bottle", "Lifestyle", 349),
    ("Running Shoes", "Footwear", 2499),
    ("Yoga Mat", "Fitness", 699),
    ("Smart Watch", "Electronics", 3499),
    ("Backpack", "Accessories", 1299),
    ("Desk Organizer", "Stationery", 299),
]

# ---- customers.csv ----
NUM_CUSTOMERS = 40
customers = []
for cid in range(1, NUM_CUSTOMERS + 1):
    name = f"{random.choice(CUSTOMER_FIRST)} {random.choice(CUSTOMER_LAST)}"
    region = random.choice(REGIONS)
    customers.append((cid, name, region))

with open("customers.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["customer_id", "customer_name", "region"])
    writer.writerows(customers)

# ---- sales.csv ----
NUM_ORDERS = 500
start_date = date(2025, 1, 1)
end_date = date(2025, 12, 31)
day_range = (end_date - start_date).days

with open("sales.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow(["order_id", "order_date", "customer_id", "product",
                      "category", "quantity", "unit_price"])
    for order_id in range(1, NUM_ORDERS + 1):
        order_date = start_date + timedelta(days=random.randint(0, day_range))
        customer_id = random.randint(1, NUM_CUSTOMERS)
        product, category, price = random.choice(PRODUCTS)
        quantity = random.randint(1, 5)
        writer.writerow([order_id, order_date.isoformat(), customer_id,
                          product, category, quantity, price])

print(f"Generated customers.csv ({NUM_CUSTOMERS} rows) and sales.csv ({NUM_ORDERS} rows)")
