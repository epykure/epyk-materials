

from epyk.core.js import JsUtils


class Select(object):

  varName = 'select'
  expr = "new mdc.select.MDCSelect(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName


class List(object):

  varName = 'list'
  expr = "new mdc.list.MDCList(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName

  def singleSelection(self, bool):
    """

    :param bool:
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.singleSelection = %s" % (self._selector, bool)
