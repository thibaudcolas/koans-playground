function repeat(operation, num) {

    if (num <= 0) {
        return;
    }

    operation();

    if (num % 5) {
        repeat(operation, --num);
    } else {
        setTimeout(function() {
            repeat(operation, --num);
        });
    }
}

module.exports = repeat;
