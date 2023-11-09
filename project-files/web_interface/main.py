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

with tab_ab:
    st.header("Webpage about")

    text = """This info webpage studies the biodiversity of Finland by utilizing the observations obtained from laji.fi.
      In the Biodiversity tab, we present an overview interactive map indicating the observations of species
      and the biodiversity indexes. The Correlation tab explores different relationships between species and
      presents prediction maps to inference the whole area observations from a small number of datapoints.
      We also prepare some projects based on this webpage for educational purposes, which can be found in the Projects tab."""
    st.caption(text)

    exp1 = tab_ab.expander("Biodiversity")
    exp1.markdown(
        """
      - We present the Finnish map made of hexagons whose area is 250 sqkm  to plot observations of different species.
      We use H3 library to achieve this type of map. The map can be zoomed in and out, and users can select a small part 
      of the map which then only shows the data for that part.
      - We calculate two indexes in this webpage: Shannon index and Simpson index. Shannon index calculates the diversity
      of species in a given community. The higher the index is, the more diverse the species are in that habitat. Simpson index
      measures the probability of two randomly chosen individuals belonging to the same species in a given habitat. This index ranges
      from 0 to 1, with 0 being infinite diversity and 1 meaning that there is only one species in that area - zero diversity.
      - We also introduce keystones species, which are the important species that play a big role in the biodiversity of 
      some habitats and their disappearance might have enormous consequences.
        """
    )

    exp2 = tab_ab.expander("Correlation")
    exp2.markdown(
        """
        - There are different types of relationships between species: parasitic, symbiosis, and predatory. These correlations 
        are discussed in more detail in Correlation tab. We estimate these relationships based on the count of species in a given area.
        - As we only have a limited number of species and observations, we also provide a prediction map (inferential map/...) to predict
        biodiversity for the whole map. We use Bayesian/MaxEnt model to perform this inferential process.
        """
    )

    exp3 = tab_ab.expander("Projects")
    exp3.markdown(
        """
        For educational purposes, we also suggest some projects which can be achieved by utilizing our webpage information.
        To see further details of available projects, please visit the Projects tab.  
        """
    )
