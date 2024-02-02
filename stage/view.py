import streamlit as st
import pandas as pd
from stage.sidebar import get_filter
from stage.stage import set_date_columns


def filter_df(
    df: pd.DataFrame, columns_options: dict, start_date, end_date
) -> pd.DataFrame:
    # Initialize a boolean mask with all True values
    mask = pd.Series([True] * len(df), index=df.index)

    for column, options in columns_options.items():
        if options:
            mask &= df[column].isin(options)
        if start_date:
            df = df[(df["Début"] >= start_date)]
        if end_date:
            df = df[(df["Fin"] <= end_date)]

    # Apply the final mask to the DataFrame
    filtered_df = df[mask]
    return filtered_df


def show_df(df):
    if isinstance(df, pd.DataFrame):
        df = set_date_columns(df, ["Début", "Fin"])
        columns_options, submitted, start_date, end_date = get_filter(df)
        if submitted:
            df = filter_df(df, columns_options, start_date, end_date)
        st.dataframe(df, hide_index=True, use_container_width=True)


def get_readme(path: str):
    # Read content from README.md
    with open(f"{path}/README.md", "r", encoding="utf-8") as readme_file:
        readme_content = readme_file.read()

    # Display the content using st.markdown()
    st.markdown(readme_content)
