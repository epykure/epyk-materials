

class Select(object):

  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def filled(self, placeholder=""):
    """
    The select uses an MDCMenu component instance to contain the list of options, but uses the data-value attribute instead of value to represent the options’ values.

    https://material.io/develop/web/components/input-controls/select-menus/
    """

    schema = {"type": 'div',
      'children': [
          {"type": 'div', "class": "mdc-select__anchor demo-width-class", 'css': False, 'children': [
            {"type": 'icon', "class": "mdc-select__dropdown-icon", 'css': False},
            {"type": 'div', "class": "mdc-select__selected-text", 'css': False},
            {"type": 'floating', 'css': False, 'args': {"label": placeholder}},
            {"type": 'mdc_line'}]},
          {"type": 'div', "class": "mdc-select__menu mdc-menu mdc-menu-surface demo-width-class", 'css': False, 'children': [
            {"type": 'list', "class": "mdc-list", 'css': False, 'children': [
              {"type": 'item', "class": "mdc-list-item", 'css': False, 'args': {"text": "Ok"}, 'attrs': {"data-value": "Ok"}},
              {"type": 'item', "class": "mdc-list-item", 'css': False, 'args': {"text": "Data"}, 'attrs': {"data-value": "Data"}}
            ]},
    ]}]}
    html_b = self.context.rptObj.materials.composite(schema)
    self.context.add_cls(html_b)
    html_b.style.mdc.select()
    return html_b

  def outlined(self, placeholder=""):
    """

    :return:
    """
    schema = {"type": 'div', 'class': 'mdc-select--outlined',
              'children': [
                {"type": 'div', "class": "mdc-select__anchor demo-width-class", 'css': False, 'children': [
                  {"type": 'icon', "class": "mdc-select__dropdown-icon", 'css': False},
                  {"type": 'div', "class": "mdc-select__selected-text", 'css': False},
                  {"type": 'div', "class": "mdc-notched-outline", 'css': False, 'children': [
                    {"type": 'div', "class": "mdc-notched-outline__leading", 'css': False},
                    {"type": 'div', "class": "mdc-notched-outline__notch", 'css': False, 'children': [
                      {"type": 'floating', 'args': {"label": placeholder}}
                    ]},
                    {"type": 'div', "class": "mdc-notched-outline__trailing", 'css': False},
                  ]},
                ]},

                {"type": 'div', "class": "mdc-select__menu mdc-menu mdc-menu-surface demo-width-class", 'css': False,
                 'children': [
                   {"type": 'list', "class": "mdc-list", 'css': False, 'children': [
                     {"type": 'item', "class": "mdc-list-item", 'css': False, 'args': {"text": "Ok"},
                      'attrs': {"data-value": "Ok"}},
                     {"type": 'item', "class": "mdc-list-item", 'css': False, 'args': {"text": "Data"},
                      'attrs': {"data-value": "Data"}}
                   ]},
                 ]}]}
    html_b = self.context.rptObj.materials.composite(schema)
    html_b.style.css.margin = 10
    self.context.add_cls(html_b)
    html_b.style.mdc.select()
    return html_b

  def shaped_filled(self):
    """

    :return:
    """

  def shaped_outlined(self):
    """

    :return:
    """
