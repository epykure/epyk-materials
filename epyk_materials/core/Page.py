
from epyk.core import Page

from epyk_materials.interfaces import Components


# Modules extension required
MODULES_EXTS = {
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

  @property
  def materials(self):
    """
    Description:
    ------------


    Related Pages:

      https://material.io/develop/web/

    :rtype: :doc:`Components.Materials <report/ui>`

    :return: Python HTML object
    """
    if self._mt is None:
      self._mt = Components.Materials(self)
    return self._mt
