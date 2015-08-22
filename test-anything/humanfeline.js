var test = require('tape');

var feedCatPath = process.argv[2];
var feedCat = require(feedCatPath);

test('feedCat feeds cats', function (t) {
    t.equal(feedCat('SUSHI'), 'yum', '~~YUM~~');
    t.equal(feedCat('SL hot lunch'), 'yum', '~~YUM~~');
    t.equal(feedCat('spaghetti code'), 'yum', '~~YUM~~');

    t.throws(function () {
        feedCat('chocolate')
    }, 'NOT YUM');

    t.end();
})
