exports = (typeof window === 'undefined') ? global : window;

exports.flowControlAnswers = {
  fizzBuzz : function(num) {
    // write a function that receives a number as its argument;
    // if the number is divisible by 3, the function should return 'fizz';
    // if the number is divisible by 5, the function should return 'buzz';
    // if the number is divisible by 3 and 5, the function should return
    // 'fizzbuzz';
    //
    // otherwise the function should return the number, or false if no number
    // was provided or the value provided is not a number
    var isDivisible = {
      by3: num % 3 === 0,
      by5: num % 5 === 0
    };

    var isNumeric = function(n) {
      return !isNaN(parseFloat(n)) && isFinite(n);
    }

    var ret;

    if (isDivisible.by3 && isDivisible.by5) {
      ret = 'fizzbuzz';
    } else if (isDivisible.by3) {
      ret = 'fizz';
    } else if (isDivisible.by5) {
      ret = 'buzz';
    } else {
      ret = isNumeric(num) ? num : false;
    }

    return ret;
  }
};
