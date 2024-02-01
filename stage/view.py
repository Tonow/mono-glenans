import streamlit as st
import pandas as pd
from stage.sidebar import get_filter


def filter_df(df: pd.DataFrame, columns_options: dict) -> pd.DataFrame:
    # Initialize a boolean mask with all True values
    mask = pd.Series([True] * len(df), index=df.index)

    for column, options in columns_options.items():
        if options:
            mask &= df[column].isin(options)
    # Apply the final mask to the DataFrame
    filtered_df = df[mask]
    return filtered_df


def show_df(df):
    if isinstance(df, pd.DataFrame):
        columns_options, submitted = get_filter(df)
        if submitted:
            filtered_df = filter_df(df, columns_options)
            st.dataframe(filtered_df, hide_index=True, use_container_width=True)


def get_readme(path: str):
    # Read content from README.md
    with open(f"{path}/README.md", "r", encoding="utf-8") as readme_file:
        readme_content = readme_file.read()

    # Display the content using st.markdown()
    st.markdown(readme_content)
