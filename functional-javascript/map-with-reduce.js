module.exports = function(arr, fn) {

    return arr.reduce(function(acc, cur, i, arr) {
        acc.push(fn(cur, i, arr));

        return acc;
    }, []);
};
