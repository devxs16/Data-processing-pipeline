import pandas as pd
import pickle

df = pd.read_csv("cleaned_transactions.csv")

filename = "processed_df_v1.pkl"

with open(filename, "wb") as file:
    pickle.dump(df, file)

print("Pickle file created.")

with open(filename, "rb") as file:
    loaded_df = pickle.load(file)

print("Pickle file loaded.")
if len(df) == len(loaded_df):
    print("Row count matches.")
else:
    print("Row count does not match.")

if df.equals(loaded_df):
    print("Data integrity verified.")
else:
    print("Data mismatch found.")