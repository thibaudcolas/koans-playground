const inputs = process.argv.slice(2);

// First, extract the first character of all input strings.
// Then, concatenate all those first chars with reduce.
const result = inputs.map(str => str.charAt(0))
    .reduce((chain, str) => {
        return `${chain}${str}`;
    }, '');

// No one will ever guess that format.
console.log(`[${inputs}] becomes "${result}"`);
