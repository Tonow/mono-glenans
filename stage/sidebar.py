import streamlit as st
import pandas as pd


def get_filter(df: pd.DataFrame):
    columns_options = {}
    with st.form("stage_options"):
        with st.sidebar:
            for column in df.columns:
                options = st.multiselect(
                    f"Filter sur: {column}", set(df[column].values.tolist())
                )
                columns_options[column] = options
            submitted = st.form_submit_button("Valider les filtres")
    return columns_options, submitted
