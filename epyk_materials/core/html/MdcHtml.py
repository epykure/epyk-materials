
from epyk.core.html import HtmlTextComp


class MdcComposite(HtmlTextComp.Composite):

  @property
  def _get_comp_map(self):
    """
    Description:
    ------------

    """
    return {
      'div': self._report.ui.div,
      'textarea': self._report.ui.textarea,
      'button': self._report.ui.section,
      'label': self._report.ui.label,
      'header': self._report.ui.header,
      'section': self._report.ui.section,
      'input': self._report.ui.inputs.d_text,
      'icon': self._report.materials.icon,
      'span': self._report.ui.texts.span,
      'circle': self._report.ui.charts.svg.circle,
      'checkbox': self._report.ui.inputs.checkbox,
      'ripple': self._report.materials.texts.ripple,
    }
