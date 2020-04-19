

class Icon(object):

  def __init__(self, context):
    self.context = context

  def icon(self, text=None, in_text_field=False):
    """

    Attributes:
    ----------
    """
    self.context.rptObj.cssImport.add("material-icons")
    span = self.context.rptObj.ui.texts.span(text)
    span.style.clear_all()
    span.attr["class"].add("material-icons")
    if in_text_field:
      span.attr["class"].add("mdc-text-field__icon")
    return span

  def clock(self, position=None, tooltip="Last Updated Time", width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    """
    Description:
    ------------

    Attributes:
    ----------
    :param position: Optional. The position of the icon in the line (left, right, center)
    :param tooltip: Optional. A string with the value of the tooltip
    :param width: Optional. A tuple with the integer for the component width and its unit
    :param height: Optional. A tuple with the integer for the component height and its unit
    :param htmlCode: Optional. An identifier for this component (on both Python and Javascript side)
    :param profile: Optional. A flag to set the component performance storage
    """
    return self.icon('alarm', tooltip, position, width, height, htmlCode, profile)

  def refresh(self, position=None, tooltip="Last Updated Time", width=(None, 'px'), height=(None, 'px'),
            htmlCode=None, profile=None):
    return self.icon('refresh', tooltip, position, width, height, htmlCode, profile)
