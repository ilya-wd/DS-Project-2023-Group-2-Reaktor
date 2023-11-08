import numpy as np
import pandas as pd

import streamlit as st
import streamlit.components.v1 as components
import os
from func_import import open_file

st.set_page_config(layout="wide")
st.title('Reaktor biological diversity sample web app')
tab1, tab2, tab4 = st.tabs(["🗃 Data", "📈 Visualization", "🛈 About"])

tab1.header("Data set description")
tab1.write("Data is obtained from laji.fi. It's about birds 🐦.")
year = tab1.slider("Choose year:", 2000, 2022, 2000, 2)

df_year = pd.read_csv(open_file(f'../../data/birds/{year}-{year+1}.csv')[0])
tab1.write(f"Total observations of year {year}: {len(df_year)} observations.")
tab1.write(f"First 10 rows of data set.")
tab1.write(df_year.head(10))


tab2.header("Line graph")
tab2._html(open_file("./precomp_data/observation_count.html")[1], height=500)

tab2.header("Bar graph")
option = tab2.selectbox(
      'Year selection',
      tuple(['all'] + list(range(2000, 2024))), 
      key=1)
tab2._html(open_file(f"./precomp_data/observation_muni/{option}.html")[1], height=500)

tab2.header("Map")
tab2._html(open_file("./precomp_data/grid_map.html")[1], height=800, width=1000)

with tab4:
      st.header("Webpage about")

      text = """This info webpage studies the biodiversity of Finland by utilizing the observations obtained from laji.fi.
      In the Biodiversity tab, we present an overview interactive map indicating the observations of species
      and the biodiversity indexes. The Correlation tab explores different relationships between species and
      presents prediction maps to inference the whole area observations from a small number of datapoints.
      We also prepare some projects based on this webpage for educational purposes, which can be found in the Projects tab."""
      st.caption(text)

exp1 = tab4.expander("Biodiversity")
exp1.markdown("""
      - We present the Finnish map made of hexagons whose area is 250 sqkm  to plot observations of different species.
      We use H3 library to achieve this type of map. The map can be zoomed in and out, and users can select a small part 
      of the map which then only shows the data for that part.
      - We calculate two indexes in this webpage: Shannon index and Simpson index. Shannon index calculates the diversity
      of species in a given community. The higher the index is, the more diverse the species are in that habitat. Simpson index
      measures the probability of two randomly chosen individuals belonging to the same species in a given habitat. This index ranges
      from 0 to 1, with 0 being infinite diversity and 1 meaning that there is only one species in that area - zero diversity.
      - We also introduce keystones species, which are the important species that play a big role in the biodiversity of 
      some habitats and their disappearance might have enormous consequences.
            """)

exp2 = tab4.expander("Correlation")
exp2.markdown("""
      - There are different types of relationships between species: parasitic, symbiosis, and predatory. Except for predatory relationship 
      which is quite hard to obtain from mere observations, parasitic and symbiosis correlations are discussed in more detail in Correlation tab.
      We estimate these relationships based on the count of species in a given area.
      - As we only have a limited number of species and observations, we also provide a prediction map (inferential map/...) to predict
      biodiversity for the whole map. We use Bayesian/MaxEnt model to perform this inferential process.
            """)

exp3 = tab4.expander("Projects")
exp3.markdown("""
            For educational purposes, we also suggest some projects which can be achieved by utilizing our webpage information.
            To see further details of available projects, please visit the Projects tab.  
            """)