

from epyk.core.html import HtmlButton


class Button(HtmlButton.Button):
  __reqCss, __reqJs = ['material-components-web', "material-icons"], ['material-components-web']

  def __init__(self, report, htmlObj, icon, width, height, htmlCode, tooltip, profile, options):
    if htmlObj and isinstance(htmlObj, list):
      newHtmlObj = []
      for obj in htmlObj:
        if isinstance(obj, list) and obj:
          newHtmlObj.append(report.ui.div(obj))
        else:
          newHtmlObj.append(obj)
        if hasattr(newHtmlObj[-1], 'inReport'):
          if options.get('inline'):
            newHtmlObj[-1].style.css.display = 'inline-block'
          newHtmlObj[-1].inReport = False
      htmlObj = newHtmlObj
    elif htmlObj is not None and hasattr(htmlObj, 'inReport'):
      htmlObj.inReport = False
    super(Button, self).__init__(report, htmlObj, icon, width, height, htmlCode, tooltip, profile, options)
    self.style.clear_all()
    self.attr['class'].add('mdc-fab')

  def __add__(self, htmlObj):
    """ Add items to a container """
    htmlObj.inReport = False # Has to be defined here otherwise it is set to late
    if not isinstance(self.val, list):
      self.val = [self.val]
    self.val.append(htmlObj)
    return self

  def __str__(self):
    str_div = "".join([v.html() if hasattr(v, 'html') else str(v) for v in self.val])
    return '<button %s>%s</button>' % (self.get_attrs(pyClassNames=self.style.get_classes()), self.val)
