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
  })
;

/*
 * testing with google safe browsing API
 */
function testSafeChuncks(num, url) {
  var options = {
    method: 'POST',
    url: 'https://safebrowsing.googleapis.com/v4/threatMatches:find',
    qs: {key: 'AIzaSyD8xw-x2GdSI4EfPwnEnCr0X87AZQA81XI'},
    headers: {'content-type': 'application/json'},
    body: {
      client: {clientId: 'polymtl', clientVersion: '1.0.0'},
      threatInfo: {
        threatEntryTypes: ['URL'],
        threatEntries: [{url: url}]
      }
    },
    json: true
  };

  request(options, function (error, response, body) {
    var curr = num;
    if (error) {
      console.log(curr);
      throw new Error(error);
    }
    if (body) console.log(body);
  });
}

