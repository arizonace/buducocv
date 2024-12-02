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

function bulletrating(jqo)
{
  var content = jqo.text();
  var rating = parseInt(content);
  jqo.sparkline([rating,rating,9], {type: 'bullet', width:'60px'});
};


function bulletrating(jqo)
{
  var content = jqo.text();
  var rating = parseInt(content);
  jqo.sparkline([rating,rating,9], {type: 'bullet', width:'60px'});
};


function chartspan(jqo)
{
  jqo.sparkline('html', { type: 'line', chartRangeMin: -1, chartRangeMax: 12, width:'80px'});
};

function chartspan2(jqo)
{
  jqo.sparkline('html', { type: 'line', lineColor: 'red', fillColor: false, chartRangeMin: 0, chartRangeMax: 100, width:'320px', height:'40px'});
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

$.fn.chartspan2 = function () {
  return this.each(function () {
    chartspan2($(this));
  });
}


function front_page_load()
{
  $.fn.sparkline.defaults.common.disableHiddenCheck = true;
  $.fn.sparkline.defaults.common.disableInteraction = true;
  $('.spanchart').chartspan();
  $('.spanchart2').chartspan2();
  $('.starrating').starrating();
}
