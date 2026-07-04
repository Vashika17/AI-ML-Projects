"""
generate_data.py
-----------------
Creates a synthetic telecom customer churn dataset (customer_churn.csv)
with realistic features and a churn label that depends on those features
(with some randomness), so the ML model has real signal to learn from.
"""

import csv
import random

random.seed(7)

N = 800  # number of customers

CONTRACTS = ["Month-to-month", "One year", "Two year"]
INTERNET = ["DSL", "Fiber optic", "No"]
YES_NO = ["Yes", "No"]

rows = []
for cust_id in range(1, N + 1):
    tenure_months = random.randint(0, 72)
    contract = random.choice(CONTRACTS)
    internet_service = random.choice(INTERNET)
    tech_support = random.choice(YES_NO)
    online_security = random.choice(YES_NO)
    monthly_charges = round(random.uniform(20, 120), 2)
    total_charges = round(monthly_charges * max(tenure_months, 1) * random.uniform(0.9, 1.05), 2)
    senior_citizen = random.choice([0, 1])
    paperless_billing = random.choice(YES_NO)
    payment_method = random.choice(["Electronic check", "Mailed check", "Bank transfer", "Credit card"])

    # ---- churn probability logic (this is what the model has to learn) ----
    churn_score = 0.0
    if contract == "Month-to-month":
        churn_score += 0.35
    elif contract == "One year":
        churn_score += 0.10
    if tenure_months < 12:
        churn_score += 0.25
    if tech_support == "No":
        churn_score += 0.15
    if online_security == "No":
        churn_score += 0.10
    if monthly_charges > 80:
        churn_score += 0.15
    if internet_service == "Fiber optic":
        churn_score += 0.05
    if senior_citizen == 1:
        churn_score += 0.05
    churn_score += random.uniform(-0.15, 0.15)  # noise

    churn = "Yes" if churn_score > 0.45 else "No"

    rows.append([
        cust_id, senior_citizen, tenure_months, contract, internet_service,
        tech_support, online_security, paperless_billing, payment_method,
        monthly_charges, total_charges, churn
    ])

with open("customer_churn.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerow([
        "customer_id", "senior_citizen", "tenure_months", "contract",
        "internet_service", "tech_support", "online_security",
        "paperless_billing", "payment_method", "monthly_charges",
        "total_charges", "churn"
    ])
    writer.writerows(rows)

churn_rate = sum(1 for r in rows if r[-1] == "Yes") / N
print(f"Generated customer_churn.csv with {N} rows. Churn rate: {churn_rate:.1%}")