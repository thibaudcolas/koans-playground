exports = (typeof window === 'undefined') ? global : window;

exports.arraysAnswers = {

  indexOf : function(arr, item) {
    return arr.indexOf(item);
  },

  sum : function(arr) {
    return arr.reduce(function(acc, cur) {
      return acc + cur;
    }, 0);
  },

  remove : function(arr, item) {
    return arr.filter(function(it) {
      return it !== item;
    });
  },

  removeWithoutCopy : function(arr, item) {
    var positions = arr.reduce(function(acc, cur, i) {
        if (cur === item) {
            acc.unshift(i);
        }

        return acc;
    }, []);

    positions.forEach(function(i) {
        arr.splice(i, 1);
    });

    return arr;
  },

  append : function(arr, item) {
    arr.push(item);
    return arr;
  },

  truncate : function(arr) {
    return arr.slice(0, arr.length - 1);
  },

  prepend : function(arr, item) {
    arr.unshift(item);
    return arr;
  },

  curtail : function(arr) {
    return arr.slice(1);
  },

  concat : function(arr1, arr2) {
    return arr1.concat(arr2);
  },

  insert : function(arr, item, index) {
    arr.splice(index, 0, item);
    return arr;
  },

  count : function(arr, item) {
    return arr.reduce(function(acc, cur) {
      return acc + (cur === item ? 1 : 0);
    }, 0);
  },

  duplicates : function(arr) {
    return arr.filter(function(item, i) {
      return arr.lastIndexOf(item) === i && arr.indexOf(item) !== i;
    });
  },

  square : function(arr) {
    return arr.map(function(item) {
      return Math.pow(item, 2);
    });
  },

  findAllOccurrences : function(arr, target) {
    return arr.reduce(function(acc, cur, i) {
      if (cur === target) {
        acc.push(i);
      }

      return acc;
    }, []);
  }
};
