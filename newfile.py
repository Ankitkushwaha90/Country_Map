import csv
import json
import folium

def csv_to_json(csv_file):
    # Read CSV file and convert it to a list of dictionaries
    with open(csv_file, 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        data = list(csv_reader)

    # Print the data in JSON format
    json_data = json.dumps(data, indent=4)
    print(json_data[10])

# Replace 'input.csv' with the name of your CSV file
data = csv_to_json('datas.csv')
print("hello data 👍")



map = folium.Map(location=[26.917352525602915, 80.70342311181138], zoom_start=15)
folium.CircleMarker(location=[26.917352525602915, 80.70342311181138], radius=50, popup="anyplace").add_to(map)
folium.Marker([26.917352525602915, 80.70342311181138], popup = "unknown place").add_to(map)
folium.Marker([26.782735771895954, 79.02783602026649], popup = "place").add_to(map)
folium.PolyLine(locations=[(26.782735771895954, 79.02783602026649),[26.917352525602915, 80.70342311181138]], line_opacity = 0.6).add_to(map)

map.save("map.html")