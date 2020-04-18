

class Inputs(object):

  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def chips(self, text):
    """

    https://material.io/resources/icons/?style=baseline

    :param text:
    """
    div = self.context.rptObj.ui.div("text")
    div.style.clear_all()
    div.attr["class"].add("mdc-chip")
    div.attr["role"] = 'row'
    return div

  def input(self, value="", label=""):
    """

    https://material-components.github.io/material-components-web-catalog/#/component/text-field?icons=leadingIcon&type=outlined

    :param text:
    """
    schema = {"type": 'ripple',
              'children': [
                  {"type": 'div', "class": "mdc-text-field__ripple", 'css': False},
                  {"type": 'input', "class": "mdc-text-field__input", 'css': False, 'args': {'text': value}},
                  {"type": 'div', "class": "mdc-line-ripple", 'css': False},
      ]
    }

    ripple = self.context.rptObj.ui.div().set_attrs({"class": "mdc-text-field__ripple", 'css': None})
    text = self.context.rptObj.ui.inputs.d_text(value).set_attrs({"class": "mdc-text-field__input", 'css': None, "aria-labelledby": "my-label-id"})
    val = self.context.rptObj.ui.texts.label(label).set_attrs({"class": "mdc-floating-label", 'css': None, 'for': text.htmlId})
    line = self.context.rptObj.ui.div().set_attrs({"class": "mdc-line-ripple", 'css': None})

    cont = self.context.rptObj.ui.texts.label([ripple, text, val, line]).set_attrs({"class": "mdc-text-field", 'css': None})
    return cont

  def filled(self, value="", label=""):
    """

    https://material-components.github.io/material-components-web-catalog/#/component/text-field?icons=leadingIcon&type=outlined

    :param text:
    """
    schema = {"type": 'ripple',
              'children': [
                  {"type": 'div', "class": "mdc-text-field__ripple", 'css': False},
                  {"type": 'input', "class": "mdc-text-field__input", 'css': False, 'args': {'text': value}},
                  {"type": 'div', "class": "mdc-line-ripple", 'css': False},
      ]
    }
    html_b = self.context.rptObj.materials.composite(schema)
    self.context.add_cls(html_b)
    return html_b

  def outlined(self, value="", label=""):
    """
    const textField = new MDCTextField(document.querySelector('.mdc-text-field'))

    https://material.io/develop/web/components/input-controls/text-field/

    :param text:
    """
    text = self.context.rptObj.ui.inputs.d_text(value).set_attrs({"class": "mdc-text-field__input", 'css': None, "aria-labelledby": "my-label-id"})
    div = self.context.rptObj.ui.div().set_attrs({"class": "mdc-notched-outline", 'css': None})

    div += self.context.rptObj.ui.div().set_attrs({"class": "mdc-notched-outline__leading", 'css': None})
    notch = self.context.rptObj.ui.div().set_attrs({"class": "mdc-notched-outline__notch", 'css': None})
    notch += self.context.rptObj.ui.texts.label(label).set_attrs({"class": "mdc-floating-label", 'css': None, 'for': text.htmlId})

    div += notch
    div += self.context.rptObj.ui.div().set_attrs({"class": "mdc-notched-outline__trailing", 'css': None})

    cont = self.context.rptObj.ui.div([text, div]).set_attrs({"class": "mdc-text-field mdc-text-field--outlined", 'css': None})
    return cont

  def textarea(self, value="", label="", width=(100, '%'), rows=5, placeholder=None, background_color=None, htmlCode=None,
               options=None, profile=None):
    """
    Description:
    ------------
    const lineRipple = new mdc.textField.MDCTextField(document.querySelector('.mdc-text-field'));

    :param text:
    :param width:
    :param rows:
    :param placeholder:
    :param background_color:
    :param htmlCode:
    :param options:
    :param profile:
    """
    text = self.context.rptObj.ui.inputs.textarea(value).set_attrs({"class": "mdc-text-field__input", 'css': None, "aria-labelledby": "my-label-id"})
    div = self.context.rptObj.ui.div().set_attrs({"class": "mdc-notched-outline", 'css': None})

    div += self.context.rptObj.ui.div().set_attrs({"class": "mdc-notched-outline__leading", 'css': None})
    notch = self.context.rptObj.ui.div().set_attrs({"class": "mdc-notched-outline__notch", 'css': None})
    notch += self.context.rptObj.ui.texts.label(label).set_attrs({"class": "mdc-floating-label", 'css': None, 'for': text.htmlId})

    div += notch
    div += self.context.rptObj.ui.div().set_attrs({"class": "mdc-notched-outline__trailing", 'css': None})

    cont = self.context.rptObj.ui.texts.label([text, div]).set_attrs({"class": "mdc-text-field mdc-text-field--outlined", 'css': None})
    return cont
