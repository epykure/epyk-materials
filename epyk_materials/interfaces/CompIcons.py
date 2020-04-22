from epyk_materials.core import JsMdcComponents


class Icon(object):

  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    context.rptObj.cssImport.add("material-icons")
    self.context = context

  def field(self, icon=""):
    """

    :param icon:
    """
    schema = {"type": 'span', 'class': "material-icons", 'css': None, 'attrs': {"role": 'button'}, 'args': {"text": icon}}
    span = self.context.rptObj.materials.composite(schema)
    dom_obj = JsMdcComponents.Icon(span)
    span.style.builder(span.style.varName, dom_obj.instantiate("#%s" % span.htmlId))
    # Add the specific dom features
    span.dom = dom_obj
    return span

  def icon(self, text="", in_text_field=False):
    """

    https://material.io/develop/web/components/buttons/icon-buttons/

    Attributes:
    ----------
    """
    schema = {"type": 'span', 'class': "material-icons", 'css': None, 'attrs': {"role": 'button'}, 'args': {"text": text}}
    span = self.context.rptObj.materials.composite(schema, options={"reset_class": True})
    if in_text_field:
      dom_obj = JsMdcComponents.Icon(span)
      span.style.builder(span.style.varName, dom_obj.instantiate("#%s" % span.htmlId))
      # Add the specific dom features
      span.dom = dom_obj
    return span

  def text(self, icon, value, htmlCode=None):
    """

    https://material.io/develop/web/components/input-controls/text-field/icon/

    :param icon:
    :param value:
    """
    schema = {"type": 'label', 'class': "mdc-text-field--outlined mdc-text-field--with-trailing-icon", 'css': None, 'children': [
      {"type": 'input', 'class': "mdc-text-field__input", 'css': None, 'arias': {"labelledby": htmlCode or ''}},
      {"type": 'mdc_icon', 'class-keep': True, 'class': "mdc-text-field__icon--trailing", 'css': None, 'attrs': {"role": 'button'}, 'args': {"text": icon, 'in_text_field': True}},
      {"type": 'div', 'class': "mdc-notched-outline", 'css': None, 'children': [
        {"type": 'div', 'class': "mdc-notched-outline__leading", 'css': None},
        {"type": 'div', 'class': "mdc-notched-outline__notch", 'css': None, 'children': [
          {"type": 'mdc_floating', 'class-keep': True, 'css': None, 'args': {"label": value}},
        ]},
        {"type": 'div', 'class': "mdc-notched-outline__trailing", 'css': None},
      ]},
    ]}
    span = self.context.rptObj.materials.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.TextRipple(span)
    span.style.builder(span.style.varName, dom_obj.instantiate("#%s" % span.htmlId))
    # Add the specific dom features
    span.dom = dom_obj
    return span

  def button(self, text=""):
    """
    Description:
    ------------
    The icon button will work without JavaScript, but you can enhance it to have a ripple effect by instantiating MDCRipple on the root element. See MDC Ripple for details.

    https://material.io/develop/web/components/buttons/icon-buttons/

    Attributes:
    ----------
    """
    schema = {"type": 'button', 'class': "material-icons", 'css': None}
    button = self.context.rptObj.materials.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.ButtonFloating(button)
    button.style.builder(button.style.varName, dom_obj.instantiate("#%s" % button.htmlId))
    # Add the specific dom features
    button.dom = dom_obj
    button.onReady([button.dom.unbounded(True)])
    return button

  def toggle(self, text="", label=""):
    """
    Description:
    ------------
    The icon button can be used to toggle between an on and off icon.
    To style an icon button as an icon button toggle, add both icons as child elements and place the mdc-icon-button__icon--on class on the icon that represents the on element.

    https://material.io/develop/web/components/buttons/icon-buttons/

    Attributes:
    ----------
    """
    schema = {"type": 'button', 'class': None, 'css': None, 'arias': {"pressed": False, 'label': label}, 'children': [
      {"type": 'icon', 'css': None, 'class': 'material-icons mdc-icon-button__icon mdc-icon-button__icon--on', 'args': {"text": text}},
      {"type": 'icon', 'css': None, 'class': 'material-icons mdc-icon-button__icon"', 'args': {"text": "%s_border" % text}},
    ]}
    button = self.context.rptObj.materials.composite(schema, options={"reset_class": True})
    dom_obj = JsMdcComponents.ButtonFloating(button)
    button.style.builder(button.style.varName, dom_obj.instantiate("#%s" % button.htmlId))
    # Add the specific dom features
    button.dom = dom_obj
    button.onReady([button.dom.unbounded(True)])
    return button

  def clock(self, position=None, tooltip="Last Updated Time", width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.icon('alarm', tooltip, position, width, height, htmlCode, profile)

  def refresh(self, position=None, tooltip="Last Updated Time", width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    return self.icon('refresh', tooltip, position, width, height, htmlCode, profile)
