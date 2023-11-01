import numpy as np
import pandas as pd

import streamlit as st
import streamlit.components.v1 as components
import os
from func_import import open_file

st.set_page_config(layout="wide")
st.title('Reaktor biological diversity sample web app')
tab1, tab2 = st.tabs(["🗃 Data", "📈 Visualization"])

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
tab2._html(open_file("./precomp_data/observation_muni.html")[1], height=500)

tab2.header("Map")
tab2._html(open_file("./precomp_data/grid_map.html")[1], height=800, width=1000)