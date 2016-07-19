function createGraph(tag, data, graphWidth) {
	function getKeys(object) {
		var list = [];
		for (key in object)
			list.push(key);
		return list;
	}
	function getValues(object) {
		var list = [];
		for (key in object)
			list.push(object[key]);
		return list;
	}

	var dataKeys = getKeys(data);
	var dataValues = getValues(data);

	var margin = {top: 20, right: 20, bottom: 100, left: 60},
	    width = graphWidth - margin.left - margin.right,
	    height = 400 - margin.top - margin.bottom;

	var x = d3.scale.ordinal()
		.domain(dataKeys)
		.rangeRoundBands([0, width], .05);
	var y = d3.scale.linear()
		.domain([0, d3.max(dataValues)])
		.range([height, 0]);

	var xAxis = d3.svg.axis()
	    .scale(x)
	    .orient("bottom");
	var yAxis = d3.svg.axis()
	    .scale(y)
	    .orient("left")
	    .ticks(10);

	var svg = d3.select(tag)
	    .attr("width", width + margin.left + margin.right)
	    .attr("height", height + margin.top + margin.bottom)
	  .append("g")
	    .attr("transform", 
	          "translate(" + margin.left + "," + margin.top + ")");


	svg.append("g")
		.attr("class", "x axis")
		.attr("transform", "translate(0," + height + ")")
		.call(xAxis)
	.selectAll("text")
		.attr("transform", "rotate(-90)" )
		.attr("dx", "-.8em")
		.attr("dy", "-.55em")
		.style("text-anchor", "end");

	svg.append("g")
		.attr("class", "y axis")
		.call(yAxis)
	.append("text")
		.attr("transform", "rotate(-90)")
		.attr("x", "-2")
		.attr("y", "-32")
		.style("text-anchor", "end")
		.text("# of Cards");

	svg.selectAll("bar")
		.data(dataKeys)
	.enter().append("rect")
		.attr("class", "bar")
		.attr("x", function(d) { return x(d); })
		.attr("width", x.rangeBand())
		.attr("y", function(d) { return y(data[d]); })
		.attr("height", function(d) { return height - y(data[d]); });
}

$(document).ready(function() {
	// var falseData = {
	// 	"monster": 45,
	// 	"spell": 12,
	// 	"trap": 62
	// };
	// createGraph("#chart-types", falseData, 1000);
	// return;

	$.getJSON('/yu-gi-oh.json', function(data) {
		var dataTypesDict = {};
		var dataSubtypesDict = {};
		var dataFamiliesDict = {};

		$.each(data, function(index) {
			var type = data[index]["type"];
    		if (!(type in dataTypesDict))
    			dataTypesDict[type] = 0;
    		dataTypesDict[type] += 1;

    		var subtype = data[index]["subtype"];
    		if (!(subtype in dataSubtypesDict))
    			dataSubtypesDict[subtype] = 0;
    		dataSubtypesDict[subtype] += 1;

    		var family = data[index]["family"];
    		if (family == "") family = "none";
    		if (!(family in dataFamiliesDict))
    			dataFamiliesDict[family] = 0;
    		dataFamiliesDict[family] += 1;
		});

		var getValues = function(object) {
			var list = [];
			for (key in object) {
				list.push(object[key]);
			}
			return list;
		}

		var dataTypes = getValues(dataTypesDict);
		var dataSubtypes = getValues(dataSubtypesDict);
		var dataFamilies = getValues(dataFamiliesDict);

		createGraph("#chart-types", dataTypesDict, 600);
		createGraph("#chart-subtypes", dataSubtypesDict, 1400);
		createGraph("#chart-families", dataFamiliesDict, 800);
	});
});