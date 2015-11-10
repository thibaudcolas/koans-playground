const numbers = process.argv.splice(2, process.argv.length);

// Math.min can take lots of arguments.
const min = Math.min(...numbers);

// No one will ever guess that format.
console.log(`The minimum of [${numbers}] is ${min}`);
