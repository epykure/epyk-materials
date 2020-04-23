
from epyk.core import Page
from epyk.core.css import Defaults

from epyk_materials.interfaces import Comp

# Remove the default layout in all the component done by Epyk Core
Defaults.DEFAULT_STYLE = None

# Modules extension required
MODULES_EXTS = {
  'material-icons': {
    'website': 'https://material.io/resources/icons/?style=baseline',
    'services': [
      {'type': 'css', 'url': 'https://fonts.googleapis.com/icon', 'values': {'family': 'Material+Icons'}},
    ]
  },

  'material-components-web': {
    'version': '5.1.0',
    'website': 'https://material.io/components',
    'modules': [
      {'script': 'material-components-web.min.js', 'path': 'material-components-web/%(version)s/'},
      {'script': 'material-components-web.min.css', 'path': 'material-components-web/%(version)s/'}
  ]},
}


class Report(Page.Report):

  ext_packages = MODULES_EXTS

  def __init__(self):
    super(Report, self).__init__()
    self._mt = None
    # Override the icon to use the one from the github repository
    self.headers._favicon_url = "https://raw.githubusercontent.com/epykure/epyk-materials/master/epyk_materials/static/images/epyk_materials_logo.ico"

  @property
  def materials(self):
    """
    Description:
    ------------
    Set the material components entry point.
    This will be available in the same way than ui is available for anything else in the core framework.

    Related Pages:

      https://material.io/develop/web/

    :rtype: :doc:`Components.Materials <report/ui>`

    :return: Python HTML object
    """
    if self._mt is None:
      self._mt = Comp.Materials(self)
    return self._mt

  @property
  def outs(self):
    """
    Description:
    ------------
    Change the styles before rendering the page
    Override the predefined colors with the ones from the theme
    """
    self.css.customText('''
:root {--mdc-theme-primary: %(color)s; --mdc-theme--on-primary: %(color)s; --mdc-theme--primary-bg: %(color)s;}
.mdc-text-field--focused:not(.mdc-text-field--disabled) .mdc-floating-label {color: var(--mdc-theme-primary);}
    ''' % {"color": self.theme.success[1]})
    return super(Report, self).outs
