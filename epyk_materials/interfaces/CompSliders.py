

class Slider(object):
  """
  Description:
  ------------
  This module is relying on some Jquery IU components

  The slider and progress bar components can be fully described on the corresponding website

    - https://jqueryui.com/progressbar/
    - https://jqueryui.com/slider/

  As this module will return those object, all the properties and changes defined in the documentation can be done.
  """
  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def progressbar(self, number=0, total=100, width=(100, '%'), height=(20, 'px'), htmlCode=None, attrs=None,
                  helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Add a progress bar component to the page

    Usage::

      rptObj.ui.sliders.progressbar(300)

    Underlying HTML Objects:

      - :class:`epyk.core.html.HtmlEvent.ProgressBar`

    Related Pages:

      https://jqueryui.com/progressbar/

    Attributes:
    ----------
    :param number: A number (by default between 0 and 100)
    :param total: A number
    :param width: Optional. Integer for the component width
    :param height: Optional. Integer for the component height
    :param htmlCode:
    :param attrs:
    :param helper:
    :param profile:
    """
    buff = self.context.rptObj.ui.div().set_attrs({"class": "mdc-linear-progress__buffe", 'css': None})
    buff += self.context.rptObj.ui.div().set_attrs({"class": "mdc-linear-progress__buffer-bar", 'css': None})
    buff += self.context.rptObj.ui.div().set_attrs({"class": "mdc-linear-progress__buffering-dots", 'css': None})
    bar = self.context.rptObj.ui.div().set_attrs({"class": "mdc-linear-progress__bar mdc-linear-progress__primary-bar", 'css': None})
    bar += self.context.rptObj.ui.texts.span().set_attrs({"class": "mdc-linear-progress__bar-inner", 'css': None})
    bar_sec = self.context.rptObj.ui.div().set_attrs({"class": "mdc-linear-progress__bar mdc-linear-progress__secondary-bar", 'css': None})
    bar_sec += self.context.rptObj.ui.texts.span().set_attrs({"class": "mdc-linear-progress__bar-inner", 'css': None})
    html_pr = self.context.rptObj.ui.div([buff, bar, bar_sec], width=width, height=height, options=options, profile=profile)
    html_pr.set_attrs({"role": "progressbar", "class": "mdc-linear-progress", "aria-valuemin": 0, "aria-valuemax": total,
                       "aria-valuenow": number})
    return html_pr
