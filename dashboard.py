import streamlit as st
from stage.stage import get_df, get_readme
from stage.view import show_df
from config import STAGE_README_PATH

st.set_page_config(
    page_title="Mono Glenans",
    page_icon="⛵",
    layout="wide",
    menu_items={
        "Get Help": "https://gitlab.com/dashboard-streamlit/mono-glenans",
        "Report a bug": "https://gitlab.com/dashboard-streamlit/mono-glenans",
        "About": """
            Fait par [Tonow](https://gitlab.com/Tonow). Sous licence libre **GNU 3** \n
            N'hésiter pas à aider ou faire des commentaires.
        """,
    },
)

get_readme(STAGE_README_PATH)

df = get_df()

show_df(df)
