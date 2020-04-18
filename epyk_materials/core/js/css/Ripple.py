

class LineRipple(object):

  varName = 'lineRipple'
  expr = "new mdc.textField.MDCTextField(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = self.expr % varName

  def test(self):
    return 'alert("%s")' % self._selector
