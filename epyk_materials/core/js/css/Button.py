

class Floating(object):

  varName = 'lineRipple'
  expr = "new mdc.ripple.MDCRipple(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = self.expr % varName

  def test(self):
    return 'alert("%s")' % self._selector


class Toggle(object):

  varName = 'iconToggle'
  expr = "new mdc.iconButton.MDCIconButtonToggle(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = varName# "(function(){return new mdc.iconButton.MDCTextFieldIconFoundation(document.querySelector('%s'))})()" % varName

  def setAttr(self):
    return "console.log(%s.foundation_)" % self._selector #.setContent('RRRRR')" % self._selector


class Switch(object):

  varName = 'switchControl'
  expr = "new mdc.switchControl.MDCSwitch(document.querySelector('%s'))"

  def __init__(self, htmlObj, varName):
    self.htmlObj = htmlObj
    self._selector = self.expr % varName
