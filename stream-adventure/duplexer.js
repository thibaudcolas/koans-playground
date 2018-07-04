var spawn = require('child_process').spawn;
var duplexer = require('duplexer');

module.exports = function (cmd, args) {
  var process = spawn(cmd, args);

  return duplexer(process.stdin, process.stdout);
};
