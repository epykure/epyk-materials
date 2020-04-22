from epyk_materials.core import JsMdcComponents


class Navigation(object):

  def __init__(self, context):
    context.rptObj.jsImports.add("material-components-web")
    context.rptObj.cssImport.add("material-components-web")
    self.context = context

  def tabs(self, data):
    """
    Tabs organize and allow navigation between groups of content that are related and at the same level of hierarchy.
    The Tab Bar contains the Tab Scroller and Tab components.

    https://material.io/develop/web/components/tabs/tab-bar/

    """
    schema = {"type": 'div', 'css': False, 'attrs': {'role': 'tablist'},
      'children': [
        {"type": 'div', 'css': False, 'class': 'mdc-tab-scroller', 'children': [
          {"type": 'div', 'css': False, 'class': "mdc-tab-scroller__scroll-area", 'children': [
            {"type": 'div', 'css': False, 'class': "mdc-tab-scroller__scroll-content", 'children': []}
          ]}
      ]}]
    }

    for text in data:
      schema['children'][0]['children'][0]['children'][0]['children'].append(
        {"type": 'button', 'css': False, 'class': 'mdc-tab mdc-tab--active', 'attrs': {"role": 'tab'},
         'arias': {"selected": False}, 'children': [
            {"type": 'div', 'css': False, 'class': 'mdc-tab__content', 'children': [
              {"type": 'span', 'css': False, 'class': 'mdc-tab__icon material-icons', 'arias': {"hidden": True}},
              {"type": 'span', 'css': False, 'class': 'mdc-tab__text-label', 'args': {"text": text}},
            ]},
             {"type": 'div', 'css': False, 'class': 'mdc-tab-indicator mdc-tab-indicator', 'children': [
               {"type": 'span', 'css': False, 'class': 'mdc-tab-indicator__content mdc-tab-indicator__content--underline'}]},
             {"type": 'span', 'css': False, 'class': 'mdc-tab__ripple'}]
         })

    html_t = self.context.rptObj.materials.composite(schema, options={"reset_class": True})

    #
    dom_obj = JsMdcComponents.TabBar(html_t)
    html_t.style.builder(html_t.style.varName, dom_obj.instantiate("#%s" % html_t.htmlId))
    # Add the specific dom features
    html_t.dom = dom_obj
    return html_t

  def bar(self, title, icon="menu", buttons=None):
    """
    MDC Top App Bar acts as a container for items such as application title, navigation icon, and action items.
    
    https://material.io/develop/web/components/tabs/tab-bar/
    """
    schema = {"type": 'header', 'css': False, 'children': [
                {"type": 'div', 'css': False, 'class': 'mdc-top-app-bar__row', 'children': [
                  {"type": 'section', 'css': False, 'class': "mdc-top-app-bar__section mdc-top-app-bar__section--align-start", 'children': [
                    {"type": 'icon', 'class-keep': True, 'css': False, 'args': {'text': icon}, 'class': "mdc-top-app-bar__navigation-icon mdc-icon-button"},
                    {"type": 'span', 'css': False, 'class': 'mdc-top-app-bar__title', 'args': {"text": title}},
                  ]},
                  {"type": 'div', 'css': False, 'class': 'mdc-top-app-bar__section mdc-top-app-bar__section--align-end', 'attrs': {"role": 'toolbar'}, 'children': []}
                ]}
    ]}

    if buttons is not None:
      for b in buttons:
        schema['children'][1]['children'].append(
          {"type": 'icon', 'class-keep': True, 'css': False, 'arias': {'label': b}, 'args': {'text': b}, 'class': "mdc-top-app-bar__navigation-icon mdc-icon-button"})
    html_t = self.context.rptObj.materials.composite(schema, options={"reset_class": True})

    #
    dom_obj = JsMdcComponents.TopBar(html_t)
    html_t.style.builder(html_t.style.varName, dom_obj.instantiate("#%s" % html_t.htmlId))
    # Add the specific dom features
    html_t.dom = dom_obj
    return html_t
