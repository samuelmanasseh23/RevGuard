import pandas as pd
import random
from datetime import datetime, timedelta

num_transactions = 2000

customers = [f"C{str(i).zfill(3)}" for i in range(1,101)]
regions = ["India","US","UK","Germany","Singapore"]
plans = ["Basic","Pro","Enterprise"]
payment_methods = ["card","upi","bank"]

start_date = datetime(2024,1,1)

data = []

for i in range(num_transactions):

    transaction_id = f"T{str(i+1).zfill(5)}"
    customer_id = random.choice(customers)

    date = start_date + timedelta(days=random.randint(0,180))

    plan = random.choice(plans)

    if plan == "Basic":
        amount = random.choice([99,120,150])
    elif plan == "Pro":
        amount = random.choice([250,300,350])
    else:
        amount = random.choice([700,900,1200])

    status = random.choices(
        ["success","failed"],
        weights=[0.9,0.1]
    )[0]

    payment_method = random.choice(payment_methods)
    region = random.choice(regions)

    data.append([
        transaction_id,
        customer_id,
        date.date(),
        amount,
        status,
        payment_method,
        region,
        plan
    ])

columns = [
    "transaction_id",
    "customer_id",
    "transaction_date",
    "amount",
    "status",
    "payment_method",
    "region",
    "plan"
]

df = pd.DataFrame(data, columns=columns)

df.to_csv("data/raw/transactions.csv", index=False)

print("Dataset generated successfully")