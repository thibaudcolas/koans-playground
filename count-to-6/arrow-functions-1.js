const inputs = process.argv.slice(2);

const result = inputs.map(str => str.charAt(0))
    .reduce((acc, str) => {
        return `${acc}${str}`;
    }, '');

console.log(`[${inputs}] becomes "${result}"`);
