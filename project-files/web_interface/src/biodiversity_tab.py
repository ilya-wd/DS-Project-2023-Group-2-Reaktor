import streamlit as st
import pandas as pd

import sys
import os

sys.dont_write_bytecode = True
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from func_import import open_file

sys.dont_write_bytecode = True


def render():
    st.header("Biodiversity in Finland")
    col1, col2 = st.columns([0.75, 0.25], gap="small")
    year = "2023"
    # name = "total"
    with col2:
        st.subheader("Map controller")
        year = str(col2.slider("Year slider", 2000, 2023, 2023))
        col2.caption(f"Showing data from **2000** to **{year}**")
        stats = pd.read_csv(CURRENT_DIR + "/../precomp_data/statistics.csv")
        observations_stats = stats[stats["Year"] == int(year)]["Observations"].iloc[0]
        species_stats = stats[stats["Year"] == int(year)]["Species"].iloc[0]

        col21, col22 = st.columns([0.5, 0.5], gap="small")
        col21.markdown(
            f"<p style='text-align: center; font-size: 16px;'> Observations so far </p>",
            unsafe_allow_html=True,
        )
        col21.markdown(
            f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> {str(observations_stats)} </p>",
            unsafe_allow_html=True,
        )
        col22.markdown(
            f"<p style='text-align: center; font-size: 16px;'> Observed species </p>",
            unsafe_allow_html=True,
        )
        col22.markdown(
            f"<p style='text-align: center; font-size: 25px; font-weight: bold;'> {str(species_stats)} </p>",
            unsafe_allow_html=True,
        )

        name = col2.selectbox(
            "Type of data",
            ["Observations", "Species richness", "Other species richness"],
        )

    with col1:
        col1._html(
            open_file(f"./precomp_data/grid_map/grid_map_2000-{year}.html")[1],
            height=700,
        )


if __name__ == "__main__":
    render()
