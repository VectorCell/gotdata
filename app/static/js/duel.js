function createGraph(tag, data) {
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

	var margin = {top: 20, right: 20, bottom: 70, left: 40},
	    width = 600 - margin.left - margin.right,
	    height = 300 - margin.top - margin.bottom;

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
		.style("text-anchor", "end")
		.attr("dx", "-.8em")
		.attr("dy", "-.55em")
		.attr("transform", "rotate(-90)" );

	svg.append("g")
		.attr("class", "y axis")
		.call(yAxis)
	.append("text")
		.attr("transform", "rotate(-90)")
		.attr("y", 6)
		.attr("dy", ".71em")
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

	// createGraph("#chart-types", falseData);

	$.getJSON('/yu-gi-oh.json', function(data) {
		var dataTypesDict = {};
		var dataSubtypesDict = {};
		var dataFamiliesDict = {};

		$.each(data, function(index) {
    		// var type = data[index]["type"];
    		// if (type == "monster")
    		// 	dataTypes[0] += 1;
    		// else if (type == "spell")
    		// 	dataTypes[1] += 1;
    		// else if (type == "trap")
    		// 	dataTypes[2] += 1;
    		// else // unknown type
    		// 	dataTypes[3] += 1;

    		var type = data[index]["type"];
    		if (!(type in dataTypesDict))
    			dataTypesDict[type] = 0;
    		dataTypesDict[type] += 1;

    		var subtype = data[index]["subtype"];
    		if (!(subtype in dataSubtypesDict))
    			dataSubtypesDict[subtype] = 0;
    		dataSubtypesDict[subtype] += 1;

    		var family = data[index]["family"];
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

		createGraph("#chart-types", dataTypesDicts);
		createGraph("#chart-subtypes", dataSubtypesDicts);
		createGraph("#chart-families", dataFamiliesDicts);

		// var width = 420, barHeight = 20;

		// var x = d3.scale.linear()
		//     .domain([0, d3.max(dataTypes)])
		//     .range([0, width]);
		// var chart = d3.select("#chart-types")
		//     .attr("width", width)
		//     .attr("height", barHeight * dataTypes.length);
		// var bar = chart.selectAll("g")
		//     .data(dataTypes)
		//   .enter().append("g")
		//     .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });
		// bar.append("rect")
		//     .attr("width", x)
		//     .attr("height", barHeight - 1);
		// bar.append("text")
		//     .attr("x", function(d) { return x(d) - 3; })
		//     .attr("y", barHeight / 2)
		//     .attr("dy", ".35em")
		//     .text(function(d) { return d; });

		// x = d3.scale.linear()
		//     .domain([0, d3.max(dataSubtypes)])
		//     .range([0, width]);
		// chart = d3.select("#chart-subtypes")
		//     .attr("width", width)
		//     .attr("height", barHeight * dataSubtypes.length);
		// bar = chart.selectAll("g")
		//     .data(dataSubtypes)
		//   .enter().append("g")
		//     .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });
		// bar.append("rect")
		//     .attr("width", x)
		//     .attr("height", barHeight - 1);
		// bar.append("text")
		//     .attr("x", function(d) { return x(d) - 3; })
		//     .attr("y", barHeight / 2)
		//     .attr("dy", ".35em")
		//     .text(function(d) { return d; });

		// x = d3.scale.linear()
		//     .domain([0, d3.max(dataFamilies)])
		//     .range([0, width]);
		// chart = d3.select("#chart-families")
		//     .attr("width", width)
		//     .attr("height", barHeight * dataFamilies.length);
		// bar = chart.selectAll("g")
		//     .data(dataFamilies)
		//   .enter().append("g")
		//     .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });
		// bar.append("rect")
		//     .attr("width", x)
		//     .attr("height", barHeight - 1);
		// bar.append("text")
		//     .attr("x", function(d) { return x(d) - 3; })
		//     .attr("y", barHeight / 2)
		//     .attr("dy", ".35em")
		//     .text(function(d) { return d; });
	});
});