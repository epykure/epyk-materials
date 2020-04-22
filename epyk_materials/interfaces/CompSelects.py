from epyk_materials.core import JsMdcComponents


class Select(object):

  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def filled(self, placeholder=""):
    """
    Description:
    ------------
    The select uses an MDCMenu component instance to contain the list of options, but uses the data-value attribute instead of value to represent the options’ values.

    Related Pages:

      https://material.io/develop/web/components/input-controls/select-menus/
    """
    schema = {"type": 'div', 'css': False,
      'children': [
          {"type": 'div', "class": "mdc-select__anchor demo-width-class", 'css': False, 'children': [
            {"type": 'icon', "class": "mdc-select__dropdown-icon", 'css': False},
            {"type": 'div', "class": "mdc-select__selected-text", 'css': False},
            {"type": 'mdc_floating', 'css': False, 'args': {"label": placeholder}},
            {"type": 'mdc_line'}]},
          {"type": 'div', "class": "mdc-select__menu mdc-menu mdc-menu-surface demo-width-class", 'css': False, 'children': [
            {"type": 'list', "class": "mdc-list", 'css': False, 'children': [
              {"type": 'item', "class": "mdc-list-item", 'css': False, 'args': {"text": "Ok"}, 'attrs': {"data-value": "Ok"}},
              {"type": 'item', "class": "mdc-list-item", 'css': False, 'args': {"text": "Data"}, 'attrs': {"data-value": "Data"}}
            ]},
    ]}]}
    html_b = self.context.rptObj.materials.composite(schema)
    dom_obj = JsMdcComponents.Select(html_b, html_b.style.varName)
    html_b.style.builder(html_b.style.varName, dom_obj.instantiate("#%s" % html_b.htmlId))
    # Add the specific dom features
    html_b.dom = dom_obj
    return html_b

  def outlined(self, placeholder=""):
    """
    Description:
    ------------
    MDC Select provides Material Design single-option select menus, using the MDC menu. The Select component is fully accessible, and supports RTL rendering.

    Related Pages:

      https://material.io/develop/web/components/input-controls/select-menus/
    """
    schema = {"type": 'div', 'class': 'mdc-select--outlined', 'css': False,
              'children': [
                {"type": 'div', "class": "mdc-select__anchor demo-width-class", 'css': False, 'children': [
                  {"type": 'icon', "class": "mdc-select__dropdown-icon", 'css': False},
                  {"type": 'div', "class": "mdc-select__selected-text", 'css': False},
                  {"type": 'div', "class": "mdc-notched-outline", 'css': False, 'children': [
                    {"type": 'div', "class": "mdc-notched-outline__leading", 'css': False},
                    {"type": 'div', "class": "mdc-notched-outline__notch", 'css': False, 'children': [
                      {"type": 'mdc_floating', 'args': {"label": placeholder}}
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
    html_b.style.css.margin = 2
    dom_obj = JsMdcComponents.Select(html_b, html_b.style.varName)
    html_b.style.builder(html_b.style.varName, dom_obj.instantiate("#%s" % html_b.htmlId))
    # Add the specific dom features
    html_b.dom = dom_obj
    return html_b

