const numbers = process.argv.splice(2, process.argv.length);

//const numbersPrint = numbers.toString().replace(/,/g, ', ');

const min = Math.min(...numbers);

console.log(`The minimum of [${numbers}] is ${min}`);
