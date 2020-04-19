

class Text(object):
  """
  """

  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def ripple(self, htmlCode=None):
    """
    """
    label = self.context.rptObj.ui.texts.label(htmlCode=htmlCode)
    label.set_attrs({"class": None, 'css': None})
    self.context.add_cls(label)
    label.style.mdc.line_ripple()
    return label

  def icon(self, value):
    """

    https://material.io/develop/web/components/input-controls/text-field/icon/
    """
    schema = {"type": 'label', 'class': 'mdc-text-field mdc-text-field--with-leading-icon',
              'children': [
                {"type": 'icon', "class": "material-icons mdc-text-field__icon mdc-text-field__icon--leading",
                 'attrs': {'tabindex': 0}, 'arias': {'role': 'button'}, 'css': False, 'args': {'text': value}},
                {"type": 'input', 'class': 'mdc-text-field__input'},
                {"type": 'span', 'class': 'mdc-floating-label'},
                {"type": 'div', 'class': 'mdc-line-ripple'},
              ]
    }
    html_t = self.context.rptObj.materials.composite(schema)
    self.context.add_cls(html_t)
    html_t.style.mdc.text_icon()
    return html_t

  def floating(self, label):
    """
    Floating labels display the type of input a field requires.
    Every Text Field and Select should have a label, except for full-width text fields, which use the input’s placeholder attribute instead.

    https://material.io/develop/web/components/input-controls/floating-label/

    :param label:
    """
    span = self.context.rptObj.ui.texts.span(label)
    span.set_attrs({"class": None, 'css': None})
    self.context.add_cls(span)
    span.style.mdc.text_floating()
    return span
