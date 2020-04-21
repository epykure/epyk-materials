
from epyk.core.js import JsUtils


class Floating(object):

  varName = 'lineRipple'
  expr = "new mdc.ripple.MDCRipple(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName

  def unbounded(self, bool):
    """

    https://material.io/develop/web/components/buttons/icon-buttons/

    :param bool:
    """
    bool = JsUtils.jsConvertData(bool, None)
    return "%s.unbounded = %s" % (self._selector, bool)


class Toggle(object):

  varName = 'iconToggle'
  expr = "new mdc.iconButton.MDCIconButtonToggle(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName

  def setAttr(self):
    return "console.log(%s.foundation_)" % self._selector #.setContent('RRRRR')" % self._selector


class Switch(object):

  varName = 'switchControl'
  expr = "new mdc.switchControl.MDCSwitch(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = self.expr % varName
