import pandas as pd
import streamlit as st


def get_df(sep=";"):
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
        df = pd.read_csv(uploaded_file, sep=sep)
    return df


def get_readme(path: str, filename: str = "README.md"):
    # Read content from README.md
    with open(f"{path}/{filename}", "r", encoding="utf-8") as readme_file:
        readme_content = readme_file.read()

    # Display the content using st.markdown()
    st.markdown(readme_content)


def set_date_columns(df: pd.DataFrame, columns_to_change: list) -> pd.DataFrame:
    """Change string columns on python date.

    Args:
        df (pd.DataFrame): dataframe to format.
        columns_to_change (list): list of columns to change.

    Returns:
        pd.DataFrame: dataframe with columns changed to date.
    """
    input_date_format = "%d/%m/%y"
    output_date_format = "%Y/%m/%d"
    for column in columns_to_change:
        df[column] = pd.to_datetime(df[column], format=input_date_format)
        df[column] = df[column].dt.strftime(output_date_format)
        df[column] = pd.to_datetime(df[column]).dt.date
    return df
