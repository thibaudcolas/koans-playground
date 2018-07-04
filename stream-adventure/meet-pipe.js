var fs = require('fs');

var path = process.argv[2];

fs.createReadStream(path).pipe(process.stdout);
