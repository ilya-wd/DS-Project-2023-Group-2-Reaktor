import streamlit as st
import streamlit.components.v1 as components

import sys
import os

sys.dont_write_bytecode = True
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from func_import import open_file


def render():
    st.markdown(
        """
        <style>
        a {
            text-decoration: none;
        }
        </style>
        """,
        unsafe_allow_html=True,
    )

    st.header("Relationships")
    filler_col1, fillercol2 = st.columns([0.55, 0.45], gap="medium")
    relationship = "symbiotic"
    with filler_col1:
        relationship = st.selectbox(
            "Relationship type", ["Mutualistic", "Predatory", "Parasitic"]
        )
    col1, col2 = st.columns([0.55, 0.45], gap="medium")
    with col1:
        relationship = (
            "symbiotic" if relationship == "Mutualistic" else relationship.lower()
        )
        if relationship == "symbiotic":
            st.markdown(
                """
                #### Mutualistic

                A [mutualistic relationship](https://www.britannica.com/science/mutualism-biology) between organisms of two different species benefits both species.

                The map on the right showcases the habitats of the fly agaric mushroom (_Amanita muscaria_) and the baltic pine tree (_Pinus sylvestris_). Their mutualistic relationship can be observed from the map: the fly agaric essentially only exists in areas in which the baltic pine does as well. In this case, the pine can be observed in many areas by itself, since it has mutualistic relationships with other mushrooms in addition to the fly agaric.

                The bar graph below hihglights the average number of both species in their habitats overall, and in areas where they coexist. For the fly agaric, the averages are the same (since its habitat is dependent on the baltic pine), but the pine's occurences are higher in areas where the fly agaric coexists with it, since it benefits from the fly agaric's presence.
                """
            )

        elif relationship == "predatory":
            st.markdown(
                """
                #### Predatory

                A [predatory relationship](https://www.britannica.com/science/predation) between two animal species places the predator to hunt the pray for food. 

                The map on the right showcases the habitats of the boreal owl (_Aegolius funereus_), and two rodents it hunts: the bank vole (_Clethrionomys glareolus_) and the field vole (_Microtus agrestis_). The voles' habitats are combined in the map. Their predatory relationship can be observed from the map: the boreal owl can be observed essentially everywhere the voles do as well. In this case, the owl can be observed in many areas by itself, since it has predatory relationships with other species in addition to the voles.
                
                The bar graph below highlights the average number of both the owl and the voles in their habitats overall, and in areas where they coexist. The voles' average is the same in both cases, since the owl shares their habitat, but the owl's occurences are higher in areas in which the voles coexist.
                """
            )

        else:
            st.markdown(
                """
                #### Parasitic

                A [parasitic relationship](https://www.britannica.com/science/parasitism) between organisms of two different species benefits one species on the expense of the other, though sometimes without killing the host organism. 

                The map on the right showcases the habitats of the downy birch (_Betula pubescens_) and the witches broom fungus (_Taphrina betulina_). Their parasitic relationship can be observed from the map: the fungus essentially only exists in areas in which the birch does as well, as it is dependent on the birch to live. Since the birch is not dependent on the fungus, it can also be observed in other areas by itself.
                
                The bar graph below highlights the average number of both the birch and the fungus in their habitats overall, and in areas where they coexist. The fungus' average is the same in both cases, since it's dependent on the birch. The birch's average is somewhat counterintuitively higher in areas where the parasite fungus exists as well: this is a sign that the fungus, though a parasite of the birch, does not kill its host tree, but is rather able to spread easily in areas with a high density of host candidates.
                """
            )

        components.html(
            open_file(f"./precomp_data/correlation/{relationship}_bar.html")[1],
            height=400,
        )
    with col2:
        if relationship == "symbiotic":
            components.html(
                open_file(f"./precomp_data/correlation/{relationship}_map.html")[1],
                height=750,
            )

        elif relationship == "predatory":
            components.html(
                open_file(f"./precomp_data/correlation/{relationship}_map.html")[1],
                height=750,
            )

        else:
            components.html(
                open_file(f"./precomp_data/correlation/{relationship}_map.html")[1],
                height=750,
            )


if __name__ == "__main__":
    render()
