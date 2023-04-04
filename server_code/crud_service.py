from typing import List

from sailboats import SailBoat

import anvil.server
import anvil.users
from anvil.tables import app_tables


@anvil.server.callable
def create_boat(sailboat: SailBoat)->bool:
    # check user is logged in
    user = anvil.users.get_user()
    if user is None:
        return False
    # check that the boat does not already exist
    boat = app_tables.sailboats.get(name=sailboat.name)
    if boat is not None:
        app_tables.sailboats.update(user_email = user['email'], **sailboat.as_db_dict())
    else:
        app_tables.sailboats.add_row(user_email = user['email'], **sailboat.as_db_dict())
    return True


@anvil.server.callable
def get_all_boats()->List[SailBoat]:
    """Get all the boats in the database and return them as a list of SailBoat objects"""
    # check user is logged in
    user = anvil.users.get_user()
    if user is None:
        return []

    return [SailBoat(**dict(row)) for row in app_tables.sailboats.search(user_email=user['email'])]


@anvil.server.callable
def delete_boat(name:str)->bool:
    # check user is logged in
    user = anvil.users.get_user()
    if user is None:
        return False
    row = app_tables.sailboats.get(name=name, user_email=user['email'])
    if row is None:
        return False
    row.delete()
    return True
