module.exports = function(string, bangs = string.length) {
    // The repeat function is new in ES6.
    return string + '!'.repeat(bangs);
};
