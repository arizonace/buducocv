#!/usr/bin/env python3
# azce::HighlightsHtml.py - Arizona Edwards
# Created: 2024-12-01 21:19-EST

class BuducoCvHtml:
    @staticmethod
    def get_template(name):
        return getattr(BuducoCvHtml, name+"_row", None)

    @staticmethod
    def get_template_start(name):
        return getattr(BuducoCvHtml, name+"_start", None)

    @staticmethod
    def get_template_end(name):
        return getattr(BuducoCvHtml, name+"_end", None)

    @staticmethod
    def fix_dict(d, template):
        pass

    competency_row ="""\
    <tr>
      <td class="competency-name">
        <p>{skill}</p>
      </td>
      <td class="competency-years">
        {YoE}
      </td>
      <td class="competency-years-plus">
        {YoEp}
      </td>
      <td class="competency-span">
        <p><span class="spanchart">{sparks}</span></p>
      </td>
      <td class="competency-rating">
        <p><span class="starrating">{Star}</span></p>
      </td>
      <td class="competency-keywords">
        <p>{caption}</p>
      </td>
    </tr>
"""

    competency_start ="""\
<table cellpadding="0" cellspacing="0" class="competencies-table" width="100%">
  <tbody>
    <tr class="cv-section-header">
      <td colspan="6">
        <p>Skills</p>
      </td>
    </tr>

    <!-- Column Headers -->
    <tr class="cv-column-headers">
      <td class="competency-name">
        <p>Skill</p>
      </td>
      <td class="competency-years">
        <p>YoE</p>
      </td>
      <td class="competency-years-plus">
        <p></p>
      </td>
      <td class="competency-span">
        <p>Engagement</p>
      </td>
      <td class="competency-rating">
        <p>Rating</p>
      </td>
      <td>
        <p>Description/Keywords</p>
      </td>
    </tr>
"""

    competency_end ="""\
    <tr class="competency-narrative">
      <td colspan="6">
        <p>
          While I do not claim to maintain focused expertise in all the above simultaneously, I have a strong inventory of current and refreshable skills and solution finding experience.
          The table above is my attempt to estimate and depict for each skill my:
        </p>
        <p class="competency-bullets">
          <span>◇ proficiency development;</span>
          <span>◇ engagement over time;</span>
          <span>◇ overall self rating.</span>
          <br/>
        </p>
        <p>
          I look forward to the opportunity to prove myself via interviews and assessments, and to contribute positively to your organization.
        </p>
      </td>
    </tr>
  </tbody>
</table>
"""

    discipline_row ="""\
    <tr>
      <td>
        <p>{Discipline}</p>
      </td>
      <td>
        <p>{Engagement}</p>
      </td>
    </tr>
"""

    discipline_start ="""\
<table cellpadding="0" cellspacing="0" class="cv-section-table" width="100%">
  <tbody>
    <tr class="cv-section-header">
      <td colspan="2">
        <p>Aspects</p>
      </td>
    </tr>
"""

    discipline_end ="""\
  </tbody>
</table>
"""

    html_start ="""\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
  <title>{DocTitle}</title>
  <link href="budu-cv-w.css" media="print,screen" rel="stylesheet" type="text/css" />
  <script type="text/javascript" src="jquery-3.1.1.js"></script>
  <script type="text/javascript" src="jquery.sparkline.js"></script>
  <script type="text/javascript" src="budu-cv.js"></script>
  <script type="text/javascript">$(function() {{front_page_load();}});</script>
</head>
<body>
<div class="cv-page">
"""

    html_end ="""\
</div>
</body>
</html>
"""
