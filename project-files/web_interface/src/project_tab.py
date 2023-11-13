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
        "In the remote wilderness of the fictitious Silverwood Forest, a delicate balance unfolds as\
        wolves and sheep coexist in a delicate dance of survival. Recent observations suggest a surge\
        in wolf predation on the local sheep population, revealing the intricate interplay between predator \
        and prey. Researchers are intrigued by the ecological dynamics at play, as the wolves demonstrate \
        cunning strategies to secure their meals while the sheep adapt to the ever-present threat. This \
        complex interaction raises questions about the broader impact on the ecosystem and underscores the \
        perpetual struggle for survival in nature's unforgiving embrace.",
        open_file(f"./precomp_data/correlation/parasitic_bar.html")[1],
        key=0,
    )
    project_card.render(
        f"{CURRENT_DIR}/../../../data/butterfly/gonepteryx1.csv",
        "Wolf and sheeps",
        "In the remote wilderness of the fictitious Silverwood Forest, a delicate balance unfolds as\
        wolves and sheep coexist in a delicate dance of survival. Recent observations suggest a surge\
        in wolf predation on the local sheep population, revealing the intricate interplay between predator \
        and prey. Researchers are intrigued by the ecological dynamics at play, as the wolves demonstrate \
        cunning strategies to secure their meals while the sheep adapt to the ever-present threat. This \
        complex interaction raises questions about the broader impact on the ecosystem and underscores the \
        perpetual struggle for survival in nature's unforgiving embrace.",
        open_file(f"./precomp_data/correlation/parasitic_bar.html")[1],
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
