

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
              {"type": 'div', 'css': False, 'class': "mdc-tab-scroller__scroll-content", 'children': [
                #{"type": 'button', 'css': False, 'class': 'dc-tab mdc-tab--active', 'attrs': {"role": 'tab'}, 'arias': {"selected": False}, 'children': [
                  # {"type": 'div', 'css': False, 'class': 'mdc-tab__content', 'children': [
                  #   {"type": 'span', 'css': False, 'class': 'mdc-tab__icon material-icons', 'arias': {"hidden": True}},
                  #   {"type": 'span', 'css': False, 'class': 'mdc-tab__text-label', 'args': {"text": "Test"}},
                  # ]},
                  # {"type": 'div', 'css': False, 'class': 'mdc-tab-indicator mdc-tab-indicator--active', 'children': [
                  #   {"type": 'span', 'css': False, 'class': 'mdc-tab-indicator__content mdc-tab-indicator__content--underline'}]},
                  # {"type": 'span', 'css': False, 'class': 'mdc-tab__ripple'}
                #]
               #},
              ]}
            ]}
          ]},
        ]
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

    html_t = self.context.rptObj.materials.composite(schema)
    self.context.add_cls(html_t)
    html_t.style.mdc.tab_bar()
    return html_t

  def bar(self):
    """

    https://material.io/develop/web/components/tabs/tab-bar/
    """
    pass
