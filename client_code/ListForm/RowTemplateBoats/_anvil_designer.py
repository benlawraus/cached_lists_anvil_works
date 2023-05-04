from anvil import *
from _anvil_designer.common_structures import attr_getter, attr_setter, ClassDict
from ...ActionForm import ActionForm

label_name = dict(
)
label_length = dict(
)
action_form_1 = dict(
)
databindings = [
    dict( item='self.item["boat_name"]', element='label_name.text', writeback=False,),
    dict( item='self.item["boat_length"]', element='label_length.text', writeback=False,),
    dict( item='self.item["boat_name"]', element='action_form_1.boat_name', writeback=False,),
]

class RowTemplateBoatsTemplate(DataRowPanel):
    def __init__(self, **properties):
        super(RowTemplateBoatsTemplate, self).__init__()
        self.label_name = Label(**label_name)
        self.label_length = Label(**label_length)
        self.action_form_1 = ActionForm(**action_form_1)
        self._bindings = databindings
        self._item = ClassDict()

        if properties.get('item', None) is not None:
            self.item = properties['item']

    def __getattr__(self, item):
        '''It seems pycharm runs @property on initialization, so this is the alternative.
        It is for the attribute self.item.'''
        if item == 'item':
            return attr_getter(self, 'item')
        else:
            raise AttributeError(f"The attribute {item} is not defined.")

    def __setattr__(self, key, value):
        '''It seems pycharm runs @property on initialization, so this is the alternative.
        It is for the attribute self.item.'''
        if key == 'item':
            attr_setter(self, value, 'item')
        else:
            self.__dict__[key] = value

    def init_components(self, **properties):
        RowTemplateBoatsTemplate.__init__(self, **properties)
