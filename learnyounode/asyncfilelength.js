var fs = require('fs');

var path = process.argv[2];

fs.readFile(path, 'utf8', function (err, content) {
  if (err) {
    console.error(err);
  }
  else {
    var nbLines = content.split('\n').length - 1;
    console.log(nbLines);
  }
});
