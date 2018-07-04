var fs = require('fs');
var path = require ('path');

module.exports = function (dir, extension, callback) {
  if (typeof dir === 'undefined' || typeof extension === 'undefined')
    return callback('dir path and extension are necessary');

  fs.readdir(dir, function (err, list) {
    if (err)
      return callback(err);

    list = list.filter(function (file) {
      return path.extname(file) === '.' + extension;
    });

    callback(null, list);
  });
};
