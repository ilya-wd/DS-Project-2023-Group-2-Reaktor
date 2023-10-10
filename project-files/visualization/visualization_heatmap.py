import folium
import pandas as pd
import webbrowser
from folium.plugins import HeatMap

# Assumes that there are rows "Species", "WGS84 N", "WGS84 E" in the DF

df = pd.read_excel("new_bears.xlsx").dropna()
m = folium.Map(location=[65.0000, 26.0000], zoom_start=6)

heat_data = [[(row["WGS84 N"]), (row["WGS84 E"]), 1] for _, row in df.iterrows()]
HeatMap(heat_data).add_to(m)

m.save('finland_heatmap.html')
webbrowser.open('finland_heatmap.html', new=2)