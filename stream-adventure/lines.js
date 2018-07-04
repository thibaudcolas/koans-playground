var through = require('through');
var split = require('split');

var alternateCase = function(str) {
  var out = this.isOdd ? str.toUpperCase() : str.toLowerCase();
  this.isOdd = !this.isOdd;
  return out;
};
alternateCase.isOdd = true;

function write(buf) {
  this.queue(alternateCase(buf.toString() + '\n'));
}

function end() {
  this.queue(null);
}

var tr = through(write, end);
process.stdin
  .pipe(split())
  .pipe(tr)
  .pipe(process.stdout);
