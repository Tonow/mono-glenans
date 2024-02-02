import streamlit as st
import pandas as pd
from datetime import datetime, date


def get_filter(df: pd.DataFrame):
    columns_options = {}
    with st.form("stage_options"):
        with st.sidebar:
            for column in df.columns:
                if column in ["Début"]:
                    start_date, end_date = get_date_range()
                elif column == "Fin":
                    pass
                else:
                    options = st.multiselect(
                        f"{column}", set(df[column].values.tolist())
                    )
                columns_options[column] = options
            submitted = st.form_submit_button("Valider les filtres")
    return columns_options, submitted, start_date, end_date


def get_date_range():
    today = datetime.now()
    next_year = today.year + 1
    start_date, end_date = st.date_input(
        "Dates des stage",
        (today, date(next_year, 1, 1)),
        format="YYYY-MM-DD",
    )
    return start_date, end_date
