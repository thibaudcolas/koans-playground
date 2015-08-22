var emotifyPath = process.argv[2];
var testString = process.argv[3];

var emotify = require(emotifyPath);

console.log(emotify(testString));
