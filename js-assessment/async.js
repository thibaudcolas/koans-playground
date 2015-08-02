exports = (typeof window === 'undefined') ? global : window;

exports.asyncAnswers = {
  async : function(value) {
    return new Promise(function(resolve, reject) {
      resolve(value);
    });
  },

  manipulateRemoteData : function(url) {
    return new Promise(function(resolve, reject) {
      window.$.getJSON(url, function(data) {
        var sortedNames = data.people.map(function(item) {
          return item.name;
        }).sort();

        resolve(sortedNames);
      });
    });
  }
};
