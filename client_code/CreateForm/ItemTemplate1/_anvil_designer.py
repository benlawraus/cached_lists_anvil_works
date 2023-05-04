from anvil import *
from _anvil_designer.common_structures import attr_getter, attr_setter, ClassDict

text_box_sail_name = dict(
    role=None,
    align='left',
    hide_text=False,
    tooltip='',
    placeholder='Sail Name',
    border='',
    enabled=True,
    foreground='',
    visible=True,
    text='',
    font_size=None,
    font='',
    spacing_above='small',
    type='text',
    spacing_below='small',
    italic=False,
    background='',
    bold=False,
    underline=False,
    parent=Container(),
)
text_box_sail_area = dict(
    role=None,
    align='left',
    hide_text=False,
    tooltip='',
    placeholder='Sail Area',
    border='',
    enabled=True,
    foreground='',
    visible=True,
    text='',
    font_size=None,
    font='',
    spacing_above='small',
    type='text',
    spacing_below='small',
    italic=False,
    background='',
    bold=False,
    underline=False,
    parent=Container(),
)
link_add = dict(
    role='title',
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
    col_widths='',
    spacing_below='small',
    italic=False,
    background='',
    bold=False,
    underline=False,
    icon='fa:plus',
    parent=Container(),
)
column_panel_1 = dict(
    col_widths='{}',
    parent=Container(),
)
databindings = [
    dict( item='self.item["sail_name"]', element='text_box_sail_name.text', writeback=True,),
    dict( item='self.item["sail_area"]', element='text_box_sail_area.text', writeback=True,),
]

class ItemTemplate1Template(ColumnPanel):
    def __init__(self, **properties):
        super(ItemTemplate1Template, self).__init__()
        self.text_box_sail_name = TextBox(**text_box_sail_name)
        self.text_box_sail_area = TextBox(**text_box_sail_area)
        self.link_add = Link(**link_add)
        self.column_panel_1 = ColumnPanel(**column_panel_1)
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
        ItemTemplate1Template.__init__(self, **properties)
