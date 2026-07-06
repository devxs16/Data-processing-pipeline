import pandas as pd

df = pd.read_excel("transactions.xlsx")

print(df.head())

expected_columns = [
    "txn_id",
    "account_id",
    "txn_ts",
    "amount",
    "currency",
    "narration"
]

for column in expected_columns:
    if column not in df.columns:
        print(f"{column} is missing")

print("Schema is valid")

df["txn_ts"] = pd.to_datetime(df["txn_ts"], errors="coerce")
df["amount"] = pd.to_numeric(df["amount"], errors="coerce")

print(df.isnull().sum())

df = df.dropna(subset=["amount", "txn_ts"])
df["narration"] = df["narration"].fillna("Unknown")
df["currency"] = df["currency"].fillna("INR")
df = df.drop_duplicates(subset=["txn_id"])

print(df.info())
print(df.head())

df.to_excel("cleaned_transactions.xlsx", index=False)
df.to_csv("cleaned_transactions.csv", index=False)
print("Data cleaned and saved successfully!")