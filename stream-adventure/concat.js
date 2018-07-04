var concat = require('concat-stream');

process.stdin.pipe(concat(function (body) {
  var reversed = body ? body.toString().split('').reverse().join('') : '';
  process.stdout.write(reversed);
}));
