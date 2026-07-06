import os
import time
from dotenv import load_dotenv

load_dotenv()

processed_files = set()

while True:

    remote_files = [
        "transactions1.xlsx",
        "transactions2.xlsx"
    ]

    for file in remote_files:

        if file not in processed_files:

            print(f"Processing {file}")

            processed_files.add(file)

    time.sleep(10)