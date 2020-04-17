
from epyk_materials.interfaces import CompButtons
from epyk_materials.interfaces import CompInputs
from epyk_materials.interfaces import CompIcons


class Materials(object):

  def __init__(self, rptObj):
    self.rptObj = rptObj

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
