#!/usr/bin/env python3
# azce::HighlightsHtml.py - Arizona Edwards
# Created: 2024-11-30 17:28-EST

class HighlightsHtml:
    link = '<a href="{url}">{title}</a>'
    highlight_start = '<li>{text}'
    highlight_end = '</li>'
    highlight_additional_line = '<br /> {text}'
    highlightList_start = '    <h3 class="highlights">{caption}:</h3>\n    <ul>'
    highlightList_end = '    </ul>'
    job_start = '  <div class="highlights data" id="{jobid}">'
    job_end = '  </div>'
    html_start ="""\
<!DOCTYPE html PUBLIC "-//W3C//DTD XHTML 1.0 Transitional//EN" "http://www.w3.org/TR/xhtml1/DTD/xhtml1-transitional.dtd">
<html xmlns="http://www.w3.org/1999/xhtml">
<head>
  <meta content="text/html; charset=utf-8" http-equiv="Content-Type" />
  <title>{DocTitle}</title>
  <link href="highlights.css" media="print,screen" rel="stylesheet" type="text/css" />
</head>
<body>
<div class="cv-page">
"""
    html_end ="""\
</div>
</body>
</html>
"""
    @staticmethod
    def make_link(link):
        return HighlightsHtml.link.format(url=link.url, title=link.title)

    @staticmethod
    def make_span(span):
        if span.link:
            return HighlightsHtml.make_link(span.link)
        else:
            return span.text()

    @staticmethod
    def make_line(line):
        return ''.join([HighlightsHtml.make_span(sub) for sub in line.children])

    @staticmethod
    def make_highlight(highlight):
        prefix = ' ' * (6 + highlight.level * 4)
        html_lines = [prefix + HighlightsHtml.highlight_start.format(text=HighlightsHtml.make_line(highlight.children[0]))]
        if len(highlight.children) == 1:
            html_lines[0] += HighlightsHtml.highlight_end
        else:
            sub_prefix = ' ' * (8 + highlight.level * 4)
            in_highlight_group = False
            for child in highlight.children[1:]:
                if child.otype == 'line':
                    if in_highlight_group:
                        html_lines.append(sub_prefix + '</ul>')
                        in_highlight_group = False
                    html_lines.append(sub_prefix + HighlightsHtml.highlight_additional_line.format(text=HighlightsHtml.make_line(child)))
                elif child.otype == 'highlight':
                    if not in_highlight_group:
                        html_lines.append(sub_prefix + '<ul>')
                        in_highlight_group = True
                    html_lines.append(HighlightsHtml.make_highlight(child))
            if in_highlight_group:
                html_lines.append(sub_prefix + '</ul>')
                in_highlight_group = False
            html_lines.append(prefix + HighlightsHtml.highlight_end)
        return '\n'.join(html_lines)

    @staticmethod
    def make_highlightlist(highlightlist):
        html_highlights = [HighlightsHtml.highlightList_start.format(caption=highlightlist.caption)]
        for highlight in highlightlist.highlights:
            html_highlights.append(HighlightsHtml.make_highlight(highlight))
        html_highlights.append(HighlightsHtml.highlightList_end)
        return '\n'.join(html_highlights)

    @staticmethod
    def make_job(job):
        html_job = [HighlightsHtml.job_start.format(jobid=job.jobid)]
        html_job.append(HighlightsHtml.make_highlightlist(job.highlights))
        html_job.append(HighlightsHtml.job_end)
        return '\n'.join(html_job)

    @staticmethod
    def make_cv_highlights(cv_highlights):
        return HighlightsHtml.html_start.format(DocTitle="Arizona Edwards' Employment Highlights") \
          + '\n\n'.join([HighlightsHtml.make_job(job) for job in cv_highlights.jobs]) \
          + HighlightsHtml.html_end
