function duckCount() {
    var count = 0;

    for (var i = 0; i < arguments.length; i++) {
        if (Object.prototype.hasOwnProperty.call(arguments[i], 'quack')) {
            count++;
        }
    }

    return count;
}

module.exports = duckCount;
