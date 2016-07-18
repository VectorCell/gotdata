$(document).ready(function() {
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


		var width = 420, barHeight = 20;

		var x = d3.scale.linear()
		    .domain([0, d3.max(dataTypes)])
		    .range([0, width]);
		var chart = d3.select("#chart-types")
		    .attr("width", width)
		    .attr("height", barHeight * dataTypes.length);
		var bar = chart.selectAll("g")
		    .data(dataTypes)
		  .enter().append("g")
		    .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });
		bar.append("rect")
		    .attr("width", x)
		    .attr("height", barHeight - 1);
		bar.append("text")
		    .attr("x", function(d) { return x(d) - 3; })
		    .attr("y", barHeight / 2)
		    .attr("dy", ".35em")
		    .text(function(d) { return d; });

		x = d3.scale.linear()
		    .domain([0, d3.max(dataSubtypes)])
		    .range([0, width]);
		chart = d3.select("#chart-subtypes")
		    .attr("width", width)
		    .attr("height", barHeight * dataSubtypes.length);
		bar = chart.selectAll("g")
		    .data(dataSubtypes)
		  .enter().append("g")
		    .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });
		bar.append("rect")
		    .attr("width", x)
		    .attr("height", barHeight - 1);
		bar.append("text")
		    .attr("x", function(d) { return x(d) - 3; })
		    .attr("y", barHeight / 2)
		    .attr("dy", ".35em")
		    .text(function(d) { return d; });

		x = d3.scale.linear()
		    .domain([0, d3.max(dataFamilies)])
		    .range([0, width]);
		chart = d3.select("#chart-families")
		    .attr("width", width)
		    .attr("height", barHeight * dataFamilies.length);
		bar = chart.selectAll("g")
		    .data(dataFamilies)
		  .enter().append("g")
		    .attr("transform", function(d, i) { return "translate(0," + i * barHeight + ")"; });
		bar.append("rect")
		    .attr("width", x)
		    .attr("height", barHeight - 1);
		bar.append("text")
		    .attr("x", function(d) { return x(d) - 3; })
		    .attr("y", barHeight / 2)
		    .attr("dy", ".35em")
		    .text(function(d) { return d; });
	});
});

// (function(d3) {
// 'use strict';

// var dataset = [
//   { label: 'Abulia', count: 10 }, 
//   { label: 'Betelgeuse', count: 20 },
//   { label: 'Cantaloupe', count: 30 },
//   { label: 'Dijkstra', count: 40 }
// ];

// var width = 360;
// var height = 360;
// var radius = Math.min(width, height) / 2;

// var color = d3.scale.category20b();

// var svg = d3.select('#chart-types')
//   .append('svg')
//   .attr('width', width)
//   .attr('height', height)
//   .append('g')
//   .attr('transform', 'translate(' + (width / 2) + 
//     ',' + (height / 2) + ')');

// var arc = d3.svg.arc()
//   .outerRadius(radius);

// var pie = d3.layout.pie()
//   .value(function(d) { return d.count; })
//   .sort(null);

// var path = svg.selectAll('path')
//   .data(pie(dataset))
//   .enter()
//   .append('path')
//   .attr('d', arc)
//   .attr('fill', function(d, i) { 
//     return color(d.data.label);
//   });

// })(window.d3);