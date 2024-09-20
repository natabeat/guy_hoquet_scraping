import folium
from arcgis.gis import GIS
from arcgis.geocoding import geocode

def generate_map(names, addresses):
    # Créer la carte avec Folium
    customMap = folium.Map(tiles='OpenStreetMap', zoom_start=3)
    gis = GIS()

    for i in range(len(addresses)):
        # Géocoder l'adresse avec ArcGIS
        location = geocode(addresses[i])
        lat, lon = location[0]['location']['y'], location[0]['location']['x']

        # Ajouter un marqueur à la carte
        folium.Marker(
            location=[lat, lon],
            popup=f"{names[i]}\n{addresses[i]}"
        ).add_to(customMap)

    # Afficher la carte dans le navigateur
    customMap.show_in_browser()
