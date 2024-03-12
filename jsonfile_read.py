import json
import csv
import folium
map = folium.Map(location=[41.5025, -72.699997], zoom_start=4)

csv_file = open("./datas.csv", "r")

csv_reader = csv.DictReader(csv_file)
data = list(csv_reader)

for country in data:
    coords = ([country['Latitude'], country['Longitude']])
    folium.Marker(coords).add_to(map)
    # map.save("map.html")

map.save("map.html")