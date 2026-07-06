import pandas as pd
import random
from datetime import datetime, timedelta

data = []

for i in range(1000):
    data.append({
        "txn_id": f"TXN{i+1}",
        "account_id": f"ACC{random.randint(1,50)}",
        "txn_ts": datetime.now() - timedelta(days=random.randint(0,30)),
        "amount": round(random.uniform(100,10000), 2),
        "currency": "INR",
        "narration": random.choice([
            "Salary",
            "Shopping",
            "Fuel",
            "Transfer",
            "Restaurant"
        ])
    })

df = pd.DataFrame(data)

df.to_excel("transactions.xlsx", index=False)

print("Excel file created successfully!")