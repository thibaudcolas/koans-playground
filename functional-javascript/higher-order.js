function repeat(operation, num) {
    operation();

    if (num > 0) {
        // Call our function again, but with a lower `num`.
        repeat(operation, num - 1);
    }
}

module.exports = repeat;
