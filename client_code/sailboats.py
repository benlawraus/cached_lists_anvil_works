import anvil.server

if anvil.server.context.type == 'laptop':
    # allow type checking in pycharm for client code
    from typing import List, Any


class Boat:
    def __init__(self, name, length):
        # type: (str, float) -> None
        self.name = name
        self.length = length


@anvil.server.portable_class
class SailBoat(Boat):
    """
    :param name: name of the boat
    :param length: length of the boat
    :param sails: list of sail names
    :param properties: any other properties that will be ignored
    """

    def __init__(self, name, length, sails=None, **properties):
        # type: (str, float, List, Any) -> None
        # pycharm can type check the client code with above line
        Boat.__init__(self, name, length)
        if sails is None:
            self.sails = []
        else:
            self.sails = sails

    def as_db_dict(self):
        return self.__dict__
