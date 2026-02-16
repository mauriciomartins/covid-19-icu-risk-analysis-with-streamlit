"""
Main entry point for the Streamlit application. This script loads and preprocesses the data, then renders the Streamlit interface.
"""

import streamlit as st
import re
import requests
import urllib3
from io import BytesIO
import pandas as pd

# =====================================================
# DATA LOADING
# =====================================================

DATA_URL = "https://raw.githubusercontent.com/mauriciomartins/covid-19-icu-risk-analysis/main/Kaggle_Sirio_Libanes_ICU_Prediction.xlsx"


def load_data(url: str) -> pd.DataFrame:
    """
    Downloads and loads the Excel dataset from a remote URL.
    """
    try:
        response = requests.get(url, timeout=30)
        response.raise_for_status()
        return pd.read_excel(BytesIO(response.content))
    except Exception:
        urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
        response = requests.get(url, verify=False, timeout=30)
        response.raise_for_status()
        return pd.read_excel(BytesIO(response.content))


# =====================================================
# DATA CLEANING & FEATURE ENGINEERING
# =====================================================

def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Cleans and prepares dataset:
    - Removes redundant statistical columns
    - Creates age_group and numeric age features
    """

    df = df.copy()

    # Remove redundant statistical aggregations
    remove_patterns = ("_DIFF", "_MIN", "_MAX", "_MEDIAN")
    remove_cols = [col for col in df.columns if col.endswith(remove_patterns)]

    df.drop(columns=remove_cols)

    # Create age_group
    df["AGE_ABOVE65"] = df["AGE_ABOVE65"].map({1: "AGE +65", 0: "AGE <65"})

    # Extract numeric age from AGE_PERCENTIL
    df["age"] = df["AGE_PERCENTIL"].apply(
        lambda x: float(re.sub(r"[^\d.]", "", str(x)))
    )

    df["ICU_LABEL"] = df["ICU"].map({1: "YES", 0: "NO"})

    return df

# =====================================================
# Streamlit screen
# =====================================================
def render_streamlit(df):
    st.title("COVID-19 ICU Risk Analysis")
    st.write("Exploratory analysis and visualization of COVID-19 ICU admission data.")
    st.write(df)
    st.write("### Dataset Summary")
    st.write(st.session_state["df"].describe())


# =====================================================
# MAIN EXECUTION
# =====================================================
def main():
    st.set_page_config(layout="wide")
    if "df" not in st.session_state:
        st.warning("No data loaded. Please go back to the home page.")
        df = load_data(DATA_URL)
        df = preprocess_data(df)
        st.session_state["df"] = df 
    
    render_streamlit(st.session_state["df"])


if __name__ == "__main__":
    main()
