
from epyk.core.js import JsUtils
from epyk.core.js.html import JsHtml

from epyk.core.js.primitives import JsObjects

from epyk.core.js.objects import JsNodeDom


class JsMdcHtml(JsNodeDom.JsDoms):
  css_class = None

  def __init__(self, htmlObj, varName=None):
    self.htmlObj, self.varName = htmlObj, varName or htmlObj.style.varName # because driven from the CSS
    if self.css_class is not None:
      self.htmlObj.attr["class"].add(self.css_class)

  def instantiate(self, html_id=None):
    raise Exception("This should be defined in the sub classes")


class FAB(JsMdcHtml):
  css_class = "mdc-fab"

  def instantiate(self, html_id=None):
    return "new mdc.ripple.MDCRipple(document.querySelector('%s'))" % html_id


class ButtonFloating(JsMdcHtml):
  css_class = "mdc-icon-button"

  def instantiate(self, html_id=None):
    return "new mdc.ripple.MDCRipple(document.querySelector('%s'))" % html_id

  def unbounded(self, bool):
    """

    https://material.io/develop/web/components/buttons/icon-buttons/

    :param bool:
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.unbounded = %s" % (self.varName, bool)


class ButtonToggle(JsMdcHtml):
  css_class = "mdc-icon-button"

  def instantiate(self, html_id=None):
    return "new mdc.iconButton.MDCIconButtonToggle(document.querySelector('%s'))" % html_id

  def setAttr(self):
    return "console.log(%s.foundation_)" % self.varName #.setContent('RRRRR')" % self._selector


class ButtonSwitch(JsMdcHtml):
  css_class = "mdc-switch"

  def instantiate(self, html_id=None):
    return "new mdc.switchControl.MDCSwitch(document.querySelector('%s'))" % html_id


class MenuSurface(JsMdcHtml):
  css_class = "mdc-menu-surface"

  def instantiate(self, html_id=None):
    return "new mdc.menuSurface.MDCMenuSurface(document.querySelector('%s'))" % html_id


class TabBar(JsMdcHtml):
  css_class = "mdc-tab-bar"

  def instantiate(self, html_id=None):
    return "new mdc.tabBar.MDCTabBar(document.querySelector('%s'))" % html_id


class LinearProgress(JsMdcHtml):

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


class Select(JsMdcHtml):
  css_class = "mdc-select"

  @property
  def content(self):
    return JsHtml.ContentFormatters(self.htmlObj._report, "%s.value" % self.varName)

  def instantiate(self, html_id=None):
    return "new mdc.select.MDCSelect(document.querySelector('%s'))" % html_id

  def setDisabled(self, bool):
    """
    Updates the disabled state.

    https://material.io/develop/web/components/input-controls/select-menus/
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.disabled = %s" % (self.varName, bool)

  def setValue(self, value):
    """

    https://material.io/develop/web/components/input-controls/select-menus/

    :param value:
    """
    value = JsUtils.jsConvertData(value, None)
    return "%s.value = %s" % (self.varName, value)

  def getValue(self):
    """

    https://material.io/develop/web/components/input-controls/select-menus/
    """
    return self.content

  def getSelectedIndex(self):
    """
    Returns the index of the currently selected menu item.

    https://material.io/develop/web/components/input-controls/select-menus/
    """
    return JsObjects.JsNumber.JsNumber("%s.selectedIndex" % self.varName)


class List(JsMdcHtml):
  css_class = "mdc-list"

  def instantiate(self, html_id=None):
    return "new mdc.list.MDCList(document.querySelector('%s'))" % html_id

  def singleSelection(self, bool):
    """

    :param bool:
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.singleSelection = %s" % (self.varName, bool)


class Line(JsMdcHtml):
  css_class = "mdc-line-ripple"

  def instantiate(self, html_id=None):
    return "new mdc.lineRipple.MDCLineRipple(document.querySelector('%s'))" % html_id


class Chip(JsMdcHtml):
  css_class = "mdc-chip-set"

  def instantiate(self, html_id=None):
    return "new mdc.chips.MDCChipSet(document.querySelector('%s'))" % html_id


class Field(JsMdcHtml):
  css_class = "mdc-form-field"

  def instantiate(self, html_id=None):
    return "new mdc.formField.MDCFormField(document.querySelector('%s'))" % html_id

  def input(self, value):
    """

    :param value:
    """
    value = JsUtils.jsConvertData(value, None)
    return "%s.input = %s" % (self.varName, value)


class Icon(JsMdcHtml):
  css_class = "mdc-text-field-icon"

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


class TextNothedOutline(JsMdcHtml):
  css_class = "mdc-text-field--outlined"

  def instantiate(self, html_id=None):
    return "new mdc.notchedOutline.MDCNotchedOutline(document.querySelector('%s'))" % html_id


class TextRipple(JsMdcHtml):
  css_class = "mdc-text-field"

  def instantiate(self, html_id=None):
    return "new mdc.textField.MDCTextField(document.querySelector('%s'))" % html_id


class TextFloating(JsMdcHtml):
  css_class = "mdc-floating-label"

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


class Radio(JsMdcHtml):
  css_class = "mdc-radio"

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


class Slider(JsMdcHtml):
  css_class = "mdc-slider"

  @property
  def content(self):
    return JsHtml.ContentFormatters(self.htmlObj._report, "%s.foundation_.getValue()" % self.varName)

  def instantiate(self, html_id=None):
    return "new mdc.slider.MDCSlider(document.querySelector('%s'))" % html_id

  def getValue(self):
    """
    Returns the current value of the slider

    https://material.io/develop/web/components/input-controls/sliders/

    :return:
    """
    return self.content

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

  def getMax(self):
    """
    Description:
    ------------
    Returns the max value the slider can have

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/
    """
    return JsObjects.JsNumber.JsNumber("%s.foundation_.getMax()" % self.varName)

  def setMax(self, num):
    """
    Description:
    ------------
    Returns the max value the slider can have

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param num: String.
    """
    num = JsUtils.jsConvertData(num, None)
    return "%s.foundation_.setMax(%s)" % (self.varName, num)

  def getMin(self):
    """
    Description:
    ------------
    Returns the min value the slider can have

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/
    """
    return JsObjects.JsNumber.JsNumber("%s.foundation_.getMin()" % self.varName)

  def setMin(self, num):
    """
    Description:
    ------------
    Sets the min value the slider can have

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param num: String.
    """
    num = JsUtils.jsConvertData(num, None)
    return "%s.foundation_.setMin(%s)" % (self.varName, num)

  def getStep(self):
    """
    Description:
    ------------
    Returns the step value of the slider

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/
    """
    return JsObjects.JsNumber.JsNumber("%s.foundation_.getStep()" % self.varName)

  def setStep(self, num):
    """
    Description:
    ------------
    Sets the step value of the slider

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param num: String.
    """
    num = JsUtils.jsConvertData(num, None)
    return "%s.foundation_.setStep(%s)" % (self.varName, num)

  def isDisabled(self):
    """
    Description:
    ------------
    Returns whether or not the slider is disabled

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/
    """
    return JsObjects.JsBoolean.JsBoolean("%s.foundation_.isDisabled()" % self.varName)

  def setDisabled(self, bool):
    """
    Description:
    ------------
    Sets the step value of the slider

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    Attributes:
    ----------
    :param num: String.
    """
    bool = JsUtils.setDisabled(bool, None)
    return "%s.foundation_.setDisabled(%s)" % (self.varName, bool)

