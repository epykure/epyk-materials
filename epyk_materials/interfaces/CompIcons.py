

class Icon(object):

  def __init__(self, context):
    self.context = context

  def icon(self, text):
    span = self.context.rptObj.ui.texts.span(text)
    span.style.clear_all()
    span.attr["class"].add("material-icons")
    return span
