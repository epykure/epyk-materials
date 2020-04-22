
from epyk.core.js import JsUtils
from epyk.core.js.primitives import JsObjects

from epyk.core.js.objects import JsNodeDom


class JsMdcHtml(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-fab")

  def instantiate(self, html_id=None):
    raise Exception("")


class FAB(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-fab")

  def instantiate(self, html_id=None):
    return "new mdc.ripple.MDCRipple(document.querySelector('%s'))" % html_id


class ButtonFloating(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-icon-button")

  def instantiate(self, html_id=None):
    return "new mdc.ripple.MDCRipple(document.querySelector('%s'))" % html_id

  def unbounded(self, bool):
    """

    https://material.io/develop/web/components/buttons/icon-buttons/

    :param bool:
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.unbounded = %s" % (self.varName, bool)


class ButtonToggle(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-icon-button")

  def instantiate(self, html_id=None):
    return "new mdc.iconButton.MDCIconButtonToggle(document.querySelector('%s'))" % html_id

  def setAttr(self):
    return "console.log(%s.foundation_)" % self._selector #.setContent('RRRRR')" % self._selector


class ButtonSwitch(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-switch")

  def instantiate(self, html_id=None):
    return "new mdc.switchControl.MDCSwitch(document.querySelector('%s'))" % html_id


class MenuSurface(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-menu-surface")

  def instantiate(self, html_id=None):
    return "new mdc.menuSurface.MDCMenuSurface(document.querySelector('%s')" % html_id


class TabBar(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    htmlObj.attr['class'].add("mdc-tab-bar") # Attach the CSS class used to build this class

  def instantiate(self, html_id=None):
    return "new mdc.tabBar.MDCTabBar(document.querySelector('%s'))" % html_id


class LinearProgress(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName

  def instantiate(self, html_id=None):
    return "new mdc.linearProgress.MDCLinearProgress(document.querySelector('%s'))" % html_id

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
    return "%s.progress = %s" % (self.varName, num)

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
    return "%s.determinate = %s" % (self.varName, bool)

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
    return "%s.buffer = %s" % (self.varName, num)

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
    return "%s.reverse = %s" % (self.varName, bool)


class Select(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-select")

  def instantiate(self, html_id=None):
    return "new mdc.select.MDCSelect(document.querySelector('%s'))" % html_id


class List(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-list")

  def instantiate(self, html_id=None):
    return "new mdc.list.MDCList(document.querySelector('%s'))" % html_id

  def singleSelection(self, bool):
    """

    :param bool:
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.singleSelection = %s" % (self.varName, bool)


class Line(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-line-ripple")

  def instantiate(self, html_id=None):
    return "new mdc.lineRipple.MDCLineRipple(document.querySelector('%s'))" % html_id


class Chip(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-chip-set")

  def instantiate(self, html_id=None):
    return "new mdc.chips.MDCChipSet(document.querySelector('%s'))" % html_id


class Field(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-form-field")

  def instantiate(self, html_id=None):
    return "new mdc.formField.MDCFormField(document.querySelector('%s'))" % html_id

  def input(self, value):
    """

    :param value:
    """
    value = JsUtils.jsConvertData(value, None)
    return "%s.input = %s" % (self.varName, value)


class Icon(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-text-field-icon")

  def instantiate(self, html_id=None):
    return "new mdc.textField.MDCTextFieldIcon(document.querySelector('%s'))" % html_id

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
    return "%s.foundation.setDisabled(%s)" % (self.varName, bool)

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
    return "%s.foundation.setAriaLabel(%s)" % (self.varName, label)

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
    return "%s.foundation.setContent(%s)" % (self.varName, content)


class TextNothedOutline(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-text-field--outlined")

  def instantiate(self, html_id=None):
    return "new mdc.notchedOutline.MDCNotchedOutline(document.querySelector('%s'))" % html_id


class TextRipple(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-text-field")

  def instantiate(self, html_id=None):
    return "new mdc.textField.MDCTextField(document.querySelector('%s'))" % html_id


class TextFloating(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-floating-label")

  def instantiate(self, html_id=None):
    return "new mdc.floatingLabel.MDCFloatingLabel(document.querySelector('%s'))" % html_id

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
    return "%s.foundation_.float(%s)" % (self.varName, bool)

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
    return "%s.foundation_.shake(%s)" % (self.varName, bool)

  def getWidth(self):
    """
    Description:
    ------------
    Returns the width of the label element.

    Related Pages:

      https://material.io/develop/web/components/input-controls/floating-label/
    """
    return JsObjects.JsNumber.JsNumber("%s.foundation_.getWidth()" % self.varName)


class Radio(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-radio")

  def instantiate(self, html_id=None):
    return "new mdc.radio.MDCRadio(document.querySelector('%s'))" % html_id

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
    return "%s.disabled = %s" % (self.varName, bool)


class Slider(JsNodeDom.JsDoms):

  def __init__(self, htmlObj, varName):
    self.htmlObj, self.varName = htmlObj, varName
    self.htmlObj.attr["class"].add("mdc-slider")

  def instantiate(self, html_id=None):
    return "new mdc.slider.MDCSlider(document.querySelector('%s'))" % html_id

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
    return "%s.foundation_.setValue(%s)" % (self.varName, num)

