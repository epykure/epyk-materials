

from epyk_materials.core import html


class Buttons(object):

  def __init__(self, context):
    self.context = context

  def button(self, text="", icon=None, width=(None, "%"), height=(None, "px"), htmlCode=None, tooltip=None, profile=None, options=None):

    html_button = html.MtButtons.Button(self.context.rptObj, text, icon, width, height, htmlCode=htmlCode,
                                         tooltip=tooltip, profile=profile, options=options)
    self.context.register(html_button)
    return html_button
