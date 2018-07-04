var http = require('http');
var net = require('net');

var port = process.argv[2];

var formatDate = function () {
  var date = new Date();
  date.setHours(date.getHours() + 1);
  return date.toISOString().replace('T', ' ').slice(0, 16);
}

var server = net.createServer(function (socket) {
  socket.end(formatDate());
})

server.listen(port);
