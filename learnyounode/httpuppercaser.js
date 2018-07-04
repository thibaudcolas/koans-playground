var http = require('http');
var map = require('through2-map');

var port = Number(process.argv[2]) || 80;

var server = http.createServer(function (req, res) {
  if (req.method === 'POST') {
    req.pipe(map(function (chunk) {
      return chunk.toString().toUpperCase();
    })).pipe(res);
  }
})

server.listen(port);
