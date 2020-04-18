
from epyk_materials.interfaces import CompButtons
from epyk_materials.interfaces import CompInputs
from epyk_materials.interfaces import CompIcons
from epyk_materials.interfaces import CompSliders
from epyk_materials.interfaces import CompNavigation
from epyk_materials.interfaces import CompTexts
from epyk_materials.interfaces import CompLists

from epyk_materials.core.html import MdcHtml
from epyk_materials.core.css import Classes


class Materials(object):

  def __init__(self, rptObj):
    self.rptObj = rptObj
    self.navbar = self.navigation.bar #: shortcut for bar :func:`epyk.interfaces.components.CompNavigation.Navigation.bar`
    self.icon = self.icons.icon

  @property
  def lists(self):
    """
    Description:
    ------------
    """
    return CompLists.List(self)

  @property
  def texts(self):
    """
    Description:
    ------------
    """
    return CompTexts.Text(self)

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

  def composite(self, schema, width=(None, "%"), height=(None, "px"), htmlCode=None, helper=None, options=None, profile=None):
    """
    Description:
    ------------
    Composite bespoke object.

    This obhect will be built based on its schema. No specific CSS Style and class will be added to this object.
    The full definition will be done in the nested dictionary schema.

    Example
    schema = {'type': 'div', 'css': {}, 'class': , 'attrs': {} 'arias': {},  'children': [
        {'type': : {...}}
        ...
    ]}

    Attributes:
    ----------
    :param schema:
    :param width:
    :param height:
    :param htmlCode:
    :param helper:
    :param options:
    :param profile:
    """
    html_help = MdcHtml.MdcComposite(self.rptObj, schema, width=width, height=height, htmlCode=htmlCode, profile=profile, options=options or {}, helper=helper)
    self.register(html_help)
    return html_help

  def add_cls(self, html_comp):
    html_comp.style.mdc = Classes.Catalog(self.rptObj, html_comp)

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
