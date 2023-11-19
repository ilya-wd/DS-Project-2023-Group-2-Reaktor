import streamlit as st
import streamlit.components.v1 as components
from PIL import Image

import sys
import os

sys.dont_write_bytecode = True
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.dirname(CURRENT_DIR) + "/../")
from func_import import open_file


def render(file_path, title, text, plot, key, file_name: str = "download.csv"):
    with st.expander(title):
        col1, col2 = st.columns([0.88, 0.12])
        col1.markdown(f"## {title}")

        with open(file_path, "r", encoding="utf-8-sig") as file:
            col2.download_button(
                label="Download data :open_file_folder:",
                data=file,
                file_name=file_name,
                key=key,
            )

        if title == "Climate change and butterflies":
            st.markdown(text)
            st.markdown("### Data exploration")
            col1, col2 = st.columns([0.85, 0.25])
            year = str(col2.slider("Year slider", 2000, 2008, 2000))
            col2.caption(f"Showing data from 2000 to {year}")
            col1._html(
                open_file(f"./precomp_data/grid_map/butterfly_{year}.html")[1],
                height=700,
            )

        elif title == "Interspecies dynamics":
            st.markdown(text)
            st.markdown("### Data exploration")
            vis_type = st.radio(
                "Visualizations", ["Map box", "Bar chart"], horizontal=True
            )
            if vis_type == "Map box":
                components.html(
                    open_file(f"./precomp_data/projects/interrelation_map.html")[1],
                    height=700,
                )
            else:
                components.html(
                    open_file(f"./precomp_data/projects/interrelation_bar.html")[1],
                    height=500,
                )

        else:
            st.markdown("""
            ### Description        
            Habitat modeling attempts to predict the distribution of a species based on environmental data. Given the environmental conditions (temperature, precipitation, elevation, etc.) at one location, the model can predict the probability that the species is present at that location, or in other words, how suitable the environmental conditions are for the existence of that species.

            We modeled the distribution of *Ranunculus glacialis* in Finland based on elevation, annual mean temperature, and annual precipitation, and obtained the following map:
            """)

            left_co, cent_co,last_co = st.columns(3)
            with cent_co:
                image = Image.open(f"{CURRENT_DIR}/../../precomp_data/species-distribution/plots/ranunculus.png")
                st.image(image)
            
            st.markdown("""
            The value in each (tiny) cell can be interpreted as the probability that the species is present in that cell.

            Below are the maps of the 3 environmental variables.
            """)
            _, left_co, mid_co, last_co, _ = st.columns([0.05, 0.3, 0.3, 0.3, 0.05])
            with left_co:
                image = Image.open(f"{CURRENT_DIR}/../../precomp_data/species-distribution/plots/elev.png")
                st.image(image)
            with mid_co:
                image = Image.open(f"{CURRENT_DIR}/../../precomp_data/species-distribution/plots/temperature.png")
                st.image(image)
            with last_co:
                image = Image.open(f"{CURRENT_DIR}/../../precomp_data/species-distribution/plots/precipitation.png")
                st.image(image)

            st.markdown("""
            ### Instructions
                        
            Observe the maps. Do you have any comments on the relationship between the distribution of *Ranunculus glacialis* and 
            the 3 environmental variables? Can you state the relative value (high/moderate/low) of each environmental 
            variable that would likely permit the existence of *Ranunculus glacialis*? Based on your observations, which 
            variable would you think best explains the distribution of *Ranunculus glacialis*?

            We can see that the distribution of *Ranunculus glacialis* has a strong positive correlation with elevation 
            (i.e., the species is more likely to be present in areas with high elevation).
            """)
            st.write("\n")


            
            
