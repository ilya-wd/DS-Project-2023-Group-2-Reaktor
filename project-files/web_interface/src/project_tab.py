import streamlit as st
import sys
import os

sys.dont_write_bytecode = True
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.append(os.path.dirname(CURRENT_DIR))
sys.path.append(CURRENT_DIR + "/components/")

from func_import import open_file
import project_card


def render():
    st.header("Project tab")
    project_card.render(
        f"{CURRENT_DIR}/../../../data/butterfly/gonepteryx1.csv",
        "Climate change and butterflies",
        """
        ### Description

        In this assignment, you will explore a time series map visualization of Gonepteryx rhamni (a species 
        of butterfly) observations and their potential connection to climate change. Your task is to analyze the 
        map and draw conclusions about the changes in the location distribution over time. 

        ### Instructions

        - Spend some time exploring the map and drag the slider to see yearly changes in observations.
        - Observe changes over time: Examine the maps for different years. Note any patterns or trends you observe. 
        - Are there areas where you see changes in butterfly presence or shifts in their habitat? 
        - Consider other factors influencing the observation map. Why is the map not an accurate description of the habitats of this species? 
        - Given what you've observed and the current climate trends, try to predict how the location distribution 
        might change in the future. Do you think the northward expansion will continue? Why or why not? 
        - Why cannot Gonepteryx rhamni be found in the northernmost parts of Lapland? Consider the terrain factors.
        """,
        open_file(f"./precomp_data/correlation/parasitic_bar.html")[1],
        key=0,
    )
    project_card.render(
        f"{CURRENT_DIR}/../precomp_data/projects/interrelation_data.csv",
        "Interspecies dynamics",
        """
        ### Description

        In this assignment, you will analyze interspecies dynamics between a mushroom (Cantharellus cibarius) 
        and a tree (Pinus sylvestris). Your task is to check the graphs, maps, dataset provided, and external 
        sources to explain what the relationship between two species.

        ### Instructions

        - First, check the relationships tab to learn more about relationships and how to read the visuals.
        - Observe that in the map there is a clear dominance of some colours over others.
        - Check the bar graph if the average number depends on coexistence or not.
        - Check online to find more sources about the two species, their nutrition sources, and general behaviours to other species.
        - You can download the dataset to make experiments on it to reveal more information.
        - Form your analysis about the interspecies dynamics between the two species.
        """,
        open_file(f"./precomp_data/projects/interrelation_map.html")[1],
        key=1,
    )

    project_card.render(
        f"{CURRENT_DIR}/../../../data/butterfly/gonepteryx1.csv",
        "Birds and insects",
        "Above lush meadows and vibrant flower fields, an enchanting aerial ballet unfolds as birds and insects \
        engage in a delicate choreography. Swirling flocks of birds gracefully navigate the open skies, while a \
        myriad of colorful insects flit and flutter amongst blooming blossoms. This symbiotic relationship between \
        birds and insects is a testament to the intricate balance of nature, with birds benefiting from the insect \
        buffet and insects finding safety in the company of their avian allies. The vibrant tapestry of airborne life \
        highlights the essential role these creatures play in maintaining the health and biodiversity of our ecosystems.",
        open_file(f"./precomp_data/correlation/predatory_bar.html")[1],
        key=2,
    )


if __name__ == "__main__":
    render()
