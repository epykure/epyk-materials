
from epyk_materials.core.js.css import Ripple
from epyk_materials.core.js.css import Button
from epyk_materials.core.js.css import Text


class Catalog(object):

  def __init__(self, report, htmlObj):
    self.__rptObj, self.htmlObj = report, htmlObj
    self.__ctx = {}

  def line_ripple(self):
    """

    :return:
    """
    cls = "mdc-text-field"
    css_id = "%s_%s" % (Ripple.LineRipple.varName, self.htmlObj.htmlId)

    self.htmlObj.attr['class'].add(cls)
    self.htmlObj.style.builder(css_id, Ripple.LineRipple.expr % "#%s" % self.htmlObj.htmlId)
    # attach to the object the Javascript shortcurs to be able to use the API
    self.htmlObj.js.line_ripple = Ripple.LineRipple(self.htmlObj, css_id)

  def text_icon(self):
    """
    Description:
    ------------
    Icons describe the type of input a text field requires. They can also be interaction targets.

    Related Pages:

			https://material.io/develop/web/components/input-controls/text-field/icon/
    """
    cls = "mdc-text-field-icon"
    css_id = "%s_%s" % (Text.Icon.varName, self.htmlObj.htmlId)

    self.htmlObj.attr['class'].add(cls)
    self.htmlObj.style.builder(css_id, Text.Icon.expr % "#%s" % self.htmlObj.htmlId)
    self.htmlObj.js.icon = Text.Icon(self.htmlObj, css_id)

  def text_floating(self):
    """
    Description:
    ------------
    Icons describe the type of input a text field requires. They can also be interaction targets.

    Related Pages:

      https://material.io/develop/web/components/input-controls/text-field/icon/
    """
    cls = "mdc-floating-label"
    css_id = "%s_%s" % (Text.Floating.varName, self.htmlObj.htmlId)

    self.htmlObj.attr['class'].add(cls)
    self.htmlObj.style.builder(css_id, Text.Floating.expr % "#%s" % self.htmlObj.htmlId)
    self.htmlObj.js.floating = Text.Floating(self.htmlObj, css_id)

  def text_notched_outline(self):
    """
    Description:
    ------------
    The notched outline is a border around all sides of either a Text Field or Select component.
    This is used for the Outlined variant of either a Text Field or Select.

    Related Pages:

      https://material.io/develop/web/components/input-controls/notched-outline/
    """
    cls = "mdc-text-field--outlined"
    css_id = "%s_%s" % (Text.Floating.varName, self.htmlObj.htmlId)

    self.htmlObj.attr['class'].add(cls)
    self.htmlObj.style.builder(css_id, Text.NothedOutline.expr % "#%s" % self.htmlObj.htmlId)
    self.htmlObj.js.outline = Text.NothedOutline(self.htmlObj, css_id)

  def button(self):
    """

    Related Pages:

      https://material.io/develop/web/components/buttons/

    :return:
    """
    cls = "mdc-button"
    self.htmlObj.attr['class'].add(cls)

  def switch(self):
    """

    Related Pages:

      https://material.io/develop/web/components/buttons/icon-buttons/

    :return:
    """
    cls = "mdc-switch"
    self.htmlObj.attr['class'].add(cls)
    self.htmlObj.style.builder("%s_%s" % (Button.Switch.varName, self.htmlObj.htmlId), Button.Switch.expr % "#%s" % self.htmlObj.htmlId)
    # attach to the object the Javascript shortcurs to be able to use the API
    self.htmlObj.js.icon = Button.Switch(self.htmlObj, "#%s" % self.htmlObj.htmlId)

  def button_icon(self):
    """

    Related Pages:

      https://material.io/develop/web/components/buttons/icon-buttons/

    :return:
    """
    cls = "mdc-icon-button"
    self.htmlObj.attr['class'].add(cls)
    self.htmlObj.style.builder(Button.Floating.varName, Button.Floating.expr % ".%s" % cls)
    # attach to the object the Javascript shortcurs to be able to use the API
    self.htmlObj.js.icon = Button.Floating(self.htmlObj, self.htmlObj.htmlId)
    self.htmlObj.js.grp_icon = Button.Floating(self.htmlObj, ".%s" % cls)

  def button_icon_toggle(self):
    """

    Related Pages:

      https://material.io/develop/web/components/buttons/icon-buttons/

    :return:
    """
    cls = "mdc-icon-button"
    self.htmlObj.attr['class'].add(cls)
    self.htmlObj.style.builder("%s_%s" % (Button.Switch.varName, self.htmlObj.htmlId), Button.Toggle.expr % ".%s" % cls)
    # attach to the object the Javascript shortcurs to be able to use the API
    self.htmlObj.js.toggle = Button.Toggle(self.htmlObj, "%s_%s" % (Button.Switch.varName, self.htmlObj.htmlId))

  def floating(self):
    """

    Related Pages:

      https://material.io/develop/web/components/buttons/floating-action-buttons/

    :return:
    """
    cls = "mdc-fab"
    self.htmlObj.attr['class'].add(cls)
    self.htmlObj.style.builder(Button.Floating.varName, Button.Floating.expr % ".%s" % cls)
    # attach to the object the Javascript shortcurs to be able to use the API
    self.htmlObj.js.floating = Button.Floating(self.htmlObj, self.htmlObj.htmlId)
    self.htmlObj.js.grp_floating = Button.Floating(self.htmlObj, ".%s" % cls)

  def linear_progress(self):
    """

    :return:
    """
    cls = "mdc-linear-progress"
    css_id = "%s_%s" % (Ripple.LinearProgress.varName, self.htmlObj.htmlId)

    self.htmlObj.attr['class'].add(cls)
    self.htmlObj.style.builder(css_id, Ripple.LinearProgress.expr % "#%s" % self.htmlObj.htmlId)
    self.htmlObj.js.icon = Ripple.LinearProgress(self.htmlObj, css_id)

  def slider(self):
    """

    :return:
    """
    cls = "mdc-slider"
    css_id = "%s_%s" % (Ripple.Slider.varName, self.htmlObj.htmlId)

    self.htmlObj.attr['class'].add(cls)
    self.htmlObj.style.builder(css_id, Ripple.Slider.expr % "#%s" % self.htmlObj.htmlId)
    self.htmlObj.js.slider = Ripple.Slider(self.htmlObj, css_id)

  def radio(self):
    """

    Related Pages:

      https://material.io/develop/web/components/input-controls/radio-buttons/

    :return:
    """
    cls = "mdc-radio"
    css_id = "%s_%s" % (Ripple.Radio.varName, self.htmlObj.htmlId)

    self.htmlObj.attr['class'].add(cls)
    self.htmlObj.style.builder(css_id, Ripple.Radio.expr % "#%s" % self.htmlObj.htmlId)
    self.htmlObj.js.radio = Ripple.Radio(self.htmlObj, css_id)

  def elevation(self):
    """
    Elevation is often already included within the baseline styles of other components (e.g. raised buttons, elevated cards).

    Related Pages:

      https://material.io/develop/web/components/elevation/
    """
    self.htmlObj.attr['class'].add("mdc-elevation--z1")
