import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px
from shapely.geometry import Polygon
import h3
from geojson import Feature, Point, FeatureCollection
from func_import import load_data, load_geojson, plot_observation_count, plot_observation_municipality, plot_grid_map

import sys
sys.path.append('./project-files/helper_functions/')
from gridding import h3_grid

if 'data_loaded' not in st.session_state:
  df = load_data()  
  df.dropna(subset=['Latitude', 'Longitude'], inplace=True)

  grid_object = h3_grid()
  grid_object.fit(df)
  df_h3 = grid_object.grid_info().sort_values('count')
  geojson_object = load_geojson(df_h3)

  st.session_state.df = load_data()
  st.session_state.df_h3 = df_h3
  st.session_state.geojson_object = geojson_object
  st.session_state.data_loaded = True


if st.session_state.data_loaded:
  df_loaded = st.session_state.df
  df_h3 = st.session_state.df_h3
  geojson_object = st.session_state.geojson_object

  st.title('Reaktor biological diversity sample web app')
  tab1, tab2 = st.tabs(["🗃 Data", "📈 Visualization"])

  tab1.header("Data set description")
  tab1.write("Data is obtained from laji.fi. It's about birds 🐦.")
  year = tab1.slider("Choose year:",
              2000, 2023, 2000, 1)
  
  df_year = df_loaded[df_loaded['Date'].str.startswith(str(year), na=False)] if year != 0 else df_loaded
  
  tab1.write(f"Total observations of year {year}: {len(df_year)} observations.")
  tab1.write(f"First 10 rows of data set.")
  tab1.write(df_year.head(10))


  tab2.header("Line graph")
  option = tab2.selectbox(
      'Species select',
      tuple(['all'] + list(set(df_loaded['ScientificName']))), 
      key=1)
  tab2.plotly_chart(plot_observation_count(df_loaded, option))

  tab2.header("Bar graph")
  option = tab2.selectbox(
      'Species select',
      tuple(['all'] + list(set(df_loaded['ScientificName']))), 
      key=2)
  tab2.plotly_chart(plot_observation_municipality(df_loaded, option))

  tab2.header("Gridded observations over Finland map")
  tab2.plotly_chart(plot_grid_map(df_h3, geojson_object))

  