import streamlit as st
import streamlit.components.v1 as components

import sys
import os

sys.dont_write_bytecode = True
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from func_import import open_file
from func_import import open_file


def render():
    st.header("Relationships")
    st.subheader("Parastitic")
    components.html(
        open_file(f"./precomp_data/correlation/parasitic_bar.html")[1],
        width=1400,
        height=500,
    )
    st.write(
        "In parasitic relationships, one specie is dependent on the other one to live and by that it harms it as well. In this case, we are looking at Taphrina betulina and Betula pubescens, the first one is a fungus and the other one is a tree. From the graph, it is clear that the fungus almost exclusively lives in the locations that has the tree."
    )

    st.subheader("Predatory")
    components.html(
        open_file(f"./precomp_data/correlation/predatory_bar.html")[1],
        width=1400,
        height=500,
    )
    st.write(
        "In predatory relationships, one specie hunts and eats the other one. In this example case, we are looking to Aegolius funereus vs. Clethrionomys glareolus & Microtus agrestis, which are an owl and two moles that owl primarily hunts. It is clear from the graphs that owls appear more in the locations that has moles."
    )

    st.subheader("Symbiotic")
    components.html(
        open_file(f"./precomp_data/correlation/symbiotic_bar.html")[1],
        width=1400,
        height=500,
    )
    st.write(
        "Symbiosis is a type of relationship between two different biological species where one specie gets benefit of other one to sustain its life, however, the specie that provides the benefits doesn't get affected by that. In this case, we are looking to Amanita muscaria and Pinus sylvestris where Amantia muscaria grows more in locations that has Pinus sylvetris."
    )


if __name__ == "__main__":
    render()
