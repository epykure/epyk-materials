
from epyk.core.js import JsUtils


class LineRipple(object):

  varName = 'lineRipple'
  expr = "new mdc.textField.MDCTextField(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName


class Radio(object):

  varName = 'radio'
  expr = "new mdc.radio.MDCRadio(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName

  def disabled(self, bool=None):
    """
    Description:
    ------------
    Setter/getter for the radio’s disabled state. Setter proxies to foundation’s setDisabled method

    Related Pages:

      https://material.io/develop/web/components/input-controls/radio-buttons/

    Attributes:
    ----------
    :param bool: Boolean.
    """
    if bool is None:
      return "%s.disabled" % self._selector

    bool = JsUtils.jsConvertData(bool, None)
    return "%s.disabled = %s" % (self._selector, bool)

  def checked(self, bool=None):
    """
    Description:
    ------------
    Setter/getter for the radio’s checked state

    Related Pages:

      https://material.io/develop/web/components/input-controls/radio-buttons/

    Attributes:
    ----------
    :param bool: Boolean.
    """
    if bool is None:
      return "%s.checked" % self._selector

    bool = JsUtils.jsConvertData(bool, None)
    return "%s.checked = %s" % (self._selector, bool)

  def value(self, val=None):
    """
    Description:
    ------------
    Setter/getter for the radio’s value

    Related Pages:

      https://material.io/develop/web/components/input-controls/radio-buttons/

    Attributes:
    ----------
    :param val: String.
    """
    if val is None:
      return "%s.value" % self._selector

    val = JsUtils.jsConvertData(val, None)
    return "%s.value = %s" % (self._selector, val)


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
    :param num: Number.
    """
    num = JsUtils.jsConvertData(num, None)
    return "%s.progress = %s" % (self._selector, num)

  def setDeterminate(self, bool):
    """
    Description:
    ------------
    Toggles the component between the determinate and indeterminate state.

    Related Pages:

      https://material.io/develop/web/components/linear-progress/

    Attributes:
    ----------
    :param bool: Boolean.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.determinate = %s" % (self._selector, bool)

  def setBuffer(self, num):
    """
    Description:
    ------------
    Sets the buffer bar to this value. Value should be between [0, 1].

    Related Pages:

      https://material.io/develop/web/components/linear-progress/

    Attributes:
    ----------
    :param num: Number.
    """
    num = JsUtils.jsConvertData(num, None)
    return "%s.buffer = %s" % (self._selector, num)

  def setReverse(self, bool):
    """
    Description:
    ------------
    Reverses the direction of the linear progress indicator.

    Related Pages:

      https://material.io/develop/web/components/linear-progress/

    Attributes:
    ----------
    :param bool: Boolean.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.reverse = %s" % (self._selector, bool)
