var test = require('tape');

var repeatPath = process.argv[2];
var repeatCallback = require(repeatPath);

test('repeats the right number of times', function(t) {
    t.plan(11);

    repeatCallback(1, function() {
        t.pass('callback called')
    });

    repeatCallback(10, function() {
        t.pass('callback called')
    });
})
