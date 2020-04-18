

class Buttons(object):

  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def button(self, text=None, icon=None, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip=None,
             profile=None, options=None):
    html_button = self.context.rptObj.ui.button(text, icon, width, height, htmlCode=htmlCode,
                                         tooltip=tooltip, profile=profile, options=options)
    html_button.style.clear_all()
    html_button.attr['class'].add('mdc-fab')
    return html_button

  def icon(self, icon, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip=None,
             profile=None, options=None):
    html_button = self.button(None, None, width, height, htmlCode=htmlCode, tooltip=tooltip, profile=profile, options=options)
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
    The icon button can be used to toggle between an on and off icon.
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
    self.context.add_cls(html_button)
    html_button.style.mdc.button_icon_toggle()
    return html_button

  def toggle(self, flag, label=None, color=None, width=(150, '%'), height=(20, 'px'), htmlCode=None, profile=None):
    """


    https://material-components.github.io/material-components-web-catalog/#/component/switch

    switchControl = new mdc.switchControl.MDCSwitch(document.querySelector('.mdc-switch'));

    :param flag:
    :param label:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    schema = {"type": 'div',
              'children': [
                  {"type": 'div', "class": "mdc-switch__track", 'css': False},
                  {"type": 'div', "class": "mdc-switch__thumb-underlay", 'css': False, 'children': [
                    {"type": 'div', "class": "mdc-switch__thumb", 'css': False},
                    {"type": 'checkbox', "class": "mdc-switch__native-control", 'args': {'flag': flag}, 'aria': {'role': 'switch', 'checked': flag}}
                  ]},

      ]
    }
    html_b = self.context.rptObj.materials.composite(schema)
    self.context.add_cls(html_b)
    html_b.style.mdc.switch()
    return html_b
