
from epyk_materials.core import html


class Inputs(object):

  def __init__(self, context):
    self.context = context

  def chips(self, text):

    div = self.context.rptObj.ui.div("text")
    div.style.clear_all()
    div.attr["class"].add("mdc-chip")
    div.attr["role"] = 'row'
    return div
