from epyk_materials.core import JsMdcComponents


class Buttons(object):

  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def button(self, icon, label=""):
    """
    Description:
    ------------

    Related Pages:

      https://material.io/develop/web/components/buttons/floating-action-buttons/

    Attributes:
    ----------
    :param icon:
    :param label:
    """
    if not label:
      schema = {"type": 'button', 'class': None, 'css': None, 'arias': {"pressed": False}, 'children': [
        {"type": 'div', 'class': 'mdc-button__ripple', 'css': None},
        {"type": 'span', 'class': 'mdc-button__label', 'css': None, 'args': {"text": label}},
        {"type": 'div', 'class': 'material-icons mdc-button__icon', 'css': None, 'args': {"htmlObjs": icon}}
      ]}
    else:
      schema = {"type": 'button', 'class': None, 'css': None, 'arias': {"pressed": False}, 'children': [
        {"type": 'div', 'class': 'mdc-fab__ripple', 'css': None},
        {"type": 'span', 'class': 'mdc-fab__icon material-icons', 'css': None, 'args': {"text": icon}}
      ]}
    button = self.context.rptObj.materials.composite(schema)

    #
    dom_obj = JsMdcComponents.Button(button)
    button.style.builder(button.style.varName, dom_obj.instantiate("#%s" % button.htmlId))
    # Add the specific dom features
    button.dom = dom_obj
    return button

  def icon(self, icon, label=""):
    html_button = self.button(icon, label)
    self.context.rptObj.cssImport.add("material-icons")
    ripple = self.context.rptObj.ui.div()
    ripple.style.clear_all()
    ripple.attr["class"].add("mdc-fab__ripple")
    ripple += self.context.rptObj.materials.icons.icon(icon)
    html_button += ripple
    return html_button

  def toggle_icon(self, icon, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip=None,
                  profile=None, options=None):
    """
    Description:
    ------------
    The icon button can be used to toggle between an on and off icon.

    Attributes:
    ----------
    :param icon:
    :param width:
    :param height:
    :param htmlCode:
    :param tooltip:
    :param profile:
    :param options:
    """
    html_button = self.context.rptObj.ui.button(width=width, height=height, htmlCode=htmlCode, tooltip=tooltip, profile=profile, options=options)
    html_button.style.clear_all()
    i = self.context.rptObj.materials.icon(icon)
    i.attr['class'].add("mdc-icon-button__icon")
    i.attr['class'].add("mdc-icon-button__icon--on")
    html_button += i
    i_border = self.context.rptObj.materials.icon("%s_border" % icon)
    i_border.attr['class'].add('mdc-icon-button__icon')
    html_button += i_border

    dom_obj = JsMdcComponents.ButtonToggle(html_button)
    html_button.style.builder(html_button.style.varName, dom_obj.instantiate("#%s" % html_button.htmlId))
    # Add the specific dom features
    html_button.dom = dom_obj
    return html_button

  def toggle(self, flag, htmlCode=None, profile=None):
    """
    Description:
    ------------
    Switches communicate an action a user can take. They are typically placed throughout your UI, in places like dialogs, forms, cards, and toolbars.

    Related Pages:

      https://material-components.github.io/material-components-web-catalog/#/component/switch
      https://material-components.github.io/material-components-web-catalog/#/component/switch

    Attributes:
    ----------
    :param flag:
    :param htmlCode:
    :param profile:
    """
    schema = {"type": 'div', 'css': False, 'children': [
        {"type": 'div', "class": "mdc-switch__track", 'css': False},
        {"type": 'div', "class": "mdc-switch__thumb-underlay", 'css': False, 'children': [
          {"type": 'div', "class": "mdc-switch__thumb", 'css': False},
          {"type": 'checkbox', "class": "mdc-switch__native-control", 'args': {'flag': flag}, 'aria': {'role': 'switch', 'checked': flag}}
    ]}]}

    html_b = self.context.rptObj.materials.composite(schema)
    dom_obj = JsMdcComponents.Icon(html_b)
    html_b.style.builder(html_b.style.varName, dom_obj.instantiate("#%s" % html_b.htmlId))
    # Add the specific dom features
    html_b.dom = dom_obj
    return html_b


class FloatingButton(object):

  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def button(self, icon, mini=False):
    """

    :param icon:
    """
    schema = {"type": 'button', 'class': None, 'css': None, 'arias': {"pressed": False}, 'children': [
      {"type": 'div', 'class': 'mdc-fab__ripple', 'css': None},
      {"type": 'mdc_icon', 'class-keep': True, 'class': 'mdc-fab__icon', 'css': None, 'args': {"text": icon}},
    ]}

    if mini:
      schema['class'] = "mdc-fab--mini"

    button = self.context.rptObj.materials.composite(schema, options={"reset_class": True})

    #
    dom_obj = JsMdcComponents.FAB(button)
    button.style.builder(button.style.varName, dom_obj.instantiate("#%s" % button.htmlId))
    # Add the specific dom features
    button.dom = dom_obj
    return button

  def extended(self, label, icon=None, mini=False):
    """

    NOTE: The extended FAB must contain label where as the icon is optional.
    The icon and label may be specified in whichever order is appropriate based on context.

    :param icon:
    """
    schema = {"type": 'button', 'class': "mdc-fab--extended", 'css': None, 'children': [
      {"type": 'div', 'class': 'mdc-fab__ripple', 'css': None},
      {"type": 'span', 'class': 'mdc-fab__label', 'css': None, 'args': {"text": label}},
    ]}
    if mini:
      schema['class'] += " mdc-fab--mini"
    if icon is not None:
      schema['children'].insert(1, {"type": 'mdc_icon', 'class-keep': True, 'class': 'mdc-fab__icon', 'css': None, 'args': {"text": icon}})

    button = self.context.rptObj.materials.composite(schema, options={"reset_class": True})

    #
    dom_obj = JsMdcComponents.FAB(button)
    button.style.builder(button.style.varName, dom_obj.instantiate("#%s" % button.htmlId))
    # Add the specific dom features
    button.dom = dom_obj
    return button
