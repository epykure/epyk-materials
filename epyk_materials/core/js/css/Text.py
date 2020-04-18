

class Icon(object):

  varName = 'icon'
  expr = "new mdc.textField.MDCTextFieldIcon(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = self.expr % varName


