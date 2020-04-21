

class Slider(object):
  """
  Description:
  ------------
  This module is relying on some Jquery IU components

  The slider and progress bar components can be fully described on the corresponding website

  Related Pages:

    https://jqueryui.com/progressbar/
    https://jqueryui.com/slider/

  As this module will return those object, all the properties and changes defined in the documentation can be done.
  """
  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def progressbar(self, number=0, total=100, label=""):
    """
    The MDC Linear Progress component is a spec-aligned linear progress indicator component adhering to the Material Design progress & activity requirements.

    Related Pages:

      https://material.io/develop/web/components/linear-progress/

    """
    schema = {"type": 'div', 'css': None,
      'arias': {'role': 'progressbar', 'valuemin': 0, 'valuemax': 1, 'valuenow': number/total, 'label': label},
      'children': [
        {"type": 'div', 'class': 'mdc-linear-progress__buffering-dots', 'css': None},
        {"type": 'div', 'class': 'mdc-linear-progress__buffer', 'css': None},
        {"type": 'div', 'css': None, 'class': 'mdc-linear-progress__bar mdc-linear-progress__primary-bar', 'children': [
          {"type": 'span', 'class': 'mdc-linear-progress__bar-inner', 'css': None}
        ]},
        {"type": 'div', 'css': None, 'class': 'mdc-linear-progress__bar mdc-linear-progress__secondary-bar', 'children': [
          {"type": 'span', 'class': 'mdc-linear-progress__bar-inner', 'css': None}
        ]},
    ]}
    html_pr = self.context.rptObj.materials.composite(schema)
    self.context.add_cls(html_pr)
    html_pr.style.mdc.linear_progress()
    html_pr.onReady([
      html_pr.js.progress.setProgress(number)
    ])
    return html_pr

  def slider(self, value, total=100, label=""):
    """
    MDC Slider provides an implementation of the Material Design slider component.

    Related Pages:

      https://material.io/develop/web/components/input-controls/sliders/

    :param value:
    :param total:
    :param label:
    """
    schema = {"type": 'div', 'css': None, 'attrs': {"tabindex": 0},
              'arias': {"role": 'slider', 'label': label, 'valuenow': value, 'valuemax': total, 'valuemin': 0}, 'children': [
        {"type": 'div', 'class': 'mdc-slider__track-container', 'css': None, 'children': [
          {"type": 'div', 'class': 'mdc-slider__track', 'css': None}
        ]},
        {"type": 'div', 'class': 'mdc-slider__thumb-container', 'css': None, 'children': [
          {"type": 'circle', 'class': 'mdc-slider__thumb', 'css': None,
           'args': {"x": 10.5, "y": 10.5, 'r': 7.875, "width": (21, "px"), "height": (21, "px")}}
        ]},
        #{"type": 'div', 'class': 'mdc-slider__focus-ring', 'css': None}
      ]

    }
    html_pr = self.context.rptObj.materials.composite(schema)
    self.context.add_cls(html_pr)
    html_pr.style.mdc.slider()
    return html_pr
