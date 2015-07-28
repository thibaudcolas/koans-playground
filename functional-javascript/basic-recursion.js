function reduce(arr, fn, initial) {

    // Recursive function that does the looping.
    var red = function(i, acc) {
        if (i < arr.length) {
            return red(i + 1, fn(acc, arr[i], i, arr));
        }
        else {
            return acc;
        }
    };

    return red(0, initial);
}

module.exports = reduce;
