

class Text(object):
  """
  """

  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def ripple(self):
    """
    """
    label = self.context.rptObj.ui.texts.label()
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
