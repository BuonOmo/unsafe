var request = require('request');
var unzip = require('unzip');
var csv2 = require('csv2');
var fs = require('fs');

var writer = fs.createWriteStream('./list');
/*
 * Retrieve data from alexa
 */
request.get('http://s3.amazonaws.com/alexa-static/top-1m.csv.zip')
  .pipe(unzip.Parse())
  .on('entry', function (entry) {
    entry.pipe(csv2()).on('data', list => writer.write(list[1] + "\n"));
  });