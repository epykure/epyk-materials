

from epyk.core.html import HtmlButton


class Button(HtmlButton.Button):
  __reqCss, __reqJs = ['material-components-web'], ['material-components-web']

  def __init__(self, report, text, icon, width, height, htmlCode, tooltip, profile, options):
    super(Button, self).__init__(report, [], icon, width, height, htmlCode, tooltip, profile, options)
    self.attr['class'].add('mdc-fab')

  def __add__(self, htmlObj):
    """ Add items to a container """
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    if not isinstance(self.val, list):
      self.val = [self.val]
    self.val.append(htmlObj)
    return self

  def __str__(self):
    return '<button %s>%s</button>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val)
