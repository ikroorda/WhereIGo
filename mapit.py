from pygeocoder import Geocoder
import json
import folium


##Get a list of all the locations (lat, long) and put points on osm map
def Map(locations, colors):
        colors_n = len(colors)
	center = [0,0]
	for item in locations:
		center[0] += item[0]
		center[1] += item[1]
	center[0] = center[0]/len(locations)
	center[1] = center[1]/len(locations)
	map_osm = folium.Map(location=[center[0], center[1]], tiles = 'Stamen Toner', zoom_start=12)

#To print dots with color gradient instead of lines. Very slow.
#        loc_n = len(locations)
#       mod = int(loc_n/colors_n) + 1
#	for index, item in enumerate(locations):
#		folium.CircleMarker(location=[item[0],item[1]], radius=4,  popup='', color= colors[int(index/mod)],fill_color=colors[int(index/mod)]).add_to(map_osm)

#To print a line
        folium.PolyLine(locations, color="red", weight=2.5, opacity=1).add_to(map_osm)

	map_osm.save('overall.html')

##location that OSM uses
def GetLocation(item):
	latitude = float(item["latitudeE7"])/10000000
        longitude = float (item["longitudeE7"])/10000000
        locations = [latitude, longitude]
        print locations
        return locations

def GetColors(filename):
        colors = []
        with open(filename,'r') as f:
            for line in f:
                for word in line.split():
                        colors.append(word)
        return colors

with open('berlin4.json') as data_file:    
    data = json.load(data_file)

locations = []

for item in data:
         locations.append(GetLocation(item))

colors = GetColors("colorlist.txt")

Map(locations, colors)
       
