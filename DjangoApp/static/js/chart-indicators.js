$(function(){
	$('#sendWorldbank').click(function(event){
		event.preventDefault();
		$("#worldbank_show").show();
		var indicator = $('#selectIndicator').val()
		var country = $('#selectCountry').val()

		$.ajax({
			type: "GET",
			url: 'http://localhost:8000/getindicator?callback=?',
			data: {country:country,indicator:indicator},
			dataType: 'json',
			traditional: true,
			success: function(json){
				var series = [];
				for(var i=0;i<json.length-2;i++){
					var content = {};
					content["name"] = json[0][i];
					content["data"] = json[i+1];
					series.push(content);
				}
				var chartTitle = json[json.length-1];
				$('#container3').highcharts({
			        chart: {
			            type: 'column',
			            zoomType: 'x'
			        },
			        title: {
			            text: 'Indicators of '+chartTitle
			        },
			        subtitle: {
			            text: 'Source: World Bank'
			        },
			        xAxis: {
			            minRange: 5,
			            categories: [
			                '1960',
			                '1961',
			                '1962',
			                '1963',
			                '1964',
			                '1965',
			                '1966',
			                '1967',
			                '1968',
			                '1969',
			                '1970',
			                '1971',
			                '1972',
			                '1973',
			                '1974',
			                '1975',
			                '1976',
			                '1977',
			                '1978',
			                '1979',
			                '1980',
			                '1981',
			                '1982',
			                '1983',
			                '1984',
			                '1985',
			                '1986',
			                '1987',
			                '1988',
			                '1989',
			                '1990',
			                '1991',
			                '1992',
			                '1993',
			                '1994',
			                '1995',
			                '1996',
			                '1997',
			                '1998',
			                '1999',
			                '2000',
			                '2001',
			                '2002',
			                '2003',
			                '2004',
			                '2005',
			                '2006',
			                '2007',
			                '2008',
			                '2009',
			                '2010',
			                '2011',
			                '2012',
			                '2013'
			            ]
			        },
			        yAxis: {
			            min: 0,
			            title: {
			                text: 'Indicator Value'
			            }
			        },
			        rangeSelector: {
			            selected: 1
			        },
			        tooltip: {
			            headerFormat: '<span style="font-size:10px">{point.key}</span><table>',
			            pointFormat: '<tr><td style="color:{series.color};padding:0;font-size:5px">{series.name}: </td>' +
			                '<td style="padding:0"><b>{point.y:.1f}</b></td></tr>',
			            footerFormat: '</table>',
			            shared: true,
			            useHTML: true
			        },
			        plotOptions: {
			            column: {
			                pointPadding: 0.2,
			                borderWidth: 0
			            }
			        },
			        series: series
			    });
          	}
		});


	});
})