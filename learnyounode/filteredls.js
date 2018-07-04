var fs = require('fs');

var path = process.argv[2];
var extension = process.argv[3];

fs.readdir(path, function (err, list) {
  if (err) {
    console.error(err);
  }
  else {
    list.forEach(function (item) {
      if (item.split('.').pop() === extension) {
        console.log(item);
      }
    });
  }
});
