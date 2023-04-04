from anvil import *
from ._anvil_designer import CreateFormTemplate
from ..db_actions import create_sail_boat_record, delete_boat_record
from ..sailboats import SailBoat


class CreateForm(CreateFormTemplate):
    def __init__(self, **properties):
        # Set Form properties and Data Bindings.
        self.init_components(**properties)
        self.sail_boat_store = properties['store']
        if properties.get('boat_name', None):
            # edit form
            self.sail_boat = SailBoat(**self.sail_boat_store[properties['boat_name']])
            self.text_box_name.text = self.sail_boat.name
            self.text_box_length.text = self.sail_boat.length
            self.repeating_panel_1.items = self.sail_boat.sails
        else:
            # create form
            self.repeating_panel_1.items = [{'sail_name': 'mainsail', 'sail_area': ''}]
            self.sail_boat = SailBoat(name='', length=0)

        # Any code you write here will run before the form opens.

    def store_form_data(self):
        """Store the form data in the sail_boat object and in the sail_boat_store"""
        boat_name = self.text_box_name.text
        if boat_name == '':
            alert('Please enter a name for your boat')
            return
        if self.sail_boat.name != '':
            # updated sailboat so delete old one
            delete_boat_record(self.sail_boat.name, self.sail_boat_store)
        self.sail_boat = SailBoat(name=boat_name,
                                  length=float(self.text_box_length.text),
                                  sails=self.repeating_panel_1.items[:])
        create_sail_boat_record(self.sail_boat, self.sail_boat_store)

    def button_save_click(self, **event_args):
        """This method is called when the button is clicked"""
        # return to list form
        self.store_form_data()
        get_open_form().display_list(**event_args)

    def button_cancel_click(self, **event_args):
        """This method is called when the button is clicked"""
        get_open_form().display_list(**event_args)

