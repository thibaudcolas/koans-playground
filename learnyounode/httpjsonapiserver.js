var http = require('http');
var url = require('url');

var port = Number(process.argv[2]) || 80;

var server = http.createServer(function (req, res) {
  if (req.method !== 'GET')
    return res.end('Give me some GET !');

  var request = url.parse(req.url, true);
  var response = {};
  var date = new Date(request.query.iso);

  if (request.pathname === '/api/parsetime') {

    response.hour = date.getHours();
    response.minute = date.getMinutes();
    response.second = date.getSeconds();
  }
  else if (request.pathname === '/api/unixtime') {
    response.unixtime = date.getTime();
  }

  res.writeHead(200, {'Content-Type': 'application/json'});

  res.end(JSON.stringify(response));
});

server.listen(port);
