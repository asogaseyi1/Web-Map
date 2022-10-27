import folium


# Create map
map = folium.Map(location=[49.8073,-97.13489], zoom_start=6, tiles="Stamen Terrain")

#Create markers for our map
new_fg = folium.FeatureGroup("My map")
coords_list = [[6.466720, 3.648461], [49.80743, -97.13278], [30.286189, -97.738978], [53.462382, -2.293785]]
pop_ups = ["Home", "School","Alma Mater", "Old Trafford"]
color_list = ['red','blue','green','yellow']

# Markers for home, current school, Alma Mater and Old Trafford
for coordinates,alerts,marker_color in zip(coords_list,pop_ups,color_list): 
    new_fg.add_child(folium.Marker(location=coordinates, popup=alerts, icon=folium.Icon(marker_color))) 





map.add_child(new_fg)
map.save("web-map.html")