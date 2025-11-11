# Customer Retention Analysis  
Analyzing customer retention and cohort behavior using data sourced from **BigQuery’s public `thelook_ecommerce` dataset**, explored locally with **Python + Pandas**.  

---

## Project Overview
This project examines how customer cohorts behave over time — tracking retention, churn, and purchasing frequency.  
It’s built as a hybrid **SQL + Python project**: the data originates from BigQuery via SQL, but all analysis and visualization are performed locally using pandas.  

---

## Data Source
The dataset comes from Google’s public **BigQuery dataset**:  
`bigquery-public-data.thelook_ecommerce.orders`  

Steps:
1. Queried `thelook_ecommerce.orders` in BigQuery using SQL.  
2. Exported results to CSV (`thelook_orders.csv`).  
3. Loaded and analyzed data locally in Python.

---

## ⚙️ Project Structure
