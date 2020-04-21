

class Navigation(object):
  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def bar(self, icon=None, title=None, width=(100, '%'), height=(40, 'px'), options=None, profile=False):

    return
