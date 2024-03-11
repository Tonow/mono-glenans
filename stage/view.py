import streamlit as st
import pandas as pd
from stage.sidebar import get_filter
from stage.stage import set_date_columns
from datetime import date
from data.config import BASE, ICON_CONFIG
import folium

from streamlit_folium import folium_static


def filter_df(
    df: pd.DataFrame, columns_options: dict, start_date: date, end_date: date
) -> pd.DataFrame:
    """Fliter the dataframe with input parameters.

    Args:
        df (pd.DataFrame): dataframe to filter.
        columns_options (dict): multi options to filter match on columns.
        start_date (date): first date on start date columns.
        end_date (date): last date on end date columns.

    Returns:
        pd.DataFrame: filtered dataframe.
    """
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
    return df


def get_readme(path: str):
    # Read content from README.md
    with open(f"{path}/README.md", "r", encoding="utf-8") as readme_file:
        readme_content = readme_file.read()

    # Display the content using st.markdown()
    st.markdown(readme_content)


def show_map(df):
    my_map = folium.Map(location=[48.85889, 2.320041], zoom_start=3)
    marker_cluster = folium.plugins.MarkerCluster().add_to(my_map)
    if isinstance(df, pd.DataFrame):
        sum_lat = 0
        sum_lon = 0
        count = 0
        bases = []
        for _, row in df.iterrows():
            base = BASE.get(row["Base"])
            color = ICON_CONFIG["color"].get(str(row["Niveau"]))
            popup = f'{row["Filière"]}\n{row["Stage"]}\nNiv : {row["Niveau"]}'
            lat = base.get("lat")
            lon = base.get("lon")
            if base:
                folium.Marker(
                    [lat, lon],
                    popup=popup,
                    icon=folium.Icon(color=color),
                ).add_to(marker_cluster)
                if base not in bases:
                    bases.append(base)
                    sum_lat += lat
                    sum_lon += lon
                    count += 1
        center_lat = sum_lat / count
        center_lon = sum_lon / count
        my_map.location = [center_lat, center_lon]

        folium_static(my_map)
