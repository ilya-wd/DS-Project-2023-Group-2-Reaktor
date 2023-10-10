import pandas as pd
import folium
import webbrowser

# Assumes that there are rows "Species", "WGS84 N", "WGS84 E" in the DF

# Read the Excel file and drop rows with missing coordinates
df = pd.read_excel("new_bears.xlsx", usecols=["Species", "WGS84 N", "WGS84 E"]).dropna()
m = folium.Map(location=[65.0000, 26.0000], zoom_start=6)

for _, row in df.iterrows():
    latitude = row['WGS84 N']
    longitude = row['WGS84 E']
    popup_content = f"Species: {row['Species']}"
    folium.Marker([latitude, longitude], tooltip=popup_content).add_to(m)

m.save('finland_map.html')
webbrowser.open('finland_map.html', new=2)
