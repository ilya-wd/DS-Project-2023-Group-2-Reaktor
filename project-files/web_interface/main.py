import numpy as np
import pandas as pd

import streamlit as st
import streamlit.components.v1 as components
import os
from func_import import open_file

st.set_page_config(layout="wide")
st.title("Biology dashboard")

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

with tab_rela:
    tab_rela.header("Relationships")
    tab_rela.subheader("Parastitic")
    tab_rela._html(
        open_file(f"./precomp_data/correlation/parasitic_bar.html")[1],
        width=1400,
        height=500,
    )
    tab_rela.write(
        "In parasitic relationships, one specie is dependent on the other one to live and by that it harms it as well. In this case, we are looking at Taphrina betulina and Betula pubescens, the first one is a fungus and the other one is a tree. From the graph, it is clear that the fungus almost exclusively lives in the locations that has the tree."
    )

    tab_rela.subheader("Predatory")
    tab_rela._html(
        open_file(f"./precomp_data/correlation/predatory_bar.html")[1],
        width=1400,
        height=500,
    )
    tab_rela.write(
        "In predatory relationships, one specie hunts and eats the other one. In this example case, we are looking to Aegolius funereus vs. Clethrionomys glareolus & Microtus agrestis, which are an owl and two moles that owl primarily hunts. It is clear from the graphs that owls appear more in the locations that has moles."
    )

    tab_rela.subheader("Symbiotic")
    tab_rela._html(
        open_file(f"./precomp_data/correlation/symbiotic_bar.html")[1],
        width=1400,
        height=500,
    )
    tab_rela.write(
        "Symbiosis is a type of relationship between two different biological species where one specie gets benefit of other one to sustain its life, however, the specie that provides the benefits doesn't get affected by that. In this case, we are looking to Amanita muscaria and Pinus sylvestris where Amantia muscaria grows more in locations that has Pinus sylvetris."
    )
