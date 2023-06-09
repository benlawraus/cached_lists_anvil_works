from anvil import *
from _anvil_designer.common_structures import attr_getter, attr_setter, ClassDict

repeating_panel_boats = dict(
    spacing_above='none',
    spacing_below='none',
    item_template='ListForm.RowTemplateBoats',
    parent=Container(),
)
data_grid_sailboats = dict(
    role=None,
    columns=[{'id': 'DKXOYJ', 'title': 'Name', 'data_key': 'name'}, {'id': 'TQVDLX', 'title': 'Length', 'data_key': 'length'}, {'id': 'FNUOCL', 'title': 'Actions', 'data_key': ''}],
    auto_header=True,
    tooltip='',
    border='',
    foreground='',
    rows_per_page=20.0,
    visible=True,
    wrap_on='never',
    show_page_controls=True,
    spacing_above='small',
    spacing_below='small',
    background='',
    parent=Container(),
)
databindings = [
]

class ListFormTemplate(ColumnPanel):
    def __init__(self, **properties):
        super(ListFormTemplate, self).__init__()
        self.repeating_panel_boats = RepeatingPanel(**repeating_panel_boats)
        self.data_grid_sailboats = DataGrid(**data_grid_sailboats)
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
        ListFormTemplate.__init__(self, **properties)
