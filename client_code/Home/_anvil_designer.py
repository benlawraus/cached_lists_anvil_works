from anvil import *
from _anvil_designer.common_structures import attr_getter, attr_setter, ClassDict

main_column_panel = dict(
)
content_panel = dict(
    col_widths='{}',
    parent=Container(),
)
link_create = dict(
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
    col_widths='',
    spacing_below='small',
    italic=False,
    background='lightgreen',
    bold=False,
    underline=False,
    icon='fa:plus',
    parent=Container(),
)
navbar_links = dict(
)
databindings = [
]

class HomeTemplate(HtmlTemplate):
    def __init__(self, **properties):
        super(HomeTemplate, self).__init__()
        self.main_column_panel = ColumnPanel(**main_column_panel)
        self.content_panel = ColumnPanel(**content_panel)
        self.link_create = Link(**link_create)
        self.navbar_links = FlowPanel(**navbar_links)
        self._bindings = databindings
        self._item = ClassDict()

        if properties.get('item', None) is not None:
            self._item = properties['item']

    @property
    def item(self):
        return attr_getter(self, 'item')

    @item.setter
    def item(self, some_dict):
        attr_setter(self, some_dict, 'item')
        return

    def init_components(self, **properties):
        HomeTemplate.__init__(self, **properties)
