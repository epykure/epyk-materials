

class Menu(object):

  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def surface(self):
    """

    Related Pages:

      https://material.io/develop/web/components/menu-surface/
    """
    menu = self.context.rptObj.ui.div()
    menu.set_attrs({"class": None, 'css': None})
    self.context.add_cls(menu)
    menu.style.mdc.surface()
    return menu

  def anchor(self, text, surface):
    """

    https://material.io/develop/web/components/menu-surface/

    :param text:
    :param surface:
    :return:
    """
    button = self.context.rptObj.ui.button(text)
    button.set_attrs({"class": "menu-surface-button", 'css': None})
    menu = self.context.rptObj.ui.div([button, surface])
    menu.set_attrs({"class": "mdc-menu-surface--anchor", 'css': None})
    self.context.add_cls(menu)
    return menu
