$(function () {
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
                            return (this.value > 0 ? ' + ' : '') + this.value + '%';
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

        $.getJSON( 'http://localhost:8000/static/js/'+ name+ '.json',    function (data) {

            seriesOptions[i] = {
                name: name,
                data: data,
                yAxis: i
            };

            // As we're loading the data asynchronously, we don't know what order it will arrive. So
            // we keep a counter and create the chart when all the data is loaded.
            seriesCounter += 1;

            if (seriesCounter === names.length) {
                createChart();
            }
        });
    });
});