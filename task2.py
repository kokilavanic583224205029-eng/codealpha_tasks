# unemployment_analysis.py
"""
Unemployment Analysis
- Loads a CSV with unemployment data (Date, Region, Unemployment_Rate)
- Cleans data, explores, visualizes trends
- Analyses COVID-19 (2020-01-01 to 2021-12-31) impact
- Detects seasonal patterns via monthly aggregation and seasonal_decompose (when available)
- Saves outputs to outputs/ directory
Usage:
    python unemployment_analysis.py --file unemployment_data.csv
"""

import os
import argparse
from datetime import datetime
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(style="whitegrid", context="talk")

# Optional: seasonal decomposition
try:
    from statsmodels.tsa.seasonal import seasonal_decompose
    HAS_STATS = True
except Exception:
    HAS_STATS = False

def load_dataset(path):
    # Try reading CSV
    df = pd.read_csv(path)
    # Normalize column names (lowercase, remove spaces)
    df.columns = [c.strip().lower().replace(' ', '_') for c in df.columns]
    return df

def find_columns(df):
    # Identify likely date, rate and region columns by common names   
    date_cols = [c for c in df.columns if 'date' in c or 'year' in c or 'month' in c]
    rate_cols = [c for c in df.columns if 'unemploy' in c or 'unemployment' in c or 'rate' == c or 'unemployment_rate' in c]
    region_cols = [c for c in df.columns if 'region' in c or 'country' in c or 'state' in c or 'area' in c]
    date_col = date_cols[0] if date_cols else None
    rate_col = rate_cols[0] if rate_cols else None
    region_col = region_cols[0] if region_cols else None
    return date_col, rate_col, region_col

def preprocess(df, date_col, rate_col, region_col):
    # Parse dates
    if date_col is None:
        raise ValueError("Could not find a date column. Make sure your CSV has a date column.")
    df[date_col] = pd.to_datetime(df[date_col], errors='coerce')
    # Drop rows with invalid dates
    df = df.dropna(subset=[date_col]).copy()
    # If rate isn't numeric, coerce
    if rate_col is None:
        # Try to guess: a numeric column that's n
