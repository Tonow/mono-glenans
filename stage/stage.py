import pandas as pd
import streamlit as st


def get_df():
    # File upload widget
    uploaded_file = st.file_uploader(
        "Choisir le fichier CSV ⛵",
        type="csv",
        help="C'est le fichier qui sera utiliser pour trouver votre stage",
    )
    df = None

    # Check if a file is uploaded
    if uploaded_file is not None:
        # Read the CSV file into a Pandas DataFrame
        df = pd.read_csv(uploaded_file, sep=";", index_col=False)
    return df


def get_readme(path: str):
    # Read content from README.md
    with open(f"{path}/README.md", "r", encoding="utf-8") as readme_file:
        readme_content = readme_file.read()

    # Display the content using st.markdown()
    st.markdown(readme_content)


def set_date_columns(df: pd.DataFrame, columns_to_change: list) -> pd.DataFrame:
    date_format = "%d-%m-%Y"
    for column in columns_to_change:
        df[column] = pd.to_datetime(df[column])
        df[column] = df[column].dt.strftime(date_format)
    return df
