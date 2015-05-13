$(function(){
	$('#sendyahoo').click(function(){
		$("#worldbank_show").hide();
		$("#stock_show").show();

		var stock_symbol = document.getElementById("selectStock").value;
		var start_date = document.getElementById("startDate").value;
		var end_date = document.getElementById("endDate").value;

		var stockform1 = function(){
			$.ajax({
	    		type: "GET",
				url: 'http://localhost:8000/getstockform?callback=?',
				data: {startDate:start_date,endDate:end_date,symbol:stock_symbol},
				dataType: 'json',
				traditional: true,
				success: function(json){

					if($("#form1").length>0){
						$("#form1").remove();
					}
					var fomr1 = $("<div class=\"portlet-body\" id=\"form1\">").appendTo($("#portform1"));
					
					var table = $("<table class=\"table table-striped table-bordered table-hover table-full-width\" id=\"sample_2\">").appendTo(form1);
					
					var thead = $("<thead>").appendTo(table);

					var tr = $("<tr>").appendTo(thead);
					
					$("<th>Symbol</th>").appendTo(tr);

					$("<th>Exchange Symbol</th>").appendTo(tr);

					$("<th class=\"hidden-480\">Date</th>").appendTo(tr);

					$("<th class=\"hidden-480\">Open Price</th>").appendTo(tr);

					$("<th class=\"hidden-480\">High Price</th>").appendTo(tr);

					$("<th class=\"hidden-480\">Low Price</th>").appendTo(tr);

					$("<th class=\"hidden-480\">Close Price</th>").appendTo(tr);

					$("<th class=\"hidden-480\">Volume</th>").appendTo(tr);

					$("<th class=\"hidden-480\">Adj Close</th>").appendTo(tr);

					$("</tr>").appendTo(table);								

					$("</thead>").appendTo(thead);

					var tbody = $("<tbody>").appendTo(table);	

					for(var i=0;i<json.length;i++){
						var tr = $("<tr>").appendTo(tbody);
						for(var j=0;j<9;j++){
							var html = "<td class=\"hidden-480\">"+json[i][j]+"</td>";
							$(html).appendTo(tr);
						}
						$("</tr>").appendTo(tbody);
					}
					
					$("</tbody>").appendTo(table);
					$("</table>").appendTo(form1);
					$("</div>").appendTo($("#portform1"));

					TableAdvanced.init();
				}
			});
		};

		var stockform2 = function(){
			$.ajax({
	    		type: "GET",
				url: 'http://localhost:8000/getsentimentform?callback=?',
				data: {startDate:start_date,endDate:end_date,symbol:stock_symbol},
				dataType: 'json',
				traditional: true,
				success: function(json){
					if($("#form2").length>0){
						$("#form2").remove();
					}
					var fomr2 = $("<div class=\"portlet-body\" id=\"form2\">").appendTo($("#portform2"));
					
					var table = $("<table class=\"table table-striped table-bordered table-hover table-full-width\" id=\"sample_2\">").appendTo(form2);
					
					var thead = $("<thead>").appendTo(table);

					var tr = $("<tr>").appendTo(thead);
					
					$("<th>Symbol</th>").appendTo(tr);

					$("<th class=\"hidden-480\">Date</th>").appendTo(tr);

					$("<th class=\"hidden-480\">Daily Sentiment</th>").appendTo(tr);

					$("</tr>").appendTo(table);								

					$("</thead>").appendTo(thead);

					var tbody = $("<tbody>").appendTo(table);	

					for(var i=0;i<json.length;i++){
						var tr = $("<tr>").appendTo(tbody);
						var html = "<td class=\"hidden-480\">"+stock_symbol+"</td>";
						$(html).appendTo(tr);
						for(var j=0;j<2;j++){
							var html = "<td class=\"hidden-480\">"+json[i][j]+"</td>";
							$(html).appendTo(tr);
						}
						$("</tr>").appendTo(tbody);
					}
					
					$("</tbody>").appendTo(table);
					$("</table>").appendTo(form2);
					$("</div>").appendTo($("#portform2"));

				}
			});
		};

		var stockchart1 = function(){
			var seriesOptions = [],
		        seriesCounter = 0,
		        names = ['sentiment','stock'],
		        //names = ['sentiment'],
		        // create the chart when all data is loaded
		        createChart = function () {

		            $('#container1').highcharts('StockChart', {

		                rangeSelector: {
		                    inputEnabled: false,
		                    selected: 4
		                },

		                yAxis: [{
		                    title: {
		                        text: 'Daily Sentiment',
		                        style: {
		                            color: '#7cb5ec',
		                            fontWeight: 'bold'
		                        }
		                    },
		                    labels: {
		                        formatter: function () {
		                            return (this.value > 0 ? ' + ' : '') + this.value + '%';
		                        }
		                    },
		                    opposite: true,
		                    plotLines: [{
		                        value: 0,
		                        width: 2,
		                        color: 'silver'
		                    }]
		                },{
		                    title: {
		                        text: 'Daily Stock Price',
		                        style: {
		                            color: '#434348',
		                            fontWeight: 'bold'
		                        }
		                    },
		                    labels: {
		                        formatter: function () {
		                            return (this.value > 0 ? ' + ' : '') + this.value;
		                        }
		                    },
		                    opposite: false,
		                    plotLines: [{
		                        value: 0,
		                        width: 2,
		                        color: 'silver'
		                    }]
		                }],

		                legend: {
		                    enabled: true
		                },

		                plotOptions: {
		                    series: {
		                        compare: 'percentage'
		                    }
		                },

		                tooltip: {
		                    pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> <br/>',
		                    valueDecimals: 2
		                },

		                series: seriesOptions
		            });
		        };

		    $.each(names, function (i, name) {

		    	$.ajax({
		    		type: "GET",
					url: 'http://localhost:8000/getstockprice?callback=?',
					data: {startDate:start_date,endDate:end_date,symbol:stock_symbol},
					dataType: 'json',
					traditional: true,
					success: function(json){
						seriesOptions[i] = {
			                name: name,
			                data: json[i],
			                yAxis: i
			            };
			            seriesCounter += 1;

		            	if (seriesCounter === names.length) {
		                	createChart();
		            	}
					}
		    	});
		    });
		};

		var stockchart2 = function(){
			var seriesOptions = [],
		        seriesCounter = 0,
		        names = ['sentiment','daily'],
		        // create the chart when all data is loaded
		        createChart = function () {

		            $('#container2').highcharts('StockChart', {

		                rangeSelector: {
		                    inputEnabled: false,
		                    selected: 4
		                },

		                yAxis: [{
		                    title: {
		                        text: 'Daily Sentiment',
		                        style: {
		                            color: '#7cb5ec',
		                            fontWeight: 'bold'
		                        }
		                    },
		                    labels: {
		                        formatter: function () {
		                            return (this.value > 0 ? ' + ' : '') + this.value + '%';
		                        }
		                    },
		                    opposite: true,
		                    plotLines: [{
		                        value: 0,
		                        width: 2,
		                        color: 'silver'
		                    }]
		                },{
		                    title: {
		                        text: 'Daily Stock Return',
		                        style: {
		                            color: '#434348',
		                            fontWeight: 'bold'
		                        }
		                    },
		                    labels: {
		                        formatter: function () {
		                            return (this.value > 0 ? ' + ' : '') + this.value+ '%';
		                        }
		                    },
		                    opposite: false,
		                    plotLines: [{
		                        value: 0,
		                        width: 2,
		                        color: 'silver'
		                    }]
		                }],

		                legend: {
		                    enabled: true
		                },

		                plotOptions: {
		                    series: {
		                        compare: 'value'
		                    }
		                },

		                tooltip: {
		                    pointFormat: '<span style="color:{series.color}">{series.name}</span>: <b>{point.y}</b> <br/>',
		                    valueDecimals: 2
		                },

		                series: seriesOptions
		            });
		        };

		    $.each(names, function (i, name) {

		    	$.ajax({
		    		type: "GET",
					url: 'http://localhost:8000/getsentiment?callback=?',
					data: {startDate:start_date,endDate:end_date,symbol:stock_symbol},
					dataType: 'json',
					traditional: true,
					success: function(json){
						seriesOptions[i] = {
			                name: name,
			                data: json[i],
			                yAxis: i
			            };
			            seriesCounter += 1;

		            	if (seriesCounter === names.length) {
		                	createChart();
		            	}
					}
		    	});
		    });
		};
		stockform1();
		stockform2();
		stockchart1();
		stockchart2();
		
	});

})