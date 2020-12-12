import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
#
# @anvil.server.callable
# def say_hello(name):
#   print("Hello, " + name + "!")
#   return 42
#

@anvil.server.callable
def get_data_from_stations_table():
      
      stations_information = app_tables.stations.search()
      
      stations_name = []
      stations_addresses = []
      stations_coordinates = []
      stations_facilities = []
      
      for row in stations_information:
        stations_name.append(row['Name'])
        stations_addresses.append(row['Address'])
        stations_coordinates.append(row['Coordinates'])
        current_station_facilities = []
        for facility in row['AvailableFacilities']:
          current_station_facilities.append(facility['Facility'])
        stations_facilities.append(current_station_facilities)    
      
      return stations_name, stations_addresses, stations_coordinates, stations_facilities
    

@anvil.server.callable
def display_location_on_map(coordinates, google_map):
    google_map.clear()
    latitude, longitude = coordinates.split(',')
    google_map.center = GoogleMap.LatLng(latitude, longitude)
    google_map.zoom = 16
    marker = GoogleMap.Marker(
              animation=GoogleMap.Animation.DROP,
              position=GoogleMap.LatLng(latitude, longitude)
            )
    google_map.add_component(marker)