// buducocv.js - Arizona Edwards
// Created: 2016-10-19

var ch_blackstar = '★';
var ch_whitestar = '☆';
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
      redSpan.text('|' + Array(extrastars+1).join(ch_blackstar));
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
  if (urlSearchParams.has('nodetails')) { $('#details-page').hide(); }
  if (urlSearchParams.has('nosummary')) { $('#summary-page').hide(); }
  if (urlSearchParams.has('nodownload')) { $('#download').hide(); }
  if (urlSearchParams.has('nohighlights')) { $('.detail-highlights').hide(); } else { $('.detail-highlights').hide_if_empty(); }

  if (urlSearchParams.has('print')) {
    const params = new Proxy(urlSearchParams, { get: (searchParams, prop) => searchParams.get(prop), });
    if (params.print == "frontpage") {
      unloadCSS("buducocv-print.css");
      addPrintCSS("buducocv-print-frontpage.css");
      $('#summary-page').hide();
      $('#details-page').hide();
      $('.cv-between-pages').hide();
    } else if (params.print == "rowbreak") {
      unloadCSS("buducocv-print.css");
      addPrintCSS("buducocv-print-rowbreak.css");
    } else if (params.print == "nocss") {
      unloadCSS("buducocv-print.css");
    }
  }
}
