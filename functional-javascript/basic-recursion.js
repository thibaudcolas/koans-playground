function reduce(arr, fn, initial) {

    // Recursive function that does the looping.
    var recurse = function(i, acc) {
        if (i < arr.length) {
            return recurse(i + 1, fn(acc, arr[i], i, arr));
        }
        else {
            return acc;
        }
    };

    return recurse(0, initial);
}

module.exports = reduce;
