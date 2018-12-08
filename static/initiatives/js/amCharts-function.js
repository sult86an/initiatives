
<!-- Chart code -->

var chart = AmCharts.makeChart( "chartdiv", {
"type": "serial",
"theme": "light",
"dataProvider": [ {
"country": "عمرو العقاد",
"visits": 25
}, {
"country": "موسى الرفاعي",
"visits": 22
}, {
"country": "محمد العسيري",
"visits": 22
}, {
"country": "خالد الذبياني",
"visits": 84
}, {
"country": "عبدالله العليان",
"visits": 5
}, {
"country": "محمد الشريف",
"visits": 79
}, {
"country": "عادل حماص",
"visits": 5
}, {
"country": "زياد ديولي",
"visits": 30
}, {
"country": "محمد العلوي",
"visits": 85
}, {
"country": "محمد الشريف",
"visits": 63
}],
"valueAxes": [ {
"gridColor": "#fff",
"gridAlpha": 0.2,
"dashLength": 0
} ],
"gridAboveGraphs": true,
"startDuration": 2,
"graphs": [ {
"balloonText": "[[category]]: <b>[[value]]</b>",
"fillAlphas": 0.8,
"lineAlpha": 0.2,
"type": "column",
"valueField": "visits"
} ],
"chartCursor": {
"categoryBalloonEnabled": false,
"cursorAlpha": 0,
"zoomable": false
},
"categoryField": "country",
"categoryAxis": {
"gridPosition": "start",
"gridAlpha": 0,
"tickPosition": "start",
"tickLength": 20
},
"export": {
"enabled": false
}

} );
