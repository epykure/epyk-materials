

from epyk.core.js import JsUtils


class Select(object):

  varName = 'select'
  expr = "new mdc.select.MDCSelect(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName
