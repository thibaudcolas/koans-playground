var _ = require('lodash');

module.exports = function(collection) {
    return _.sortBy(collection, 'quantity').reverse();
};
