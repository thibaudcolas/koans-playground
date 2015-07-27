function countWords(inputWords) {

    return inputWords.reduce(function(acc, word) {

        // Initialise count.
        if (!acc[word]) {
            acc[word] = 0;
        }

        acc[word]++;

        return acc;
    }, {});
}

module.exports = countWords;
