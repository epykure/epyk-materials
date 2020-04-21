

from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects


class Line(object):

  varName = 'lineRipple'
  expr = "new mdc.lineRipple.MDCLineRipple(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName


class Chip(object):

  varName = 'chipSet'
  expr = "new mdc.chips.MDCChipSet(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName


class Icon(object):

  varName = 'icon'
  expr = "new mdc.textField.MDCTextFieldIcon(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName

  def setDisabled(self, bool):
    """
    Description:
    ------------
    Updates the icon’s disabled state.

    Related Pages:

			https://material.io/develop/web/components/input-controls/text-field/icon/

    Attributes:
    ----------
    :param label: String.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.foundation.setDisabled(%s)" % (self._selector, bool)

  def setAriaLabel(self, label):
    """
    Description:
    ------------
    Updates the icon’s aria-label.

    Related Pages:

			https://material.io/develop/web/components/input-controls/text-field/icon/

    Attributes:
    ----------
    :param label: String.
    """
    label = JsUtils.jsConvertData(label, None)
    return "%s.foundation.setAriaLabel(%s)" % (self._selector, label)

  def setContent(self, content):
    """
    Description:
    ------------
    Updates the icon’s text content

    Related Pages:

			https://material.io/develop/web/components/input-controls/text-field/icon/

    Attributes:
    ----------
    :param content: String.
    """
    content = JsUtils.jsConvertData(content, None)
    return "%s.foundation.setContent(%s)" % (self._selector, content)


class Floating(object):

  varName = 'floatingLabel'
  expr = "new mdc.floatingLabel.MDCFloatingLabel(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName

  def float(self, bool):
    """
    Description:
    ------------
    Floats or docks the label, depending on the value of shouldFloat.

    Related Pages:

      https://material.io/develop/web/components/input-controls/floating-label/

    Attributes:
    ----------
    :param bool: Boolean.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.foundation_.float(%s)" % (self._selector, bool)

  def shake(self, bool):
    """
    Description:
    ------------
    Shakes or stops shaking the label, depending on the value of shouldShake.

    Related Pages:

      https://material.io/develop/web/components/input-controls/floating-label/

    Attributes:
    ----------
    :param bool: Boolean.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.foundation_.shake(%s)" % (self._selector, bool)

  def getWidth(self):
    """
    Description:
    ------------
    Returns the width of the label element.

    Related Pages:

      https://material.io/develop/web/components/input-controls/floating-label/

    Attributes:
    ----------
    :param bool: Boolean.
    """
    bool = JsUtils.jsConvertData(bool, None)
    return JsObjects.JsNumber.JsNumber("%s.foundation_.getWidth()" % self._selector)


class NothedOutline(object):

  varName = 'notchedOutline'
  expr = "new mdc.notchedOutline.MDCNotchedOutline(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName
