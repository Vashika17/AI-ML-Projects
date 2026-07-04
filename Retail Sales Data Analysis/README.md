# Retail Sales Data Analysis — Python + SQL

A small end-to-end data pipeline: **Extract → Load → Query (SQL) → Visualize (Python)**.

## What it does
1. **Extract** — `generate_data.py` creates two raw CSV files, simulating data from a
   source system: `customers.csv` and `sales.csv`.
2. **Load** — `analyze.py` reads the CSVs with pandas and loads them into a real
   SQLite database (`sales.db`) as two tables: `customers` and `sales`.
3. **Query** — runs SQL directly against the database:
   - Top 10 products by revenue (`GROUP BY`, `ORDER BY`, `LIMIT`)
   - Monthly revenue trend (`strftime` date grouping)
   - Region-wise revenue (`JOIN` between `sales` and `customers`)
   - Top 5 customers by spend (`JOIN` + aggregation)
4. **Visualize** — pulls the SQL results back into pandas DataFrames and plots them
   with matplotlib, saving charts to `charts/`.

## How to run
```bash
pip install pandas matplotlib
python generate_data.py   # creates customers.csv and sales.csv
python analyze.py         # loads into SQLite, runs queries, saves charts
```

## Files
- `generate_data.py` — creates the raw CSV data
- `analyze.py` — the pipeline: load → SQL → visualize
- `customers.csv`, `sales.csv` — raw extracted data
- `sales.db` — SQLite database (the "warehouse")
- `charts/` — output PNG charts
