

class Text(object):
  """
  """

  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def ripple(self):
    """
    """
    label = self.context.rptObj.ui.texts.label()
    label.set_attrs({"class": None, 'css': None})
    self.context.add_cls(label)
    label.style.mdc.line_ripple()
    return label
