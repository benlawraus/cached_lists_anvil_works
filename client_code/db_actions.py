import anvil.server
from sailboats import SailBoat

if anvil.server.context.type == 'laptop':
    # allow type checking in pycharm for client code
    from anvil_extras.storage import StorageWrapper


def create_sail_boat_record(sailboat, sail_boat_store):
    # type: (SailBoat, StorageWrapper) -> bool
    sail_boat_store[sailboat.name] = sailboat.as_db_dict()
    return anvil.server.call('create_boat', sailboat)


def get_boat_records(store):
    # type: (StorageWrapper)->None
    for sailboat in anvil.server.call('get_all_boats'):
        store[sailboat.name] = sailboat.as_db_dict()
    return


def delete_boat_record(name, sail_boat_store):
    # type: (str, StorageWrapper) -> bool
    if name in sail_boat_store:
        del sail_boat_store[name]
    return anvil.server.call('delete_boat', name)
