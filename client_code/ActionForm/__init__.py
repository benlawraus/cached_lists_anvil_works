from anvil import get_open_form
from ._anvil_designer import ActionFormTemplate
from anvil_extras.storage import indexed_db

from ..db_actions import delete_boat_record


class ActionForm(ActionFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.sail_boat_store = indexed_db.create_store('sail_boats')

        # Any code you write here will run before the form opens.

    def link_delete_click(self, **event_args):
        """This method is called when the link is clicked"""
        delete_boat_record(self.boat_name, self.sail_boat_store)
        get_open_form().display_list()


    def link_update_click(self, **event_args):
        """This method is called when the link is clicked"""
        get_open_form().link_create_click(boat_name=self.boat_name, **event_args)

