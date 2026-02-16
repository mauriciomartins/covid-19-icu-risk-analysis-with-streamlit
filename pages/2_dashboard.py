"""
COVID-19 ICU Risk Analysis
Author: Mauricio Martins

This script performs exploratory analysis and visualization
of COVID-19 ICU admission data from the Kaggle Sírio-Libanês dataset.
"""
from io import BytesIO

import pandas as pd
import streamlit as st
import plotly.express as px
# =====================================================
# PATIENT-LEVEL AGGREGATION
# =====================================================

def aggregate_patient_level(df: pd.DataFrame) -> pd.DataFrame:
    """
    Collapses dataset to one row per patient
    to avoid window duplication bias.
    """
    return (
        df.groupby("PATIENT_VISIT_IDENTIFIER")
        .agg({
            "ICU": "max",
            "ICU_LABEL": "max",
            "AGE_ABOVE65": "first",
            "AGE_PERCENTIL": "first"
        })
        .reset_index()
    )


# =====================================================
# VISUALIZATIONS
# =====================================================
def plot_icu_by_age_group_graph(patient_df: pd.DataFrame):
    # ---------------------------------------------
    # ICU by Age Group
    # ---------------------------------------------
    st.write("### ICU by Age Group")
    with st.expander("show ICU by Age Group Graph"):

        source = (
            patient_df.groupby(["AGE_ABOVE65", "ICU_LABEL"])
            .size()
            .reset_index(name="count")
        )

        fig = px.bar(
            source,
            x="AGE_ABOVE65",
            y="count",
            color="ICU_LABEL",
            barmode="group",
            labels={
                "AGE_ABOVE65": "Age Group",
                "count": "Number of Patients"
            },
            title="ICU by Age Group",
            color_discrete_map={
                "NO": "#16D636", 
                "YES": "#E74C3C"
            }
        )

        fig.update_layout(
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)
        st.write(source)

def plot_icu_by_age_graph(patient_df: pd.DataFrame):
    st.write("### ICU by Age")
    with st.expander("show ICU by Age Graph"):
        source = (
            patient_df.groupby(["AGE_PERCENTIL", "ICU_LABEL"])
            .size()
            .reset_index(name="count")
        )

        fig = px.bar(
            source,
            x="AGE_PERCENTIL",
            y="count",
            color="ICU_LABEL",
            labels={
                "AGE_PERCENTIL": "Age",
                "count": "Number of Patients"
            },
            title="ICU by Age",
            color_discrete_map={
                "NO": "#16D636", 
                "YES": "#E74C3C"
            }
        )

        fig.update_layout(
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)
        st.write(source)

def plot_icu_by_window_graph(df: pd.DataFrame):
    # # ---------------------------------------------
    # # ICU Rate by Window
    # # ---------------------------------------------    
    st.write("### ICU Rate by Time Window")
    with st.expander("ICU Rate by Time Window"):
        source = (
            df.groupby("WINDOW")["ICU"]
            .mean()
            .reset_index()
        )

        fig = px.scatter(
            source,
            x="WINDOW",
            y="ICU",
            labels={
                "WINDOW": "Time Window",
                "ICU": "ICU Rate"
            },
            title="ICU by Time Window",
            color_discrete_map={
                "NO": "#16D636",
                "YES": "#E74C3C"
            }
        )

        fig.update_layout(
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)
        st.write(source)


def plot_icu_frequency_by_window_graph(df: pd.DataFrame):
    # ---------------------------------------------
    # ICU Frequency by Window
    # ---------------------------------------------  
    st.write("### ICU Frequency by Time Window")
    with st.expander("ICU Frequency by Time Window"):
        source = (
        #     df.groupby("WINDOW")["ICU_LABEL"]
        #     .count()
        #     .reset_index(name="ICU_LABEL_COUNT")
             df.groupby(["WINDOW", "ICU_LABEL"])
            .size()
            .reset_index(name="ICU_LABEL_COUNT")
        )

        fig = px.bar(
            source,
            x="WINDOW",
            y="ICU_LABEL_COUNT",
            color="ICU_LABEL",
            labels={
                "WINDOW": "Time Window",
                "ICU_LABEL_COUNT": "ICU Rate"
            },
            title="ICU by Time Window",
            color_discrete_map={
                "NO": "#16D636",
                "YES": "#E74C3C"
            }
        )

        fig.update_layout(
            height=500
        )

        st.plotly_chart(fig, use_container_width=True)
        st.write(source)

def plot_dashboard(df: pd.DataFrame):
    """
    Creates ICU analysis dashboard with multiple subplots.
    """

    patient_df = aggregate_patient_level(df)

    plot_icu_by_age_group_graph(patient_df)
    plot_icu_by_age_graph(patient_df)
    plot_icu_by_window_graph(df)
    plot_icu_frequency_by_window_graph(df)



# =====================================================
# MAIN EXECUTION
# =====================================================
def main():
    st.set_page_config(layout="wide")
    st.header("COVID-19 ICU Analysis Dashboard")
    if "df" not in st.session_state:
        st.warning("No data loaded. Please go back to the home page.")
    else:
        plot_dashboard(st.session_state["df"])


if __name__ == "__main__":
    main()