import pandas as pd
import psycopg2
from pgvector.psycopg2 import register_vector

conn = psycopg2.connect(
    host="localhost",
    database="assignment_db",
    user="postgres",
    password="12345",
    port="5432"
)

register_vector(conn)
cursor = conn.cursor()

print("Connected successfully!")

cursor.execute("CREATE EXTENSION IF NOT EXISTS vector;")
conn.commit()

cursor.execute("""
CREATE TABLE IF NOT EXISTS transactions (
    txn_id VARCHAR(20) PRIMARY KEY,
    account_id VARCHAR(20),
    txn_ts TIMESTAMP,
    amount FLOAT,
    currency VARCHAR(10),
    narration TEXT,
    embedding VECTOR(5)
);
""")
conn.commit()

print("Table created successfully!")

cursor.execute("TRUNCATE TABLE transactions;")
conn.commit()

print("Old data cleared!")

df = pd.read_csv("cleaned_transactions.csv")

for _, row in df.iterrows():

    embedding = [1.0, 2.0, 3.0, 4.0, 5.0]

    cursor.execute("""
    INSERT INTO transactions
    (txn_id, account_id, txn_ts, amount, currency, narration, embedding)
    VALUES (%s, %s, %s, %s, %s, %s, %s)
    """, (
        str(row["txn_id"]),
        str(row["account_id"]),
        str(row["txn_ts"]),
        float(row["amount"]),
        str(row["currency"]),
        str(row["narration"]),
        embedding
    ))

conn.commit()

print("All rows inserted successfully!")

cursor.execute("SELECT COUNT(*) FROM transactions;")
count = cursor.fetchone()[0]
print("Rows in table:", count)

cursor.execute("""
SELECT txn_id, narration
FROM transactions
ORDER BY embedding <-> '[1,2,3,4,5]'
LIMIT 5;
""")

rows = cursor.fetchall()

print("\nNearest Transactions:")

for r in rows:
    print(r)

cursor.close()
conn.close()