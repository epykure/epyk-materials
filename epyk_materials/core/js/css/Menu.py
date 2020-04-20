
class Surface(object):

  varName = 'menuSurface'
  expr = "new mdc.menuSurface.MDCMenuSurface(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = self.expr % varName
