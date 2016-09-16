<!DOCTYPE html>
<html>
  <head>
    <!-- EXTERNAL LIBS-->
    <script src="https://ajax.googleapis.com/ajax/libs/jquery/1.11.1/jquery.min.js"></script>
    <script src="https://www.google.com/jsapi"></script>

    <!-- EXAMPLE SCRIPT -->
    <script>

      // onload callback
      function drawChart() {

        var public_key = 'dZ4EVmE8yGCRGx5XRX1W';

        // JSONP request
        var jsonData = $.ajax({
          url: 'https://data.sparkfun.com/output/' + public_key + '.json',
          data: {page: 1},
          dataType: 'jsonp',
        }).done(function (results) {

          var data = new google.visualization.DataTable();

          data.addColumn('datetime', 'Time');
          data.addColumn('number', 'Temp');
          data.addColumn('number', 'Wind Speed MPH');

          $.each(results, function (i, row) {
            data.addRow([
              (new Date(row.timestamp)),
              parseFloat(row.tempf),
              parseFloat(row.windspeedmph)
            ]);
          });

          var chart = new google.visualization.LineChart($('#chart').get(0));

          chart.draw(data, {
            title: 'Wimp Weather Station'
          });

        });

      }

      // load chart lib
      google.load('visualization', '1', {
        packages: ['corechart']
      });

      // call drawChart once google charts is loaded
      google.setOnLoadCallback(drawChart);

    </script>

  </head>
  <body>
    <div id="chart" style="width: 100%;"></div>
  </body>
</html>