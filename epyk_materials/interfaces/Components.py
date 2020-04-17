
from epyk_materials.interfaces import CompButtons
from epyk_materials.interfaces import CompInputs
from epyk_materials.interfaces import CompIcons
from epyk_materials.interfaces import CompSliders
from epyk_materials.interfaces import CompNavigation


class Materials(object):

  def __init__(self, rptObj):
    self.rptObj = rptObj
    self.navbar = self.navigation.bar #: shortcut for bar :func:`epyk.interfaces.components.CompNavigation.Navigation.bar`

  @property
  def navigation(self):
    """
    Description:
    ------------
    """
    return CompNavigation.Navigation(self)

  @property
  def buttons(self):
    """
    Description:
    ------------
    """
    return CompButtons.Buttons(self)

  @property
  def inputs(self):
    """
    Description:
    ------------
    """
    return CompInputs.Inputs(self)

  @property
  def icons(self):
    """
    Description:
    ------------
    """
    return CompIcons.Icon(self)

  @property
  def sliders(self):
    """
    Description:
    ------------
    """
    return CompSliders.Slider(self)

  def register(self, html_comp):
    """
    Description:
    ------------
    Internal function to register a HTML component based on its memory id.

    Related Pages:

    :param html_comp: The html component

    return the html component
    """
    self.rptObj.htmlItems[id(html_comp)] = html_comp
    self.rptObj.content.append(id(html_comp))
    return html_comp
