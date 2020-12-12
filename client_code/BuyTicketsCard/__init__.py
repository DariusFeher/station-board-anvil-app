from ._anvil_designer import BuyTicketsCardTemplate
from anvil import *
import anvil.server
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables

class BuyTicketsCard(BuyTicketsCardTemplate):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.
   

  def transfer_arrows_mouse_down(self, x, y, button, **event_args):
    """This method is called when a mouse button is pressed on this component"""
    # stores the initial value of the departing station
    aux = self.departing_station_drop_down.selected_value

    # sets the departing station's value to arrival station's value
    self.departing_station_drop_down.selected_value = self.arrival_station_drop_down.selected_value

    # sets the arrival station's value to the initial value of the departing station
    self.arrival_station_drop_down.selected_value = aux

  def update_stations(self, stations_list):
    self.departing_station_drop_down.items = stations_list
    self.arrival_station_drop_down.items = stations_list

  def buy_tickets_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    if(self.arrival_station_drop_down.selected_value is None and self.departing_station_drop_down.selected_value is None):
      alert("Please select a departing and an arrival station!")
    elif(self.departing_station_drop_down.selected_value is None):
      alert("Please select a departing station!")
    elif(self.arrival_station_drop_down.selected_value is None):
      alert("Please select an arrival station!")
    elif(self.departing_station_drop_down.selected_value == self.arrival_station_drop_down.selected_value):
      alert("The stations should differ!")




