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

    @property
    def item(self):
        return attr_getter(self, 'item')

    @item.setter
    def item(self, some_dict):
        attr_setter(self, some_dict, 'item')
        return

    def init_components(self, **properties):
        RowTemplateBoatsTemplate.__init__(self, **properties)
