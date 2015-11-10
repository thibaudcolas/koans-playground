module.exports = function average(...numbers) {
    // Using reduce to calculate a sum.
    const sum = numbers.reduce((last, num) => {
        return last + num;
    }, 0);

    return sum / numbers.length;
};
