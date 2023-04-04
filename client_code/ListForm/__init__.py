import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ._anvil_designer import ListFormTemplate


class ListForm(ListFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)

        # Any code you write here will run before the form opens.
        store = properties['store']
        boat_list = [{'boat_name': row['name'], 'boat_length': row['length']}
                     for row in store.values()]
        self.repeating_panel_boats.items = boat_list
