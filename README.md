# Financial Data Processing Pipeline

## Overview

This project implements a simple financial data processing pipeline using Python. It reads transaction data from an Excel file, cleans and validates it, performs analytics, stores the processed data in PostgreSQL with pgvector support, and provides a basic Django dashboard for viewing processing information.

---
![alt text](<Screenshot 2026-07-07 032123.png>) ![alt text](<Screenshot 2026-07-07 032057.png>)
## Features

### A. Excel Processing (Pandas)

* Read Excel (.xlsx) files
* Validate data
* Handle missing values
* Convert columns to correct data types
* Save cleaned data

### B. Data Analysis (Polars)

* Read cleaned data using Polars LazyFrame
* Perform simple aggregations
* Generate summary statistics

### C. Serialization

* Save processed DataFrame as a Pickle file
* Load Pickle file back into memory

### D. PostgreSQL + pgvector

* Create a PostgreSQL database
* Store cleaned transaction data
* Store vector embeddings
* Perform basic vector similarity search

### E. Django Dashboard

* Display latest processed file
* Display dataset metrics
* Provide an endpoint to trigger processing

### F. File Listener

* Poll for new files
* Avoid duplicate processing (idempotent)
* Read configuration from environment variables

### G. Bash Scripts

* Start the application
* Run health check

---

## Project Structure

```
python_assignment/
│
├── app/
│   ├── generate_data.py
│   ├── ingestion.py
│   ├── analytics.py
│   ├── pickle_operations.py
│   ├── database.py
│   └── listener.py
│
├── assignment_site/
│
├── transactions.xlsx
├── cleaned_transactions.csv
├── processed_df_v1.pkl
├── requirements.txt
├── run.sh
├── health_check.sh
└── README.md
```

---

## Technologies Used

* Python
* Pandas
* Polars
* PostgreSQL
* pgvector
* Django
* Pickle

---

## Installation

Install the required packages.

```bash
pip install -r requirements.txt
```

---

## Running the Project

Generate sample data:

```bash
python app/generate_data.py
```

Clean and process data:

```bash
python app/ingestion.py
```

Run analytics:

```bash
python app/analytics.py
```

Serialize data:

```bash
python app/pickle_operations.py
```

Store data in PostgreSQL:

```bash
python app/database.py
```

Run Django server:

```bash
cd assignment_site
python manage.py runserver
```

Run the listener:

```bash
python app/listener.py
```

---

