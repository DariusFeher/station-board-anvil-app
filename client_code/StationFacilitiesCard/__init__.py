from ._anvil_designer import StationFacilitiesCardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class StationFacilitiesCard(StationFacilitiesCardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)
    
    self.facilities_dict ={
      "Ticket Office": [self.ticket_office_img, self.ticket_office_label],
      "Ticket Machine": [self.ticket_machine_img,self.ticket_machine_label],
      "Prepurchase Collection": [self.prepurchase_collection_img,self.prepurchase_collection_label],
      "Car Park": [self.car_park_img,self.car_park_label],
      "Bus Services": [self.bus_services_img,self.bus_services_label],
      "Cycle Storage": [self.cycle_storage_img,self.cycle_storage_label],
      "Step Free Access": [self.step_free_access_img, self.step_free_access_label],
      "Toilets":  [self.toilets_img,  self.toilets_label],
      "WiFi": [self.wifi_img, self.wifi_label]
    }
    # Any code you write here will run when the form opens.
  def update_station_facilities(self, station_name, facilities):
    self.card_header.text = station_name + " at a glance"
    for key in self.facilities_dict.keys():
      if(key in facilities):
		# remove capitalization of the key
        # split by ' ' and then join the words
        # using '_'

        # E.g. Ticket_office -> ticket_office
        src_name = '_'.join(key.lower().split())
        # ticket_office_black.png
        src_name += "_black.png"
				
		# source will be _/theme/ticket_office_black.png
        self.facilities_dict[key][0].source = "_/theme/" + src_name
        # set the text colour to Black
    	self.facilities_dict[key][1].foreground = "#000000"
        
      else:
        src_name = '_'.join(key.lower().split())
        src_name += "_grey.png"
    	# source will be _/theme/ticket_office_grey.png
        self.facilities_dict[key][0].source = "_/theme/" + src_name
        # set text colour to Grey
        self.facilities_dict[key][1].foreground = "#8f9f9c"
        
		