var fls = require('./filteredlsmodule');

var path = process.argv[2];
var extension = process.argv[3];

fls(path, extension, function (err, files) {
  if (err) {
    return console.log("Error: " + err);
  }
  else {
    files.forEach(function (file) { console.log(file) });
  }
});
