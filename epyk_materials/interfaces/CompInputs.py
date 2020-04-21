

class Inputs(object):

  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def input(self, value="", label=""):
    """
    Description:
    ------------

    Related Pages:

      https://material-components.github.io/material-components-web-catalog/#/component/text-field?icons=leadingIcon&type=outlined

    :param text:
    """
    schema = {"type": 'ripple',
              'children': [
                  {"type": 'div', "class": "mdc-text-field__ripple", 'css': False},
                  {"type": 'input', "class": "mdc-text-field__input", 'css': False, 'args': {'text': value}},
                  {"type": 'div', "class": "mdc-line-ripple", 'css': False},
      ]
    }

    ripple = self.context.rptObj.ui.div().set_attrs({"class": "mdc-text-field__ripple", 'css': None})
    text = self.context.rptObj.ui.inputs.d_text(value).set_attrs({"class": "mdc-text-field__input", 'css': None, "aria-labelledby": "my-label-id"})
    val = self.context.rptObj.ui.texts.label(label).set_attrs({"class": "mdc-floating-label", 'css': None, 'for': text.htmlId})
    line = self.context.rptObj.ui.div().set_attrs({"class": "mdc-line-ripple", 'css': None})

    cont = self.context.rptObj.ui.texts.label([ripple, text, val, line]).set_attrs({"class": "mdc-text-field", 'css': None})
    return cont

  def filled(self, value="", label="", leading_icon=None, trailing_icon=None):
    """
    Description:
    ------------

    Usage::

      text_1 = rptObj.materials.inputs.filled("Test", "Title", leading_icon="favorite")
      text_2 = rptObj.materials.inputs.filled("Test", "Title", trailing_icon="visibility")

    Related Pages:

      https://material-components.github.io/material-components-web-catalog/#/component/text-field

    :param text:
    """
    schema = {"type": 'ripple', 'css': False,
              'children': [
                  {"type": 'input', "class": "mdc-text-field__input", 'css': False, 'args': {'text': value}},
                  {"type": 'div', "class": "mdc-line-ripple", 'css': False},
                  {"type": 'floating', 'css': False, 'args': {'label': label}},
      ]
    }
    if leading_icon is not None:
      schema['children'] = [{"type": 'icon', 'args': {'text': leading_icon, 'in_text_field': True}}] + schema['children']
    if trailing_icon is not None:
      schema['children'] = [{"type": 'icon', 'args': {'text': trailing_icon, 'in_text_field': True}}] + schema['children']
    html_b = self.context.rptObj.materials.composite(schema)
    self.context.add_cls(html_b)
    if leading_icon is not None:
      html_b.attr['class'].add("mdc-text-field--with-leading-icon")
    if trailing_icon is not None:
      html_b.attr['class'].add("mdc-text-field--with-trailing-icon")
    return html_b

  def outlined(self, value="", label="", leading_icon=None, trailing_icon=None):
    """
    Description:
    ------------

    Usage::

      text_1 = rptObj.materials.inputs.outlined("Test", "Title", leading_icon="favorite")
      text_2 = rptObj.materials.inputs.outlined("Test", "Title", trailing_icon="visibility")

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/

    :param text:
    """
    schema = {"type": 'div', 'css': False, 'children': [
        {"type": 'input', "class": "mdc-text-field__input", 'css': False, 'args': {'text': value}},
        {"type": 'div', "class": "mdc-notched-outline", 'css': False, 'children': [
          {"type": 'div', "class": "mdc-notched-outline__leading", 'css': False},
          {"type": 'div', "class": "mdc-notched-outline__notch", 'css': False, 'children': [
            {"type": 'floating', 'args': {'label': label}}
          ]},
          {"type": 'div', "class": "mdc-notched-outline__trailing", 'css': False},
        ]},

    ]}

    if leading_icon is not None:
      schema['children'] = [{"type": 'icon', 'args': {'text': leading_icon, 'in_text_field': True}}] + schema['children']
    if trailing_icon is not None:
      schema['children'] = [{"type": 'icon', 'args': {'text': trailing_icon, 'in_text_field': True}}] + schema['children']

    html_b = self.context.rptObj.materials.composite(schema)
    self.context.add_cls(html_b)
    html_b.style.mdc.line_ripple()
    html_b.style.mdc.text_notched_outline()
    if leading_icon is not None:
      html_b.attr['class'].add("mdc-text-field--with-leading-icon")
    if trailing_icon is not None:
      html_b.attr['class'].add("mdc-text-field--with-trailing-icon")
    html_b.css({"margin-top": '5px'})
    return html_b

  def textarea(self, value="", label="", width=(100, '%'), rows=5, placeholder=None, background_color=None, htmlCode=None,
               options=None, profile=None):
    """
    Description:
    ------------

    Usage::

      const lineRipple = new mdc.textField.MDCTextField(document.querySelector('.mdc-text-field'));

    :param text:
    :param width:
    :param rows:
    :param placeholder:
    :param background_color:
    :param htmlCode:
    :param options:
    :param profile:
    """
    text = self.context.rptObj.ui.inputs.textarea(value).set_attrs({"class": "mdc-text-field__input", 'css': None, "aria-labelledby": "my-label-id"})
    div = self.context.rptObj.ui.div().set_attrs({"class": "mdc-notched-outline", 'css': None})

    div += self.context.rptObj.ui.div().set_attrs({"class": "mdc-notched-outline__leading", 'css': None})
    notch = self.context.rptObj.ui.div().set_attrs({"class": "mdc-notched-outline__notch", 'css': None})
    notch += self.context.rptObj.ui.texts.label(label).set_attrs({"class": "mdc-floating-label", 'css': None, 'for': text.htmlId})

    div += notch
    div += self.context.rptObj.ui.div().set_attrs({"class": "mdc-notched-outline__trailing", 'css': None})

    cont = self.context.rptObj.ui.texts.label([text, div]).set_attrs({"class": "mdc-text-field mdc-text-field--outlined", 'css': None})
    return cont

  def radio(self, flag=False, group_name=None):
    """
    Description:
    ------------

    Usage::

      rptObj.materials.inputs.radio(True, group_name="group_1")
      rptObj.materials.inputs.radio(False, group_name="group_1")

    Related Pages:

      https://material.io/develop/web/components/input-controls/radio-buttons/
    """
    schema = {"type": 'div', 'css': False, 'children': [
      {"type": 'radio', "class": "mdc-radio__native-control", 'css': False, 'args': {'flag': flag, 'group_name': group_name}},
      {"type": 'div', "class": "mdc-radio__background", 'css': False, 'children': [
        {"type": 'div', "class": "mdc-radio__outer-circle", 'css': False},
        {"type": 'div', "class": "mdc-radio__inner-circle", 'css': False},
      ]},
      {"type": 'div', "class": "mdc-radio__ripple", 'css': False},
    ]}
    html_r = self.context.rptObj.materials.composite(schema)
    self.context.add_cls(html_r)
    html_r.style.mdc.radio()
    html_r.css({"margin": '5px'})
    return html_r

  def chip(self, text):
    """
    Description:
    ------------
    Chips are compact elements that allow users to enter information, select a choice, filter content, or trigger an action.

    Related Pages:

      https://material.io/develop/web/components/chips/

    :param text:
    """
    schema = {"type": 'div', 'class': 'mdc-chip-set mdc-chip-set--input', 'attrs': {'role': 'grid'}, 'children': []}
    if not isinstance(text, list):
      text = [text]

    for t in text:
      schema['children'].append({"type": 'div', "class": "mdc-chip", 'css': False, 'attrs': {'role': 'row'}, 'children': [
        {"type": 'div', "class": "mdc-chip__ripple", 'css': False},
        {"type": 'icon', "class": "material-icons mdc-chip__icon mdc-chip__icon--leading", 'css': False, 'args': {'text': 'event'}},
        {"type": 'div',  'attrs': {'role': 'gridcell'}, 'css': False, 'children': [
          {"type": 'div', "class": "mdc-chip__primary-action", 'attrs': {'role': 'button'}, 'css': False, 'children': [
            {"type": 'span', "class": "mdc-chip__text", 'css': False, 'args': {'text': t}},
          ]},
        ]},
      ]})

    html_c = self.context.rptObj.materials.composite(schema)
    self.context.add_cls(html_c)
    html_c.style.mdc.chip()
    return html_c

  def checkbox(self, text):
    """
    Checkboxes allow the user to select one or more items from a set.
    Related Pages:

        https://material.io/develop/web/components/input-controls/checkboxes/

      :param text:
    """

    schema = {"type": 'div', 'css': 'mdc-form-field', 'children': [
      {"type": 'div', "class": "mdc-checkbox", 'children': [
        {'type': 'checkbox', 'class': 'mdc-checkbox__native-control'},
        {'type': 'div', 'class': 'mdc-checkbox__background', 'children': [
          {'type': 'svg', 'class': 'mdc-checkbox__checkmark', 'attrs': {'viewBox': '0 0 24 24'}}
        ]},
      ]},
      {"type": 'div', "class": "mdc-radio__background", 'css': False, 'children': [
        {"type": 'div', "class": "mdc-radio__outer-circle", 'css': False},
        {"type": 'div', "class": "mdc-radio__inner-circle", 'css': False},
      ]},
      {"type": 'div', "class": "mdc-radio__ripple", 'css': False},
    ]}
    html_chk = self.context.rptObj.materials.composite(schema)
    self.context.add_cls(html_chk)
    html_chk.style.mdc.radio()
    html_chk.css({"margin": '5px'})
    return html_chk
