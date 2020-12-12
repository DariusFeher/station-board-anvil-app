from ._anvil_designer import LandingPageTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables


class LandingPage(LandingPageTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    # Any code you write here will run when the form opens.
    self.stations_name, self.stations_addresses, self.stations_coordinates, self.stations_facilities = anvil.server.call('get_data_from_stations_table')
    
    self.buy_tickets_card_1.update_stations(self.stations_name)
    self.station_facilities_card_1.update_station_facilities(self.stations_name[0], self.stations_facilities[0])
    self.station_information_card_1.update_station_information(self.stations_name[0],
                                                             self.stations_addresses[0],
                                                             self.stations_coordinates[0]
                                                             )
  def display_location_on_map(self, coordinates):
    self.map_1.clear()
    latitude, longitude = coordinates.split(',')
    self.map_1.center = GoogleMap.LatLng(latitude, longitude)
    self.map_1.zoom = 16
    marker = GoogleMap.Marker(
              animation=GoogleMap.Animation.DROP,
              position=GoogleMap.LatLng(latitude, longitude)
            )
    self.map_1.add_component(marker)
    

  def map_1_show(self, **event_args):
    """This method is called when the GoogleMap is shown on the screen"""
    coordinates = self.stations_coordinates[0]
#     anvil.server.call('display_location_on_map', coordinates, self.map_1)
    self.display_location_on_map(coordinates)

  def drop_down_1_show(self, **event_args):
    """This method is called when the DropDown is shown on the screen"""
    self.drop_down_1.items = self.stations_name
    self.drop_down_1.selected_value = self.stations_name[0]

  def drop_down_1_change(self, **event_args):
    """This method is called when an item is selected"""
    if(self.drop_down_1.selected_value is None):
      self.drop_down_1.selected_value = self.stations_name[0]
      self.station_nr = 0
    else:
      self.station_nr = self.stations_name.index(self.drop_down_1.selected_value)
      
#     anvil.server.call('display_location_on_map', self.stations_coordinates[self.station_nr], self.map_1)
    self.display_location_on_map(self.stations_coordinates[self.station_nr])
    self.station_information_card_1.update_station_information(self.stations_name[self.station_nr],
                                                             self.stations_addresses[self.station_nr],
                                                             self.stations_coordinates[self.station_nr],
                                                             )
    self.station_facilities_card_1.update_station_facilities(self.stations_name[self.station_nr], self.stations_facilities[self.station_nr])