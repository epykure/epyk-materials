

class Menu(object):

  def __init__(self, context):
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
