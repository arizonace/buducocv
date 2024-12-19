// buducocv.js - Arizona Edwards
// Created: 2016-10-19

var ch_blackstar = '★';
var ch_whitestar = '☆';
var no_break = '\u2060'
function star_rating(jqo)
{
  try
  {
    he = jqo.get(0);
    if (he.tagName !== "SPAN" || he.className != "starrating")
    {
      throw("Unexpected tag " + he.tagName + " of " + he.className);
    }

    var content = jqo.text();
    var rating = parseInt(content);

    var blackstars = rating > 5 ? 5 : rating;
    var whitestars = 5 - rating;
    var extrastars = rating > 5 ? rating - 5 : 0;
    var retval = Array(blackstars+1).join(ch_blackstar);
    if (whitestars > 0) { retval += Array(whitestars+1).join(ch_whitestar);}
    starCss = {"font-family": "PingFang SC", "font-size": "8px"};
    jqo.css(starCss);
    jqo.text(retval);
    if (extrastars > 0)
    {
      redSpan = $(he.parentElement.appendChild(document.createElement('SPAN')));
      redSpan.text('|' + no_break + Array(extrastars+1).join(ch_blackstar));
      starCss["color"] = "red";
      redSpan.css(starCss);
    }
  }
  catch (err)
  {
    console.log("star_rating error: " + err);
  }
};

function chartspan(jqo)
{
  jqo.sparkline('html', { type: 'line', chartRangeMin: 0, chartRangeMax: 11, width:'80px'});
};

$.fn.starrating = function () {
    return this.each(function () {
      star_rating($(this));
    });
}

$.fn.chartspan = function () {
    return this.each(function () {
      chartspan($(this));
    });
}

$.fn.hide_parent_if_empty = function () {
    return this.each(function () {
      if ($(this).text().trim() == "") { $(this).parent().hide(); }
    });
}

$.fn.hide_if_empty = function () {
  return this.each(function () {
    if ($(this).text().trim() == "") { $(this).hide(); }
  });
}

$.fn.show_if_not_empty = function () {
  return this.each(function () {
    if ($(this).text().trim() != "") { $(this).show(); }
  });
}

function addPrintCSS(filename) {
  const link = document.createElement("link");
  link.rel = "stylesheet";
  link.type = "text/css";
  link.href = filename;
  document.head.appendChild(link);
}

function unloadCSS(filename) {
  const linkElement = document.querySelector(`link[href="${filename}"]`);

  if (linkElement) {
    document.head.removeChild(linkElement);
  }
}
function toggleDetails() {
  if ($('#show-details').text() == "Hide Details") {
    $('#details-page').hide();
    $('#show-details').text("Show Details");
  } else {
    $('#details-page').show();
    $('#show-details').text("Hide Details");
  }
}

function toggleHighlights() {
  if ($('#show-highlights').text() == "Hide Highlights") {
    $('.detail-highlights').hide();
    $('#show-highlights').text("Show Highlights");
    } else {
    $('.detail-highlights').show_if_not_empty();
    $('#show-highlights').text("Hide Highlights");
  }
}

function front_page_load()
{
  $.fn.sparkline.defaults.common.disableHiddenCheck = true;
  $.fn.sparkline.defaults.common.disableInteraction = true;
  $('.spanchart').chartspan();
  $('.starrating').starrating();
  $('.no-javascript').hide();
  $('.detail-field-label').css({"font-weight": "bold"});
  $('.detail-field-value').hide_parent_if_empty();

  const urlSearchParams = new URLSearchParams(window.location.search);
  let showSummary = !urlSearchParams.has('nosummary');
  let showHighlights = showSummary && urlSearchParams.has('highlights');
  let showDetails = showSummary && (showHighlights || urlSearchParams.has('details'));

  if (!showSummary) {
    $('#summary-page').hide();
  } else {
    if (showDetails) { $('#details-page').show(); $('#show-details').text("Hide Details"); }
    if (showHighlights) { $('.detail-highlights').show_if_not_empty(); $('#show-highlights').text("Hide Highlights"); }
  }
  if (urlSearchParams.has('nodownload')) { $('#download').hide(); }
  if (urlSearchParams.has('nolegend')) { $('.star-legend').hide(); }

  if (urlSearchParams.has('print')) {
    const params = new Proxy(urlSearchParams, { get: (searchParams, prop) => searchParams.get(prop), });
    if (params.print == "frontpage") {
      unloadCSS("buducocv-print-avoidtablebreak.css");
      unloadCSS("buducocv-print-avoidrowbreak.css");
      addPrintCSS("buducocv-print-frontpage.css");
    } else if (params.print == "rowbreak") {
      unloadCSS("buducocv-print-avoidtablebreak.css");
    } else if (params.print == "nocss") {
      unloadCSS("buducocv-print-avoidtablebreak.css");
      unloadCSS("buducocv-print-avoidrowbreak.css");
    }
  }

  $('#printed-date').text(new Date().toISOString().split('T')[0]);
}
