var fs = require('fs');

var path = process.argv[2];
var content = fs.readFileSync(path).toString().split('\n');

var nbLines = content.length - 1;

console.log(nbLines);
