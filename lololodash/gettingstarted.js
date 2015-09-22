var _ = require('lodash');

module.exports = function(collection) {
    return _.where(collection, { active: true });
};
