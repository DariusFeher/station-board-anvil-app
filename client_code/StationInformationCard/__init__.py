from ._anvil_designer import StationInformationCardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class StationInformationCard(StationInformationCardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def update_station_information(self, station_name, station_address, station_coordinates):
    self.station_name_label_1.text = station_name
    self.station_name_label_2.text = station_name + " station"
    self.street_number_label.text, self.city_label.text, self.county_label.text, self.postcode_label.text = station_address.split('\\n')
    self.url = 'https://www.google.com/maps/dir/Current+Location/' + str(station_coordinates)

  def goToGoogleMaps_link_click(self, **event_args):
    """This method is called when the link is clicked"""
    self.goToGoogleMaps_link.url = self.url







