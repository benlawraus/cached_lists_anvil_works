import random
import string
from typing import Tuple

from anvil_extras.storage import indexed_db

import anvil.users
import tests.pydal_def as mydal
from _anvil_designer.set_up_user import new_user_in_db
from anvil.tables import app_tables
from client_code.CreateForm import CreateForm
from client_code.Home import Home
from client_code.ListForm import ListForm
from client_code.ListForm.RowTemplateBoats import RowTemplateBoats


def random_number(size=3):
    return ''.join(random.choice(string.digits) for count in range(size))


def random_name(size=5, chars=string.ascii_lowercase):
    half_of = int(size / 2)
    first_part = ''.join(random.choice(chars) for count in range(half_of))
    last_part = ''.join(random.choice(chars) for count in range(half_of))
    first_name = first_part + random.choice('aeiou') + last_part
    return first_name.capitalize()


class Test_indexed_db_create:
    """The App creates reads updates and deletes boat descriptions in the client."""

    def login_user(self):
        mydal.define_tables_of_db()
        user = new_user_in_db()
        anvil.users.force_login(user)
        return user

    def test_get_user(self):
        user = self.login_user()
        assert anvil.users.get_user()
        anvil.users.logout()
        assert not anvil.users.get_user()

    def add_and_store_a_boat(self, form_create: CreateForm):
        """Add and store a boat. Requires a CreateForm object to carry over any session data.
        form_create will contain the boat name and length."""
        # we are adding here, not updating, so blank out the boat name to prevent deletion of previous saved boat
        form_create.sail_boat.name = ''
        # add boat name and length in the UI
        form_create.text_box_name.text = random_name()
        form_create.text_box_length.text = random_number(size=2)
        # save the UI data to the sail_boat object and the sail_boat_store
        form_create.store_form_data()
        return

    def test_create(self):
        """This method will test this CRUD functionality."""
        # test create begins here
        # start the database and login a user
        user = self.login_user()
        assert anvil.users.get_user()
        # open the home FORM
        form_home = Home()
        # click the button to create a new boat
        form_home.link_create_click()
        # get the create FORM in the column panel
        form_create = form_home.main_column_panel.get_components()[0]
        # add boat name and length in the UI
        form_create.text_box_name.text = random_name()
        form_create.text_box_length.text = random_number(size=2)
        # click the save button
        form_create.button_save_click()
        # test that the boat is in the database
        sail_boat_store = indexed_db.create_store('sail_boats')
        # the keys are the boat names. is the boat length saved? Let's check the browser indexed_db
        boat_name = form_create.text_box_name.text
        assert boat_name in sail_boat_store
        assert boat_name == sail_boat_store[boat_name]['name']
        assert float(form_create.text_box_length.text) == sail_boat_store[boat_name]['length']
        # is the boat in the database?
        boat_row = app_tables.sailboats.get(name=boat_name, user_email=user['email'])
        assert boat_row
        assert boat_name == boat_row.name
        assert float(form_create.text_box_length.text) == boat_row.length
        # test create ends here

    def test_update(self) -> Tuple[Home, int]:
        """Creates and stores a bunch of boats. Then updates one of them.
        :return: the home form and the number of boats created"""
        # test update begins here
        # start the database and login a user
        user = self.login_user()
        assert anvil.users.get_user()
        # open the home FORM
        form_home = Home()  # because Home() is based on HtmlTemplate, we can use get_open_form() to refer to it
        # click the button to create a new boat
        form_home.link_create_click()
        # get the create FORM in the column panel
        form_create = form_home.main_column_panel.get_components()[0]
        # create a bunch of sailboats
        NR_SAIL_BOATS = 20
        for i in range(NR_SAIL_BOATS):
            self.add_and_store_a_boat(form_create)
        # check that they are in the store
        sail_boat_store = indexed_db.create_store('sail_boats')
        assert NR_SAIL_BOATS == len(sail_boat_store)
        # let's go back and update a boat from the list. Open the FORM of the boat list
        form_list = ListForm(store=form_home.sail_boat_store)
        # get a random single row of the repeating panel
        row_template_form = RowTemplateBoats()
        row_number = random.choice(range(NR_SAIL_BOATS))
        row_template_form.item = form_list.repeating_panel_boats.items[row_number]
        # here is the target data for asserts
        old_boat_name = row_template_form.item['boat_name']
        old_boat_length = row_template_form.item['boat_length']
        # Let's click the update button
        action_form = row_template_form.action_form_1
        # clicking the update button changes the components in the Home FORM to an edit component
        action_form.link_update_click()
        # let's check it by examining the component
        edit_form = form_home.main_column_panel.get_components()[0]
        assert old_boat_name == edit_form.text_box_name.text
        assert old_boat_length == edit_form.text_box_length.text
        # ok, let's change the boat name and length
        new_boat_name = random_name()
        edit_form.text_box_name.text = new_boat_name
        edit_form.text_box_length.text = random_number(size=2)
        # click the save button
        edit_form.button_save_click()
        # test that the previous boat_name is not in the browser indexed_db
        assert old_boat_name not in sail_boat_store.keys()
        # test that the previous boat_name is not in the database
        boat_rows = app_tables.sailboats.search(name=old_boat_name, user_email=user['email'])
        assert 0 == len(boat_rows)
        # test that the new boat_name is in the browser indexed_db
        assert new_boat_name in sail_boat_store.keys()
        assert sail_boat_store[edit_form.text_box_name.text]['name'] == new_boat_name
        assert sail_boat_store[edit_form.text_box_name.text]['length'] == float(edit_form.text_box_length.text)
        # test that the new boat_name is in the database
        boat_rows = app_tables.sailboats.search(name=new_boat_name, user_email=user['email'])
        assert 1 == len(boat_rows)
        assert new_boat_name == boat_rows[0]['name']
        assert float(edit_form.text_box_length.text) == boat_rows[0]['length']
        # test update ends here
        return form_home, NR_SAIL_BOATS

    def test_delete(self):
        form_home, NR_SAIL_BOATS = self.test_update()
        # let's go back and delete a random boat from the list
        form_home.display_list()
        form_list = form_home.main_column_panel.get_components()[0]
        row_template_form = RowTemplateBoats()
        row_number = random.choice(range(NR_SAIL_BOATS))
        row_template_form.item = form_list.repeating_panel_boats.items[row_number]
        boat_name = row_template_form.item['boat_name']
        action_form = row_template_form.action_form_1
        action_form.link_delete_click()
        # test that the boat is not in the browser indexed_db
        assert boat_name not in form_home.sail_boat_store.keys()
        # test that the boat is not in the database
        assert 0 == len(app_tables.sailboats.search(name=boat_name, user_email=form_home.user['email']))
