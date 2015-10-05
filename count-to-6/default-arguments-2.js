module.exports = function(string, bangs = string.length) {
    return string + '!'.repeat(bangs);
};
