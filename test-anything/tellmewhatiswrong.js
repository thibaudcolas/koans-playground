var assert = require('assert');

var modulePath = process.argv[2];

var isCoolNumber = require(modulePath);

assert.equal(isCoolNumber(42), true, '42 is a cool number');
