import streamlit as st

import sys

sys.dont_write_bytecode = True
sys.path.append("../")
from func_import import open_file


def render():
    st.header("Biodiversity in Finland")
    col1, col2 = st.columns([0.75, 0.25], gap="small")
    year = "2023"
    # name = "total"
    with col2:
        st.subheader("Map controller")
        year = str(col2.slider("Year slider", 2000, 2023, 2023))
        col2.write(f"Showing data from 2000 to {year}.")
        name = col2.selectbox(
            "Type of data",
            ["Observations", "Species richness", "Other species richness"],
        )
        species = col2.multiselect(
            "Species",
            ["Birds", "Trees", "Insects", "Keystone species"],
            ["Birds", "Trees", "Insects", "Keystone species"],
        )

    with col1:
        col1._html(
            open_file(f"./precomp_data/grid_map/grid_map_2000-{year}.html")[1],
            width=1000,
            height=800,
        )


if __name__ == "__main__":
    render()
