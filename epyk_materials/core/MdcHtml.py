
from epyk.core.html import HtmlTextComp


class MdcComposite(HtmlTextComp.Composite):

  @property
  def _get_comp_map(self):
    """
    Description:
    ------------
    This list is specific for the Material components.

    Span are replaced by div as I did not want to use the span as a container object.
    I believe this component should remain a base one.

    """
    return {
      'div': self._report.ui.div,
      'textarea': self._report.ui.textarea,
      'button': self._report.ui.button,
      'label': self._report.ui.label,
      'header': self._report.ui.header,
      'section': self._report.ui.section,
      'input': self._report.ui.inputs.d_text,
      'radio': self._report.ui.inputs.d_radio,
      'span': self._report.ui.texts.span,
      'circle': self._report.ui.charts.svg.circle,
      'checkbox': self._report.ui.inputs.checkbox,

      'list': self._report.ui.list,
      'item': self._report.ui.lists.item,

      'icon': self._report.materials.icon,
      'mdc_icon': self._report.materials.icon,
      'mdc_floating': self._report.materials.texts.floating,
      'mdc_field': self._report.materials.texts.field,
      'mdc_line': self._report.materials.texts.line,
      'mdc_radio': self._report.materials.inputs.mdc_radio,
    }
