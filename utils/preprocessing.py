# utils/preprocessing.py

import pandas as pd

def clean_ev_data(df: pd.DataFrame):
    """Clean EV Dataset by removing duplicates and fixing column names."""
    df = df.copy()
    df.columns = df.columns.str.strip()
    df.drop_duplicates(inplace=True)
    return df

def select_model_features(df: pd.DataFrame, cols):
    """Select only the required model features."""
    df = clean_ev_data(df)
    return df[cols].dropna()
