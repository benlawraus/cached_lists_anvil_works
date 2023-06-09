from anvil import *
from _anvil_designer.common_structures import attr_getter, attr_setter, ClassDict

label_title = dict(
    role='headline',
    align='left',
    tooltip='',
    border='',
    foreground='',
    visible=True,
    text='Add A Sail Boat',
    font_size=None,
    font='',
    spacing_above='small',
    icon_align='left',
    spacing_below='small',
    italic=False,
    background='',
    bold=False,
    underline=False,
    icon='',
    parent=Container(),
)
button_1 = dict(
    role='filled-button',
    align='center',
    tooltip='',
    border='',
    enabled=True,
    foreground='',
    visible=True,
    text='CANCEL',
    font_size=None,
    font='',
    spacing_above='small',
    icon_align='left',
    spacing_below='small',
    italic=False,
    background='',
    bold=False,
    underline=False,
    icon='',
    parent=Container(),
)
button_save = dict(
    role='filled-button',
    align='center',
    tooltip='',
    border='',
    enabled=True,
    foreground='',
    visible=True,
    text='SAVE',
    font_size=None,
    font='',
    spacing_above='small',
    icon_align='left',
    spacing_below='small',
    italic=False,
    background='',
    bold=False,
    underline=False,
    icon='',
    parent=Container(),
)
text_box_name = dict(
    role=None,
    align='left',
    hide_text=False,
    tooltip='',
    placeholder='Boat Name',
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
text_box_length = dict(
    role=None,
    align='left',
    hide_text=False,
    tooltip='',
    placeholder='Length',
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
repeating_panel_1 = dict(
    item_template='CreateForm.ItemTemplate1',
    parent=Container(),
)
databindings = [
]

class CreateFormTemplate(ColumnPanel):
    def __init__(self, **properties):
        super(CreateFormTemplate, self).__init__()
        self.label_title = Label(**label_title)
        self.button_1 = Button(**button_1)
        self.button_save = Button(**button_save)
        self.text_box_name = TextBox(**text_box_name)
        self.text_box_length = TextBox(**text_box_length)
        self.repeating_panel_1 = RepeatingPanel(**repeating_panel_1)
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
        CreateFormTemplate.__init__(self, **properties)
