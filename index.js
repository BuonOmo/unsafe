var request = require('request');

var fs = require('fs');
var writer = fs.createWriteStream('./threats.csv');
writer.write('url;threatType;platformType;threatEntryType\n');

var alexaList = fs.readFileSync('./list', 'utf-8').split('\n');
alexaList.pop(); // remove the last unwanted empty line
var chunkSize = 500;


nextChunk(0);

/*
 * testing with google safe browsing API
 */
function nextChunk(idx) {
  console.log(idx+ ' urls checked ('+((idx*100)/alexaList.length)+'%)' );
  if (idx + chunkSize < alexaList.length) {
    var options = {
      method: 'POST',
      url: 'https://safebrowsing.googleapis.com/v4/threatMatches:find',
      qs: {key: 'AIzaSyD8xw-x2GdSI4EfPwnEnCr0X87AZQA81XI'},
      headers: {'content-type': 'application/json'},
      body: {
        client: {clientId: 'polymtl', clientVersion: '1.0.0'},
        threatInfo: {
          threatTypes: ["THREAT_TYPE_UNSPECIFIED", "MALWARE", "SOCIAL_ENGINEERING", "UNWANTED_SOFTWARE",
            "POTENTIALLY_HARMFUL_APPLICATION"],
          platformTypes: ["ANY_PLATFORM"],
          threatEntryTypes: ["THREAT_ENTRY_TYPE_UNSPECIFIED", "URL", "EXECUTABLE", "IP_RANGE"],
          threatEntries: alexaList.slice(idx, idx + chunkSize).map(url => {
            return {"url": url}
          })
        }
      },
      json: true
    };
    request(options, function (error, response, body) {
      if (error) {
        throw new Error(error);
      }
      var sc;
      if (sc = body["matches"]) {
        for (match of sc) {
          writer.write(match['threat']['url']+';'+match['threatType']+';'+match['platformType']+';'+match['threatEntryType']+'\n');
        }
      }
      nextChunk(idx + chunkSize)
    });
  }
}

