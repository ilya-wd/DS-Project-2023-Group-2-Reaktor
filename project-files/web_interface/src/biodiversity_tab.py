import streamlit as st
import streamlit.components.v1 as components
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
    st.subheader("Biodiversity map")
    col1, col2 = st.columns([0.75, 0.25], gap="small")
    year = "2023"
    datatype = "Observations"
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

        datatype = col2.selectbox(
            "Type of data",
            ["Observations", "Richness", "Simpson index", "Shannon entropy"],
        )

    with col1:
        if datatype == "Observations":
            col1._html(
                open_file(f"./precomp_data/grid_map/grid_map_2000-{year}.html")[1],
                height=700,
            )
        elif datatype == "Richness":
            col1._html(
                open_file(f"./precomp_data/biodiversity_metrics/actual_dist/grid_richness_{year}.html")[1],
                height=700,
            )
        elif datatype == "Simpson index":
            col1._html(
                open_file(f"./precomp_data/biodiversity_metrics/actual_dist/grid_simpson_{year}.html")[1],
                height=700,
            )
        else:
            col1._html(
                open_file(f"./precomp_data/biodiversity_metrics/actual_dist/grid_shannon_{year}.html")[1],
                height=700,
            )

    st.subheader("Keystone species")
    st.markdown(
        """
        - Keystone species play a considerable role in maintaining the balance of the ecosystem. In Finland, there are several of them,
        but we focus on the yellow-breasted buntings in this webpage since this species has gone extinct in Finland, thus the effect
        of their disappearance can be studied.
        - Yellow-breasted buntings breed in Europe and migrate to Asia during winter. There, they are illegally hunted for a special dish
        and their number has decreased dramatically since 2004. Before that, they were listed as the 'Least Concerned', but, in just 10 years,
        their status became 'Critically Endangered'. In Finland, this birds has officially gone extinct, not only due to the extensive hunting
        but also because of the climate and habitat changes. Below, we study how the biodiversity changes according to the disappearance
        of yellow-breasted bunting, therefore giving an example of how keystone species might affect the whole ecosystem.
        """
    )
    components.html(open_file(f"./precomp_data/keystone/bird_paired_bunting_effect.html")[1], height=400)
    components.html(open_file(f"./precomp_data/keystone/tree_paired_bunting_effect.html")[1], height=400)

if __name__ == "__main__":
    render()
