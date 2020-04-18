
from epyk.core.js import JsUtils


class LineRipple(object):

  varName = 'lineRipple'
  expr = "new mdc.textField.MDCTextField(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = self.expr % varName

  def test(self):
    return 'alert("%s")' % self._selector


class Slider(object):

  varName = 'slider'
  expr = "new mdc.slider.MDCSlider(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName

  def setValue(self, num):
    """
    Description:
    ------------
    Sets the current value of the slider

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param num: String.
    """
    num = JsUtils.jsConvertData(num, None)
    return "%s.foundation_.setValue(%s)" % (self._selector, num)


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
    #return "console.log(%s)" % self._selector
    return "%s.foundation_.progress_ = %s" % (self._selector, num)
