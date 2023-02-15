//[Dashboard Javascript]

//Project:	CRMi - Responsive Admin Template
//Primary use:   Used only for the main dashboard (index.html)


$(function () {

  'use strict';
	
		var options = {
          series: [{
          name: 'Fees',
          type: 'column',
          data: [440, 505, 414, 671, 227, 413, 201, 352, 752, 320, 257, 160]
        }, {
          name: 'Donaion',
          type: 'line',
          data: [23, 42, 35, 27, 43, 22, 17, 31, 22, 22, 12, 16]
        }],
          chart: {
          height: 338,
          type: 'line',
		  toolbar: {
			show: false,
		  },
        },
        stroke: {
          width: [0, 2]
        },
		 plotOptions: {
		  bar: {
			  columnWidth: '50%',
		  },
		 },
		colors:['#3596f7', '#ffa800'],
        dataLabels: {
          enabled: false,
        },
		 legend: {
		  position: 'top',
		  horizontalAlign: 'center',
		 },
        labels: ['01 Jan 2001', '02 Jan 2001', '03 Jan 2001', '04 Jan 2001', '05 Jan 2001', '06 Jan 2001', '07 Jan 2001', '08 Jan 2001', '09 Jan 2001', '10 Jan 2001', '11 Jan 2001', '12 Jan 2001'],
        xaxis: {
          type: 'datetime'
        },
        yaxis: [{
          title: {
            text: 'Fees',
          },
        
        }, {
          opposite: true,
          title: {
            text: 'Donaion'
          }
        }]
        };

        var chart = new ApexCharts(document.querySelector("#chart-report"), options);
        chart.render();
	
	
	
		$('.event-bx').slimScroll({
			height: '300px'
		});
	
		$('.complaint-bx').slimScroll({
			height: '300px'
		});
	
}); // End of use strict
