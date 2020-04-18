
from epyk_materials.core.js.css import Ripple


class Catalog(object):

  def __init__(self, report, htmlObj):
    self.__rptObj, self.htmlObj = report, htmlObj
    self.__ctx = {}

  def line_ripple(self):
    """

    :return:
    """
    cls = "mdc-text-field"
    self.htmlObj.attr['class'].add(cls)
    self.htmlObj.style.builder(Ripple.LineRipple.varName, Ripple.LineRipple.expr % ".%s" % cls)
    # attach to the object the Javascript shortcurs to be able to use the API
    self.htmlObj.js.line_ripple = Ripple.LineRipple(self.htmlObj, self.htmlObj.htmlId)
    self.htmlObj.js.grp_line_ripple = Ripple.LineRipple(self.htmlObj, ".%s" % cls)

  def button(self):
    """

    https://material.io/develop/web/components/buttons/
    
    :return:
    """
    cls = "mdc-button"
    self.htmlObj.attr['class'].add(cls)

