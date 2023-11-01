import numpy as np
import pandas as pd
import plotly.express as px
from shapely.geometry import Polygon
import h3
from geojson import Feature, Point, FeatureCollection
import os

def open_file(file_name):
  script_dir = os.path.dirname(os.path.abspath(__file__))
  file_path = os.path.join(script_dir, file_name)
  with open(file_path, 'r', encoding="utf8") as file:
    content = file.read()
  return (file_path, content)

def load_data():
  df = pd.DataFrame({})
  for year in range(2000, 2024, 2):
    df_year = pd.read_csv(f'../../data/birds/{year}-{year+1}.csv')
    df = pd.concat([df, df_year])
  return df

def plot_observation_count(data: pd.DataFrame, category: str = 'all'):
  if category != 'all':
    data = data[data['ScientificName'] == category]

  month_count = data['Date'].apply(lambda row: row[:7] if isinstance(row, str) else None).value_counts().sort_index()
  fig = px.line(x=month_count.index, y=month_count.values)
  fig.update_layout(title=f'Observations count for {category}',
                    xaxis_title='Month',
                    yaxis_title='Observations')
  return fig

def plot_observation_municipality(data: pd.DataFrame, category: str = 'all'):
  if category != 'all':
    data = data[data['ScientificName'] == category]

  mun_count = data['Municipality'].value_counts().head(10)
  fig = px.bar(x=mun_count.index, y=mun_count.values)
  fig.update_layout(title=f'Top 10 municipality for {category}',
                    xaxis_title='Municipality',
                    yaxis_title='Observations')
  return fig

def add_geometry(row):
  points = h3.h3_to_geo_boundary(row['h3_cell'], True)
  return Polygon(points)

def hex_to_geojson(df_hex, hex_id_field, geometry_field, value_field):
  list_features = []
  for i, row in df_hex.iterrows():
    feature = Feature(geometry=row[geometry_field],
                      id=row[hex_id_field],
                      properties={'value': row[value_field]})
    list_features.append(feature)
    feat_collection = FeatureCollection(list_features)
  return feat_collection

def load_geojson(df_h3):
  df_h3['geometry'] = df_h3.apply(add_geometry, axis=1)
  geojson_object = hex_to_geojson(df_h3, hex_id_field='h3_cell', value_field='count', geometry_field='geometry')
  return geojson_object

def plot_grid_map(data, geojson):
  fig = px.choropleth_mapbox(
      data,
      geojson=geojson,
      locations='h3_cell',
      color=pd.cut(data['count'], bins=[0, 1000, 5000, 10000, np.inf]).astype(str),
      color_discrete_map={"(0.0, 1000.0]": '#1a02b8', 
                          "(1000.0, 5000.0]": '#ae22b3', 
                          "(5000.0, 10000.0]": 'red', 
                          "(10000.0, inf)": 'yellow'},
      hover_data=["count"],
      center=dict(lat=65, lon=24),
      zoom=4,
      width=600,
      height=650,
      opacity=0.35, 
      labels={'color': 'Observations', 'count': 'Observations'},
      mapbox_style="open-street-map")

  fig.update_geos(projection_type='foucaut')

  fig.update_layout(
        autosize=False,
        margin = dict(l=0, r=0, b=0, t=0, pad=4, autoexpand=True))
  return fig