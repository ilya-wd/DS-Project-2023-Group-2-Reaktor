import h3
import pandas as pd
import numpy as np
import sys
sys.path.append('../')
from helper_functions.gridding import h3_grid
from web_interface.func_import import plot_grid_map, load_geojson

df = pd.read_excel("fucusvesiculosus.xlsx", usecols=["Species", "WGS84 N", "WGS84 E"]).dropna()
df = df.rename(columns={"WGS84 N": "Longitude", "WGS84 E": "Latitude"})
df['Latitude'], df['Longitude'] = df['Longitude'], df['Latitude'] #Swap because lat before long for our map!
print(df.head())
print(df.info())

grid_object = h3_grid()
grid_object.fit(df)
df_h3 = grid_object.grid_info()
fig = plot_grid_map(df_h3, load_geojson(df_h3))
fig.show()

#cant import form web-interface for some reason: why?
#need to discuss how to present data on website
#base logic here, now we need a general biodiversity map next to this.
#worked locally without this file hierarchy :D