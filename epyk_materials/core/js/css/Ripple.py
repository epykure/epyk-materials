
from epyk.core.js import JsUtils


class LineRipple(object):

  varName = 'lineRipple'
  expr = "new mdc.textField.MDCTextField(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = self.expr % varName

  def test(self):
    return 'alert("%s")' % self._selector


class LinearProgress(object):
  
  varName = 'linearProgress'
  expr = "new mdc.linearProgress.MDCLinearProgress(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName

  def setProgress(self, num):
    """
    Description:
    ------------
    Updates the icon’s disabled state.

    Related Pages:

      https://material.io/develop/web/components/linear-progress/

    Attributes:
    ----------
    :param num: String.
    """
    num = JsUtils.jsConvertData(num, None)
    return "%s.foundation.setProgress(%s)" % (self._selector, num)
