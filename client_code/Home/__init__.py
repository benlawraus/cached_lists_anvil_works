import anvil.users
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
from ._anvil_designer import HomeTemplate
from ..CreateForm import CreateForm
from ..ListForm import ListForm
from anvil_extras.storage import indexed_db

from ..db_actions import get_boat_records


class Home(HomeTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        # Any code you write here will run before the form opens.
        self.user = anvil.users.get_user()
        if not self.user:
            self.user = anvil.users.login_with_form()
        # set up the data of sail boats
        self.sail_boat_store = indexed_db.create_store('sail_boats')
        if len(self.sail_boat_store) > 0:
            self.sail_boat_store.clear()
        get_boat_records(self.sail_boat_store)
        self.display_list()

    def link_create_click(self, **event_args):
        self.main_column_panel.clear()
        self.main_column_panel.add_component(CreateForm(store = self.sail_boat_store, **event_args))

    def display_list(self, **properties):
        self.main_column_panel.clear()
        self.main_column_panel.add_component(ListForm(store= self.sail_boat_store, **properties))
