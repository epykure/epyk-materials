

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

  def progressbar(self, number=0, total=100, width=(100, '%'), label="", height=(20, 'px'), htmlCode=None, attrs=None,
                  helper=None, options=None, profile=None):
    """
    The MDC Linear Progress component is a spec-aligned linear progress indicator component adhering to the Material Design progress & activity requirements.

    https://material.io/develop/web/components/linear-progress/

    """
    schema = {"type": 'div',
      'arias': {'role': 'progressbar', 'valuemin': 0, 'valuemax': total, 'valuenow': number, 'label': label},
      'children': [
        {"type": 'div', 'class': 'mdc-linear-progress__buffering-dots'},
        {"type": 'div', 'class': 'mdc-linear-progress__buffer'},
        {"type": 'div', 'class': 'mdc-linear-progress__bar mdc-linear-progress__primary-bar', 'children': [
          {"type": 'span', 'class': 'mdc-linear-progress__bar-inner'}
        ]},
        {"type": 'div', 'class': 'mdc-linear-progress__bar mdc-linear-progress__secondary-bar', 'children': [
          {"type": 'span', 'class': 'mdc-linear-progress__bar-inner'}
        ]},
    ]}
    html_pr = self.context.rptObj.materials.composite(schema)
    self.context.add_cls(html_pr)
    html_pr.style.mdc.linear_progress()
    return html_pr
