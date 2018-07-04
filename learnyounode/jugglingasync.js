var http = require('http');
var bl = require('bl');

var urls = process.argv.slice(2);

var juggleAsync = function (id, data) {
  this.content = this.content || [];
  this.content[id] = data;

  if (this.content[0] && this.content[1] && this.content[2]) {
      this.content.forEach(function (o) {
        console.log(o);
      });
  }
}

urls.forEach(function (url, id) {
  http.get(url, function (response) {
    response.pipe(bl(function (err, data) {
      if (err)
        return console.error(err);

      juggleAsync(id, data.toString());
    }));
  });
});
