from anvil import *
from _anvil_designer.common_structures import attr_getter, attr_setter, ClassDict

link_delete = dict(
    role=None,
    url='',
    align='center',
    tooltip='',
    border='',
    foreground='',
    visible=True,
    text='',
    font_size=None,
    wrap_on='mobile',
    font='',
    col_spacing='medium',
    spacing_above='small',
    icon_align='left',
    col_widths='{}',
    spacing_below='small',
    italic=False,
    background='orange',
    bold=False,
    underline=False,
    icon='fa:minus',
    parent=Container(),
)
link_update = dict(
    role=None,
    url='',
    align='center',
    tooltip='',
    border='',
    foreground='',
    visible=True,
    text='',
    font_size=None,
    wrap_on='mobile',
    font='',
    col_spacing='medium',
    spacing_above='small',
    icon_align='left',
    col_widths='{}',
    spacing_below='small',
    italic=False,
    background='lightblue',
    bold=False,
    underline=False,
    icon='fa:pencil',
    parent=Container(),
)
boat_name = dict(
)
databindings = [
]

class ActionFormTemplate(ColumnPanel):
    def __init__(self, **properties):
        super(ActionFormTemplate, self).__init__()
        self.link_delete = Link(**link_delete)
        self.link_update = Link(**link_update)
        self.boat_name = String(**boat_name)
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
        ActionFormTemplate.__init__(self, **properties)
