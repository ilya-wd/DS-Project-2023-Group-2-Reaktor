import numpy as np
import pandas as pd

import streamlit as st
import streamlit.components.v1 as components
import os
from func_import import open_file

st.set_page_config(layout="wide")
st.title("Biological dashboard")

st.markdown(
    """
    <style>
    .st-bn {
        display: flex;
        justify-content: space-around;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

tab_biod, tab_rela, tab_proj, tab_ab = st.tabs(
    ["Biodiversity", "Relationships", "Project", "About"]
)

# Biodiversity tab

with tab_biod:
    tab_biod.header("Biodiversity in Finland")
    col1, col2 = st.columns([0.8, 0.2], gap="small")
    year = "2023"
    with col2:
        year = str(col2.slider("Slider", 2000, 2023, 2023))
        col2.write(f"Showing data from 2000 to {year}.")
    with col1:
        col1._html(
            open_file(f"./precomp_data/grid_map/grid_map_2000-{year}.html")[1],
            width=1200,
            height=800,
        )

        col1.title("Keystone species")


# tab2.header("Line graph")
# tab2._html(open_file("./precomp_data/observation_count.html")[1], height=500)

# tab2.header("Bar graph")
# option = tab2.selectbox(
#     "Year selection", tuple(["all"] + list(range(2000, 2024))), key=1
# )
# tab2._html(open_file(f"./precomp_data/observation_muni/{option}.html")[1], height=500)

# tab2.header("Map")
# tab2._html(open_file("./precomp_data/grid_map.html")[1], height=800, width=1000)


"""
Write something here...
"""
