import pandas as pd
import streamlit as st

@st.cache_data
def load_data(path: str = "data/superstore.csv") -> pd.DataFrame:
    df = pd.read_csv(path)
    df.columns = df.columns.str.strip()
    df["Order Date"] = pd.to_datetime(df["Order Date"], format="%d-%m-%Y", dayfirst=False, errors="coerce")
    df["Ship Date"]  = pd.to_datetime(df["Ship Date"],  format="%d-%m-%Y", dayfirst=False, errors="coerce")
    return df