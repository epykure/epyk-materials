

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
    self.context.register(html_button)
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

  def toggle(self, recordSet=None, label=None, color=None, width=(150, '%'), height=(20, 'px'), htmlCode=None,
             profile=None):
    """

    https://material-components.github.io/material-components-web-catalog/#/component/switch

    switchControl = new mdc.switchControl.MDCSwitch(document.querySelector('.mdc-switch'));

    :param recordSet:
    :param label:
    :param color:
    :param width:
    :param height:
    :param htmlCode:
    :param profile:
    """
    switch = self.context.rptObj.ui.div().set_attrs({"class": "mdc-switch", 'css': None})
    switch += self.context.rptObj.ui.div().set_attrs({"class": "mdc-switch__track", 'css': None})
    underlay = self.context.rptObj.ui.div().set_attrs({"class": "mdc-switch__thumb-underlay", 'css': None})
    underlay += self.context.rptObj.ui.div().set_attrs({"class": "mdc-switch__thumb", 'css': None})
    check = self.context.rptObj.ui.inputs.checkbox(False).set_attrs({"class": "mdc-switch__native-control", 'css': None, 'role': 'switch', 'aria-checked': False})
    underlay += check
    switch += underlay
    switch += self.context.rptObj.ui.texts.label().set_attrs({"for": check.htmlId, 'css': None})
    return switch
