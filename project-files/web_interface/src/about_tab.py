import streamlit as st

import sys
import os

sys.dont_write_bytecode = True
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(CURRENT_DIR))
from func_import import open_file
from func_import import open_file


def render():
    st.header("Webpage about")

    text = """This info webpage studies the biodiversity of Finland by utilizing the observations obtained from laji.fi.
      In the Biodiversity tab, we present an overview interactive map indicating the observations of species
      and the biodiversity indexes. The Relationships tab explores different relationships between species and
      presents prediction maps to inference the whole area observations from a small number of datapoints.
      We also prepare some projects based on this webpage for educational purposes, which can be found in the Project tab."""
    st.caption(text)

    st.subheader("Biodiversity")
    st.markdown(
        """
      - We present the Finnish map made of hexagons whose area is 250 sqkm  to plot observations of different species.
      We use H3 library to achieve this type of map. The map can be zoomed in and out, and users can select a small part 
      of the map which then only shows the data for that part.
      - We calculate two indexes in this webpage: Shannon index and Simpson index. Shannon index calculates the abundance of
      different species in a given community. The higher the index is, the more diverse the species are in that habitat. Simpson index
      measures the probability of two randomly chosen individuals belonging to the same species in a given habitat. This index ranges
      from 0 to 1, with 0 being infinite diversity and 1 meaning that there is only one species in that area - zero diversity.
      - We also introduce keystones species, which are the important species that play a big role in the biodiversity of 
      some habitats and their disappearance might have enormous consequences.
        """
    )

    st.subheader("Relationships")
    st.markdown(
        """
        There are different types of relationships between species: parasitic, symbiosis, and predatory. These correlations 
        are discussed in more detail in Correlation tab. We estimate these relationships based on the count of species in a given area.
        """
    )

    st.subheader("Project")
    st.markdown(
        """
        For educational purposes, we also suggest some projects which can be achieved by utilizing our webpage information.
        To see further details of available projects, please visit the Project tab.  
        """
    )


if __name__ == "__main__":
    render()
