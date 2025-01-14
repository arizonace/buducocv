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
        if template == "detail":
            d['ActivitiesP'] = "\n          ".join(["<p>{line}</p>".format(line=line) for line in d["Activities"].split("\n") ])

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
<table cellpadding="0" cellspacing="0" class="cv-section-table competencies-table" width="100%">
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
          <span>◇ accumulated experience;</span>
          <span>◇ engagement over time;</span>
          <span>◇ overall self rating.</span>
          <br/>
        </p>
        <p>
          I look forward to the opportunity to demonstrate my skills, and contribute positively to your organization.
          <small><sup>*</sup>Combined over time.</small>
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

    summary_row ="""\
    <tr class="summary-label">
      <td class="summary-label">
        <p>{Name}</p>
      </td>
      <td class="summary-position">
        <p>{Title}</p>
      </td>
      <td class="summary-timeframe">
        <p>{Timeframe}</p>
      </td>
    </tr>
    <tr class="summary-did">
      <td colspan="3" class="summary-did">
        <p>{Did}</p>
      </td>
    </tr>
"""

    summary_start ="""\
<table cellspacing="0" cellpadding="0" class="cv-section-table" width="100%">
  <tbody>
    <tr class="cv-section-header">
      <td colspan="3">
        <p>Work Experience</p>
      </td>
    </tr>
"""

    summary_end ="""\
      <tr class="summary-label show-hide">
        <td colspan="3" class="summary-label">
          <p><button class="show-hide" id="show-details" onclick="toggleDetails()">Show Details</button></p>
        </td>
      </tr>
  </tbody>
</table>
"""

    detail_row ="""\
    <table cellspacing="0" cellpadding="0" class="detail-table" width="100%">
      <tr class="detail-label">
        <td class="detail-label">
          <p><strong>{Label}</strong></p>
          <p>{Timeframe}</p>
          <p>{Position}</p>
          <span class="detail-endyear" id="endyear-{jobid}">{end_y}</span>
        </td>
        <td class="detail-address">
          <p><a href="{URL}">{URL}</a></p>
          <p>{Address}</p>
          <p>{Phone}</p>
        </td>
      </tr>
      <tr class="detail-summary">
        <td colspan="2">
          <table class="detail-fields">
            <tr><td class="detail-field-label">Organization:</td><td class="detail-field-value">{Organization}</td></tr>
            <tr><td class="detail-field-label">Responsibilities:</td><td class="detail-field-value">{Responsibilities}</td></tr>
            <tr><td class="detail-field-label">Languages:</td><td class="detail-field-value">{Languages}</td></tr>
            <tr><td class="detail-field-label">Methodologies:</td><td class="detail-field-value">{Methodologies}</td></tr>
            <tr><td class="detail-field-label">Source Control:</td><td class="detail-field-value">{SourceControl}</td></tr>
            <tr><td class="detail-field-label">Platforms:</td><td class="detail-field-value">{Platforms}</td></tr>
            <tr><td class="detail-field-label">Applications:</td><td class="detail-field-value">{Applications}</td></tr>
          </table>
        </td>
      </tr>
      <tr class="detail-company">
        <td colspan="2"><p>{Company}</p></td>
      </tr>
      <tr class="detail-activity">
        <td colspan="2">
          {ActivitiesP}</td>
      </tr>
      <tr class="detail-highlights">
        <td colspan="2">
          {highlightsHTML}</td>
      </tr>
    </table>
"""
    detail_start ="""\
<div id="details-tables">
"""

    detail_end ="""\
</div> <!-- details-tables -->
"""

    sparks_row ="""\
    <tr>
      <td class="competency-name" valign="top">
        <p>{skill}</p>
      </td>
      <td class="competency-span" valign="top">
        <p><span class="spanchart">{sparks}</span></p>
      </td>
      <td class="competency-span" valign="top">
        <p><span class="spanchart2">{focus}</span></p>
      </td>
    </tr>
"""
    sparks_start ="""\
<table cellpadding="0" cellspacing="0" class="competency" width="100%">
  <tbody>
    <tr>
      <td colspan="3" class="cv-section-header">
        <p>Skill Sparks</p>
      </td>
    </tr>
"""
    sparks_end ="""\
  </tbody>
</table>
"""


    html_start ="""\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
  <title>{DocTitle}</title>
  <link href="../web/cv/buducocv.css" media="print,screen" rel="stylesheet" type="text/css" />
  <script type="text/javascript" src="../web/cv/lib/jquery-3.1.1.js"></script>
  <script type="text/javascript" src="../web/cv/lib/jquery.sparkline.js"></script>
  <script type="text/javascript" src="../web/cv/buducocv.js"></script>
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
