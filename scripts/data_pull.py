# scripts/data_pull.py
import pandas as pd

def load_data(project_id: str, sql_file: str) -> pd.DataFrame:
    """Loads the local BigQuery dataset CSV."""
    return pd.read_csv("../data/bq-ecom.csv")
