var test = require('tape');

var fancifyPath = process.argv[2];
var fancify = require(fancifyPath);

test('fancify wraps fanciness around thing', function (t) {
    t.equal(fancify('Hello'), '~*~Hello~*~', 'Hello should be fancy');
    t.equal(fancify('Hello', true), '~*~HELLO~*~', 'Hello should be fancy and upercase');
    t.equal(fancify('Hello', true, '!'), '~!~HELLO~!~', 'Hello should be fancy, uppercase and bangy');

    t.end();
})
