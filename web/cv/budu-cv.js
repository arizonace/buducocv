
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
		
		scale_11_7 = [0, 1, 1, 2, 2, 3, 4, 5, 6, 6, 6, 7];
		rating = scale_11_7[rating];

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

function front_page_load()
{
	$.fn.sparkline.defaults.common.disableHiddenCheck = true;
	$.fn.sparkline.defaults.common.disableInteraction = true;
	$('.spanchart').chartspan();
	$('.starrating').starrating();
}
